from __future__ import annotations

import importlib.util
import os
import tempfile
import unittest
from contextlib import redirect_stderr
from io import StringIO
from pathlib import Path
from unittest.mock import patch

REPO_ROOT = Path(__file__).resolve().parents[1]
LAUNCHER_PATH = REPO_ROOT / "skills" / "gpt-image" / "scripts" / "generate.py"


def load_launcher():
    spec = importlib.util.spec_from_file_location("gpt_image_skill_launcher", LAUNCHER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load launcher from {LAUNCHER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CodexProviderFallbackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.launcher = load_launcher()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)
        self.cwd = self.root / "project"
        self.home = self.root / "home"
        self.codex_home = self.home / ".codex"
        self.cwd.mkdir()
        self.codex_home.mkdir(parents=True)

    def write_config(
        self,
        *,
        base_url: str = "https://images.example.test/v1",
        token: str | None = "provider-secret",
        provider: str = "ccswitch",
    ) -> None:
        token_line = (
            f'experimental_bearer_token = "{token}"\n' if token is not None else ""
        )
        (self.codex_home / "config.toml").write_text(
            f'model_provider = "{provider}"\n'
            f"[model_providers.{provider}]\n"
            f'base_url = "{base_url}"\n'
            f"{token_line}",
            encoding="utf-8",
        )

    def configure(self, env: dict[str, str]) -> tuple[bool, str]:
        stderr = StringIO()
        with patch.dict(os.environ, env, clear=True), redirect_stderr(stderr):
            configured = self.launcher._configure_codex_provider(
                cwd=self.cwd,
                home=self.home,
            )
            resulting_env = dict(os.environ)
        env.clear()
        env.update(resulting_env)
        return configured, stderr.getvalue()

    def test_existing_process_api_key_is_never_overwritten(self) -> None:
        self.write_config()
        env = {
            "OPENAI_API_KEY": "explicit-secret",
            "OPENAI_BASE_URL": "https://explicit.example.test/v1",
        }

        configured, stderr = self.configure(env)

        self.assertFalse(configured)
        self.assertEqual(env["OPENAI_API_KEY"], "explicit-secret")
        self.assertEqual(
            env["OPENAI_BASE_URL"], "https://explicit.example.test/v1"
        )
        self.assertEqual(stderr, "")

    def test_project_dotenv_declaration_prevents_provider_fallback(self) -> None:
        self.write_config()
        (self.cwd / ".env").write_text(
            "OPENAI_API_KEY=project-secret\n", encoding="utf-8"
        )
        env: dict[str, str] = {}

        configured, _ = self.configure(env)

        self.assertFalse(configured)
        self.assertNotIn("OPENAI_API_KEY", env)
        self.assertNotIn("OPENAI_BASE_URL", env)

    def test_home_dotenv_declaration_prevents_provider_fallback(self) -> None:
        self.write_config()
        (self.home / ".env").write_text(
            "export OPENAI_API_KEY=home-secret\n", encoding="utf-8"
        )
        env: dict[str, str] = {}

        configured, _ = self.configure(env)

        self.assertFalse(configured)
        self.assertNotIn("OPENAI_API_KEY", env)
        self.assertNotIn("OPENAI_BASE_URL", env)

    def test_valid_https_provider_loads_token_and_base_url(self) -> None:
        self.write_config()
        env: dict[str, str] = {}

        configured, stderr = self.configure(env)

        self.assertTrue(configured)
        self.assertEqual(env["OPENAI_API_KEY"], "provider-secret")
        self.assertEqual(
            env["OPENAI_BASE_URL"], "https://images.example.test/v1"
        )
        self.assertIn("current Codex provider", stderr)
        self.assertNotIn("provider-secret", stderr)

    def test_external_http_provider_is_rejected(self) -> None:
        self.write_config(base_url="http://images.example.test/v1")
        env: dict[str, str] = {}

        configured, stderr = self.configure(env)

        self.assertFalse(configured)
        self.assertNotIn("OPENAI_API_KEY", env)
        self.assertNotIn("OPENAI_BASE_URL", env)
        self.assertEqual(stderr, "")

    def test_loopback_http_provider_is_accepted(self) -> None:
        self.write_config(base_url="http://127.0.0.1:8080/v1")
        env: dict[str, str] = {}

        configured, _ = self.configure(env)

        self.assertTrue(configured)
        self.assertEqual(env["OPENAI_API_KEY"], "provider-secret")
        self.assertEqual(env["OPENAI_BASE_URL"], "http://127.0.0.1:8080/v1")

    def test_missing_provider_or_token_fails_closed(self) -> None:
        self.write_config(provider="missing")
        config_path = self.codex_home / "config.toml"
        config_path.write_text(
            'model_provider = "missing"\n'
            "[model_providers.ccswitch]\n"
            'base_url = "https://images.example.test/v1"\n'
            'experimental_bearer_token = "provider-secret"\n',
            encoding="utf-8",
        )
        env: dict[str, str] = {}

        configured, _ = self.configure(env)

        self.assertFalse(configured)
        self.assertNotIn("OPENAI_API_KEY", env)
        self.assertNotIn("OPENAI_BASE_URL", env)

        self.write_config(token=None)
        configured, _ = self.configure(env)

        self.assertFalse(configured)
        self.assertNotIn("OPENAI_API_KEY", env)
        self.assertNotIn("OPENAI_BASE_URL", env)

    def test_provider_base_url_replaces_preexisting_mismatched_url(self) -> None:
        self.write_config()
        env = {"OPENAI_BASE_URL": "https://unrelated.example.test/v1"}

        configured, _ = self.configure(env)

        self.assertTrue(configured)
        self.assertEqual(env["OPENAI_API_KEY"], "provider-secret")
        self.assertEqual(
            env["OPENAI_BASE_URL"], "https://images.example.test/v1"
        )


if __name__ == "__main__":
    unittest.main()
