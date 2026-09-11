# GPT Image 2.5 model guide

GPT Image 2.5 has two API model IDs:

- `gpt-image-2.5-sunburst`: quality-first base model for detailed creative work and difficult edits. This skill uses it by default.
- `gpt-image-2.5-flare`: speed-first small model with quality comparable to GPT Image 2. Select it explicitly for latency-sensitive or high-volume work.

Both models support text-to-image generation, image editing, and transparent backgrounds. The API accepts `quality=auto`, `low`, `medium`, `high`, `xhigh`, or `max`; it also accepts `background=auto`, `opaque`, or `transparent`. The CLI keeps `high` as its default quality so model migration does not silently lower fidelity. `input_fidelity` is omitted for GPT Image 2.5.

## Migration workflow

1. Keep a GPT Image 2 baseline prompt, reference images, size, output format, and quality setting.
2. Test Sunburst first for complex identity-sensitive edits, dense text, and detailed layouts. Test Flare first when latency is the main constraint or GPT Image 2 already meets the quality bar.
3. Compare instruction following, subject/identity preservation, exact text, unwanted changes, transparency, response time, retries, and cost on the real workflow.
4. Change one setting at a time. Keep `gpt-image-2` available with `--model gpt-image-2` while the provider supports it.

For GPT Image 2, the CLI rejects `xhigh`, `max`, and `--background transparent` locally because those options are documented for GPT Image 2.5. Custom model IDs remain pass-through so a compatible provider can decide their supported options.

## CLI examples

```bash
# Default: GPT Image 2.5 Sunburst
gpt-image -p "a photorealistic tea poster" --quality high --size portrait

# Faster model
gpt-image -p "four social thumbnail variants" --model gpt-image-2.5-flare --quality medium -n 4

# Legacy compatibility
gpt-image -p "a photorealistic tea poster" --model gpt-image-2 --quality high

# Transparent asset (GPT Image 2.5)
gpt-image -p "a simple bakery logo with clean alpha edges" --background transparent --format png
```

Keep the provider URL and credentials unchanged. A provider or gateway must explicitly route the selected model; this skill does not switch accounts, endpoints, or API keys. Errors from a provider that does not expose a 2.5 model are surfaced as API errors.

## Sources

- [OpenAI Image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting)
- [Introducing ChatGPT Images 2.5](https://openai.com/index/introducing-chatgpt-images-2-5)
