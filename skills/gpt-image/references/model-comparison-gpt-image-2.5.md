# GPT Image 2.5 comparison notes

The upstream [awesome-gpt-image-2 2.5 spotlight](https://github.com/freestylefly/awesome-gpt-image-2/tree/0dc09c46c8a30b1fdd89c18cc78a894dac2104e3/docs/design/gpt-image-2-5) contains four one-shot recreations using complete gallery prompts. They are useful prompt and review examples, not a controlled model benchmark: the upstream records state that the built-in tool did not return an exact model ID, quality setting, or cost, and the original generation conditions were not independently verified.

## Showcase records

| Case | What to inspect | Upstream record |
|---|---|---|
| #532 lemon drink six-panel campaign | Grid consistency, recurring miniature person, product text, instruction following | [real-cases.md](https://github.com/freestylefly/awesome-gpt-image-2/blob/0dc09c46c8a30b1fdd89c18cc78a894dac2104e3/docs/design/gpt-image-2-5/real-cases.md) |
| #527 Rio paper-cut travel poster | Layered scene structure, landmark coverage, annotations, material depth | [real-cases.md](https://github.com/freestylefly/awesome-gpt-image-2/blob/0dc09c46c8a30b1fdd89c18cc78a894dac2104e3/docs/design/gpt-image-2-5/real-cases.md) |
| #523 Manhattan watercolor travel illustration | Foreground/background balance, location cues, painterly consistency | [real-cases.md](https://github.com/freestylefly/awesome-gpt-image-2/blob/0dc09c46c8a30b1fdd89c18cc78a894dac2104e3/docs/design/gpt-image-2-5/real-cases.md) |
| #510 Bichon Shop icon | Single-object silhouette, fur and paper-bag texture, exact brand text | [real-cases.md](https://github.com/freestylefly/awesome-gpt-image-2/blob/0dc09c46c8a30b1fdd89c18cc78a894dac2104e3/docs/design/gpt-image-2-5/real-cases.md) |

## Controlled migration protocol

For a real workflow, create the GPT Image 2 baseline first. Keep the prompt, reference files and their order, canvas size, output format, quality, number of images, and background identical. Compare Sunburst and Flare separately, changing one model at a time. Review:

- exact text and label accuracy;
- identity and geometry preservation in edits;
- layout and multi-panel consistency;
- unwanted changes outside the requested edit;
- response time, retries, provider errors, and cost when available.

Record the provider, endpoint, model ID, quality, size, format, timestamp, output dimensions, and any refusal or transport error. Do not describe a result as a 2.5 capability guarantee when the provider did not expose the actual model ID.

The current CLI defaults to `gpt-image-2.5-sunburst`; use `--model gpt-image-2.5-flare` for a speed comparison and `--model gpt-image-2` for a legacy baseline. Keep provider URL and credentials unchanged during the comparison.

## Sources

- [OpenAI Image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting)
- [GPT Image 2.5 Sunburst](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst)
- [GPT Image 2.5 Flare](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare)
