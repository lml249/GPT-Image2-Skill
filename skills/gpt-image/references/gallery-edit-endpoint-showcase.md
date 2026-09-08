# ✨ Edit Endpoint Showcase

Range: No. 100–101 · Count: 2

Load this file only when the request matches this category. For cross-cutting writing rules, pair it with `craft.md`.

## Selection notes

- Use when: Transforming an existing image while retaining its layout or content.
- Necessary inputs: Local input files, exact change, preserved elements, and local mask if applicable.
- Style / scene tags: reference edit, mockup, restyle; image editing; 编辑, 局部修改.
- Typical failures: Generating afresh without the input; shifting unchanged text or geometry; passing a preview URL as a local file.
- Related cases in this file: No. 100, No. 101.

### No. 100 · Chess board → winter evening (edit via `/v1/images/edits`) 🆕

- Images:
  - [Preview](https://raw.githubusercontent.com/lml249/GPT-Image2-Skill/76fb666a1aea94c463014351429ca1fed6bcf4f4/docs/photography/chess-midgame.png) · [Image source](https://github.com/lml249/GPT-Image2-Skill/blob/76fb666a1aea94c463014351429ca1fed6bcf4f4/docs/photography/chess-midgame.png) — Chess mid-game original

    <img src="https://raw.githubusercontent.com/lml249/GPT-Image2-Skill/76fb666a1aea94c463014351429ca1fed6bcf4f4/docs/photography/chess-midgame.png" alt="Chess mid-game original" width="420"/>
  - [Preview](https://raw.githubusercontent.com/lml249/GPT-Image2-Skill/76fb666a1aea94c463014351429ca1fed6bcf4f4/docs/edit-endpoint-showcase/edit-chess-winter.png) · [Image source](https://github.com/lml249/GPT-Image2-Skill/blob/76fb666a1aea94c463014351429ca1fed6bcf4f4/docs/edit-endpoint-showcase/edit-chess-winter.png) — Chess mid-game restyled as winter scene

    <img src="https://raw.githubusercontent.com/lml249/GPT-Image2-Skill/76fb666a1aea94c463014351429ca1fed6bcf4f4/docs/edit-endpoint-showcase/edit-chess-winter.png" alt="Chess mid-game restyled as winter scene" width="420"/>
- Metadata: Edit Endpoint Showcase · `landscape` · `1536x1024` · Author: OpenAI · Source: [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb)

```text
Make it a winter evening with heavy snowfall, snow dusted on the board and pieces, breath vapor in the air, cold blue-grey lighting, chess position still clearly readable. Preserve the original chess-board composition and landscape aspect ratio exactly; keep the board and pieces aligned and readable.
```

### No. 101 · Tea poster → metro lightbox mockup

- Image: [Preview](https://raw.githubusercontent.com/lml249/GPT-Image2-Skill/76fb666a1aea94c463014351429ca1fed6bcf4f4/docs/edit-endpoint-showcase/tea-poster-metro-lightbox.png) · [Image source](https://github.com/lml249/GPT-Image2-Skill/blob/76fb666a1aea94c463014351429ca1fed6bcf4f4/docs/edit-endpoint-showcase/tea-poster-metro-lightbox.png)

  <img src="https://raw.githubusercontent.com/lml249/GPT-Image2-Skill/76fb666a1aea94c463014351429ca1fed6bcf4f4/docs/edit-endpoint-showcase/tea-poster-metro-lightbox.png" alt="tea poster metro lightbox" width="420"/>
- Input image: [Preview](https://raw.githubusercontent.com/lml249/GPT-Image2-Skill/76fb666a1aea94c463014351429ca1fed6bcf4f4/docs/typography-posters/tea-poster.png) · [Image source](https://github.com/lml249/GPT-Image2-Skill/blob/76fb666a1aea94c463014351429ca1fed6bcf4f4/docs/typography-posters/tea-poster.png)

  <img src="https://raw.githubusercontent.com/lml249/GPT-Image2-Skill/76fb666a1aea94c463014351429ca1fed6bcf4f4/docs/typography-posters/tea-poster.png" alt="tea poster" width="420"/>
- Metadata: Edit Endpoint Showcase · `portrait` · `1024x1536` · Curated

```text
Transform the provided tea poster into a realistic metro-station lightbox mockup while preserving the poster artwork and Chinese typography as much as possible. Show the poster behind glossy glass in a vertical illuminated advertising frame on a clean subway platform wall. Add subtle reflections, brushed metal frame, floor tiles, soft overhead transit lighting, and a few blurred commuters in the distance. Keep the poster straight, legible, and dominant; do not redesign the poster, do not change its main text, and do not add fake brand logos.
```
