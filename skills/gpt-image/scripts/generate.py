#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "openai>=1.55",
#     "python-dotenv>=1.0",
# ]
# ///
"""Skill launcher for the shared gpt-image CLI.

Resolution order:
1. Repo checkout / full plugin install: import ../../../src/gpt_image_cli/cli.py.
2. Python environment already has gpt_image_cli installed: import it directly.
3. Shell has a gpt-image executable: delegate to it.
4. Final fallback: uvx installs/runs the GitHub CLI package transiently.

This keeps `skills/gpt-image` usable when copied as a standalone skill folder
while preserving one canonical implementation for the installable Python CLI.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path
from urllib.parse import urlsplit

_REPO_URL = "git+https://github.com/lml249/GPT-Image2-Skill"
_DOTENV_API_KEY_RE = re.compile(r"^\s*(?:export\s+)?OPENAI_API_KEY\s*=")
_LOOPBACK_HOSTS = {"localhost", "127.0.0.1", "::1"}


def _dotenv_declares_api_key(path: Path) -> bool:
    """Return whether a dotenv file assigns OPENAI_API_KEY."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError):
        return False
    return any(_DOTENV_API_KEY_RE.match(line) for line in lines)


def _is_safe_provider_url(value: str) -> bool:
    """Allow HTTPS endpoints and local HTTP development endpoints only."""
    try:
        parsed = urlsplit(value)
        hostname = parsed.hostname
        _ = parsed.port
    except ValueError:
        return False

    if (
        not parsed.netloc
        or not hostname
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
    ):
        return False
    if parsed.scheme == "https":
        return True
    return parsed.scheme == "http" and hostname.lower() in _LOOPBACK_HOSTS


def _configure_codex_provider(
    *,
    cwd: Path | None = None,
    home: Path | None = None,
) -> bool:
    """Reuse the current Codex provider when no regular API key source exists."""
    if "OPENAI_API_KEY" in os.environ:
        return False

    current_dir = cwd or Path.cwd()
    home_dir = home or Path.home()
    if _dotenv_declares_api_key(current_dir / ".env"):
        return False
    if _dotenv_declares_api_key(home_dir / ".env"):
        return False

    configured_home = os.environ.get("CODEX_HOME")
    codex_home = (
        Path(configured_home).expanduser()
        if configured_home
        else home_dir / ".codex"
    )
    try:
        with (codex_home / "config.toml").open("rb") as config_file:
            config = tomllib.load(config_file)
    except (OSError, tomllib.TOMLDecodeError):
        return False

    provider_name = config.get("model_provider")
    providers = config.get("model_providers")
    if not isinstance(provider_name, str) or not isinstance(providers, dict):
        return False

    provider = providers.get(provider_name)
    if not isinstance(provider, dict):
        return False

    token = provider.get("experimental_bearer_token")
    base_url = provider.get("base_url")
    if not isinstance(token, str) or not token:
        return False
    if not isinstance(base_url, str) or not _is_safe_provider_url(base_url):
        return False

    os.environ["OPENAI_API_KEY"] = token
    os.environ["OPENAI_BASE_URL"] = base_url.rstrip("/")
    print(
        "note: using the current Codex provider for GPT Image API access.",
        file=sys.stderr,
    )
    return True


def _import_local_or_installed_main():
    """Return gpt_image_cli.cli.main from repo-local src or installed package."""
    script_path = Path(__file__).resolve()

    # Full plugin/repo layout: <repo>/skills/gpt-image/scripts/generate.py
    # Standalone skill installs do not have this sibling src/ tree, so guard it.
    if len(script_path.parents) > 3:
        repo_src = script_path.parents[3] / "src"
        if (repo_src / "gpt_image_cli" / "cli.py").is_file():
            sys.path.insert(0, str(repo_src))

    try:
        from gpt_image_cli.cli import main  # type: ignore
    except ModuleNotFoundError:
        return None
    return main


def _delegate(command: list[str]) -> int:
    """Run another CLI process with the original argv and return its exit code."""
    completed = subprocess.run(command + sys.argv[1:], check=False)
    return completed.returncode


def main() -> int:
    _configure_codex_provider()

    cli_main = _import_local_or_installed_main()
    if cli_main is not None:
        return int(cli_main() or 0)

    executable = shutil.which("gpt-image")
    if executable:
        return _delegate([executable])

    uvx = shutil.which("uvx") or shutil.which("uv")
    if uvx:
        if Path(uvx).name == "uv":
            return _delegate([uvx, "tool", "run", "--from", _REPO_URL, "gpt-image"])
        return _delegate([uvx, "--from", _REPO_URL, "gpt-image"])

    print(
        "error: could not find the gpt-image CLI backend. Install uv and run this skill "
        "again, or install the CLI first with:\n"
        f"  uv tool install {_REPO_URL}\n"
        "Then retry the same command.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
