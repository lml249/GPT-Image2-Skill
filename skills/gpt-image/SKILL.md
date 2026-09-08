---
name: gpt-image
description: "Generate or edit raster images with the packaged GPT Image 2 CLI when that image-generation backend is requested."
metadata: {"openclaw":{"requires":{"anyBins":["gpt-image","uv","uvx"]},"primaryEnv":"OPENAI_API_KEY","homepage":"https://github.com/lml249/GPT-Image2-Skill"}}
---

# gpt-image

Agent runbook for GPT Image 2 generation/editing. Use the prompt library + packaged CLI. Do not reimplement image API code.

Requires Python 3.11+ and either `gpt-image`, `uv`, or `uvx`. API calls use `OPENAI_API_KEY` or the current Codex provider and may incur API charges.

## Operating loop

1. **Classify request**: `generate`, `edit`, `inpaint`, or `multi-reference`; identify asset type, exact text, aspect ratio, references, safety constraints, and budget/quality.
2. **Use references when helpful**: for style exploration or an uncertain prompt, open `references/gallery.md`; match the output type, then style/scene tags and nearby cases. Read the matching category or reusable template only. A precise request can go directly to the existing CLI without a gallery tour.
3. **Refine with craft**: load `references/craft.md` for dense text, diagrams, UI, data visualization, multi-panel layouts, weak prompts, or no close gallery match.
4. **Confer when useful**: before costly/ambiguous/high-polish calls, present 1–3 matched directions plus planned size/quality; ask at most one concise question. Skip long discussion for precise “generate now” requests.
5. **Preflight, no side effects**: use existing CLI/skill if present. Check command availability (`command -v gpt-image`), installed tool lists when the tool manager exists, or the runtime’s own skill registry when available. Do not assume a local home path in cloud/hosted runtimes.
6. **No blind setup**: do not reinstall, overwrite skill folders, create/modify `.env`, or write API keys unless the user explicitly requested setup. Global/shared installs are opt-in only.
7. **Execute via CLI only**: call `gpt-image` or `scripts/generate.py`. Do not create a new `generate.py`, SDK wrapper, or ad-hoc script for normal image requests.
8. **Report**: output file path(s), key flags, and one concise refinement suggestion if useful.

Fast path: precise prompt and authorized generation → check required inputs and use the CLI.

## CLI resolution

Preferred call order:

```bash
# Installed skill folder; use this path for automatic Codex-provider reuse
uv run "$SKILL_DIR/scripts/generate.py" -p "PROMPT" [-f OUT] [-i REF...] [-m MASK] [options]

# Existing CLI on PATH when OPENAI_API_KEY is already configured
gpt-image -p "PROMPT" [-f OUT] [-i REF...] [-m MASK] [options]

# Direct transient CLI when the user requested setup/one-off CLI execution
uvx --from git+https://github.com/lml249/GPT-Image2-Skill gpt-image -p "PROMPT" [options]
```

`scripts/generate.py` is a launcher: repo-local `src/gpt_image_cli` → installed `gpt-image` → PATH `gpt-image` → transient `uvx`/`uv` fallback.

## Key and cost rules

- Credential priority for the bundled launcher is process `OPENAI_API_KEY` → project `.env` → `~/.env` → current Codex provider in `${CODEX_HOME:-~/.codex}/config.toml`.
- Reuse a Codex provider only when it supplies both `experimental_bearer_token` and `base_url`. Always bind them together by replacing `OPENAI_BASE_URL` with that provider's URL.
- Accept provider URLs over HTTPS. Accept HTTP only for `localhost`, `127.0.0.1`, or `::1`; otherwise fail closed and report the missing key normally.
- A deliberately present blank process variable (`OPENAI_API_KEY=""`) disables provider fallback.
- Successful API calls may bill the account or provider represented by the selected credential.
- If host/runtime has native platform-managed image generation and the user wants that path, use the host tool instead of this CLI.
- If no credential source is usable, report the missing key or use host-native generation when requested; do not write secrets.
- Never print secret values.

## Flags

| Flag | Values | Use |
|---|---|---|
| `-p, --prompt` | string | Required prompt/edit instruction |
| `-f, --file` | path | Output path; auto-named if omitted |
| `-i, --image` | repeatable path | Use edits endpoint; supports multiple references |
| `-m, --mask` | PNG path | Inpaint with alpha mask; requires `-i` |
| `--model` | default `gpt-image-2` | Image model |
| `--size` | `1k`, `2k`, `4k`, `portrait`, `landscape`, `square`, `wide`, `tall`, or literal | Canvas size |
| `--quality` | `low`, `medium`, `high`, `auto` | Cost/quality dial |
| `-n, --n` | integer | Number of images |
| `--background` | `auto`, `opaque` | Generation background |
| `--moderation` | `auto`, `low` | Generation moderation setting |
| `--format` | `png`, `jpeg`, `webp` | Output encoding |
| `--compression` | `0-100` | JPEG/WebP compression |
| `--user` | string | Optional end-user identifier |

Quality policy:
- `low`: cheap drafts, broad exploration, many variants.
- `medium`: normal exploration, style probing, balanced cost.
- `high`: final assets, Chinese text, posters, diagrams, UI, paper figures, dense labels.

Size policy:
- default/social square: `1k` / `1024x1024`
- poster/mobile/beauty: `portrait`
- landscape/gameplay/photo: `landscape`
- print/paper figure: `2k`
- widescreen hero: `4k`
- vertical story/banner: `tall`

## Endpoint routing

| Mode | Trigger | Endpoint |
|---|---|---|
| Text-to-image | no `-i` | `/v1/images/generations` |
| Reference edit | one or more `-i` | `/v1/images/edits` |
| Inpaint | `-i` + `-m` | `/v1/images/edits` with mask |

Surface API errors verbatim enough for debugging; exit codes: `0` success, `1` API/refusal, `2` bad args/missing key.

## Reference loading

- `references/gallery.md`: routing index for the Reference Gallery Atlas. Load when selecting an example or style direction.
- `references/gallery-*.md`: concrete prompts, previews, paths, metadata, attribution. Load 1 category for normal requests; 2–3 for hybrids.
- `references/template-*.md`: four complete templates for scientific scale diagrams, conceptual typography posters, corporate brochure visuals, and product development boards. Select through `references/gallery.md`; fill the chosen template's inputs and preserve exact user copy. Use the user's language for the final prompt. If only a prompt is requested, return it without calling the image API.
- `references/craft.md`: prompt-craft checklist. Load for prompt repair, exact text, UI/data/diagram grammar, edit invariants, and multi-panel consistency.
- `references/openai-cookbook.md`: official parameter/model semantics. Load for API behavior or model capability questions.

Reference loading policy: load the smallest useful slice; never load all category files by default.

Gallery previews use HTTPS URLs pinned to this repository's image revision, so a standalone skill install does not need the full image directory. Prompt text remains available offline. If a preview cannot be accessed, use its source-page link or the prompt text and state the visual-access limit. Gallery preview URLs are not local `-i` inputs; use actual user/reference files for edits.

## Verification

- Before API call: confirm endpoint mode, size, quality, output path, and required reference/mask files.
- After CLI call: inspect the generated asset against the requested content and edit constraints; report actual output paths and relevant errors. Do not repeat paid calls after acceptance unless a defect or user request justifies it.
- For edits/inpaints: verify `-i` paths exist; verify `-m` exists when used.

Preserve `Curated` vs `Author + Source` metadata when adapting examples. Add new collected prompts to the Reference Gallery before README promotion.
