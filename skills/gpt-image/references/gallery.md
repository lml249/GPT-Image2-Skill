# GPT Image 2 Prompt Gallery Index

Routing index for 162 numbered cases across 31 categories, plus four reusable templates counted separately. README is a selected showcase. Use this index when choosing a style, completing a brief, or repairing a prompt; a precise authorized request can use the CLI directly. Do **not** load every category file by default.

Match the requested output type first, then style and scene tags, then nearby cases. Each category starts with selection notes: necessary inputs, typical failures, and relevant case numbers. Read one matching file; use two or three only when a hybrid request needs them. Consult `craft.md` for the specific prompt-writing issue.

## Routing tags

Use the first matching output type, then refine with a style and scene tag. These labels follow the upstream style-library vocabulary while keeping this gallery's 31 focused files:

- **Output types:** UI, infographic, poster, product, brand, architecture, photography, illustration, character, scene, history, document, edit, technical, research, and special use cases.
- **Style tags:** realistic, 3D, illustration, classical, editorial, poster, product, brand, UI, charts, technical, and watercolor/ink.
- **Scene tags:** commerce, creative, education, fashion, food, history, social, story, tech, and travel.

When a request matches a tag but no focused case, use [`template-catalog-upstream.md`](template-catalog-upstream.md) for a compact fillable structure, then return to the closest gallery file for a concrete visual reference.

Each `gallery-*.md` file contains full prompt text, original attribution, HTTPS image previews, and image-source links. Image links are pinned to repository revision `76fb666a1aea94c463014351429ca1fed6bcf4f4`; they work independently of the local `docs/` tree. Prompts remain readable offline. If image access fails, use the source link or text and report that the preview was not inspected. These URLs do not replace local reference files required by CLI `-i`.

## Reusable templates

Read only the matching template. Each includes fillable inputs, defaults, a complete prompt, execution notes, and source attribution. These four templates add no numbered gallery cases.

| Output / use when | Style and scene tags | Template |
|---|---|---|
| Micro-to-macro science explainer / 科学尺度缩放图 | infographic, 3D cutaway; science, education | [Scientific scale diagram](template-scientific-scale.md) |
| Exact title becomes the main visual / 概念字体海报 | typography, editorial; campaign, culture | [Conceptual typography poster](template-conceptual-typography.md) |
| Coordinated brochure page previews / 企业画册视觉方案 | brand, editorial; corporate, publishing | [Corporate brochure visual system](template-corporate-brochure.md) |
| Inspiration, evolution, structure, and materials / 产品研发拆解板 | industrial design, technical; product, concept | [Product development board](template-product-development.md) |

For a known template, go directly to its file. Preserve exact user copy and use the requested language for the final prompt. A prompt-only request does not trigger generation. [Adaptation sources and license](template-sources.md) record the upstream revision and credits.

## Category files

| Category | File | Range | Count |
|---|---|---:|---:|
| 🎌 Anime & Manga | [`gallery-anime-and-manga.md`](gallery-anime-and-manga.md) | No. 1–12 | 12 |
| 🎮 Gaming | [`gallery-gaming.md`](gallery-gaming.md) | No. 13–22 | 10 |
| 🤖 Retro & Cyberpunk | [`gallery-retro-and-cyberpunk.md`](gallery-retro-and-cyberpunk.md) | No. 23–25 | 3 |
| 🎬 Cinematic & Animation | [`gallery-cinematic-and-animation.md`](gallery-cinematic-and-animation.md) | No. 26–30 | 5 |
| 👤 Character Design | [`gallery-character-design.md`](gallery-character-design.md) | No. 31–32 | 2 |
| 📝 Typography & Posters | [`gallery-typography-and-posters.md`](gallery-typography-and-posters.md) | No. 33–45 | 13 |
| 🎨 Illustration | [`gallery-illustration.md`](gallery-illustration.md) | No. 46–47 | 2 |
| 💧 Watercolor | [`gallery-watercolor.md`](gallery-watercolor.md) | No. 48–49 | 2 |
| 🖌️ Ink & Chinese | [`gallery-ink-and-chinese.md`](gallery-ink-and-chinese.md) | No. 50–51 | 2 |
| 🕹️ Pixel Art | [`gallery-pixel-art.md`](gallery-pixel-art.md) | No. 52–53 | 2 |
| 📐 Isometric | [`gallery-isometric.md`](gallery-isometric.md) | No. 54–55 | 2 |
| 📦 Product & Food | [`gallery-product-and-food.md`](gallery-product-and-food.md) | No. 56–59 | 4 |
| 🧩 Brand Systems & Identity | [`gallery-brand-systems-and-identity.md`](gallery-brand-systems-and-identity.md) | No. 60–62 | 3 |
| 📷 Photography | [`gallery-photography.md`](gallery-photography.md) | No. 63–66 | 4 |
| 📊 Infographics & Field Guides | [`gallery-infographics-and-field-guides.md`](gallery-infographics-and-field-guides.md) | No. 67–74 | 8 |
| 📚 Research Paper Figures | [`gallery-research-paper-figures.md`](gallery-research-paper-figures.md) | No. 75–95 | 21 |
| 🏢 Official OpenAI Cookbook Examples | [`gallery-official-openai-cookbook-examples.md`](gallery-official-openai-cookbook-examples.md) | No. 96–99 | 4 |
| ✨ Edit Endpoint Showcase | [`gallery-edit-endpoint-showcase.md`](gallery-edit-endpoint-showcase.md) | No. 100–101 | 2 |
| 📱 UI/UX Mockups | [`gallery-ui-ux-mockups.md`](gallery-ui-ux-mockups.md) | No. 102–106 | 5 |
| 📊 Data Visualization | [`gallery-data-visualization.md`](gallery-data-visualization.md) | No. 107–111 | 5 |
| ⚙️ Technical Illustration | [`gallery-technical-illustration.md`](gallery-technical-illustration.md) | No. 112–116 | 5 |
| 🏛️ Architecture & Interior | [`gallery-architecture-and-interior.md`](gallery-architecture-and-interior.md) | No. 117–121 | 5 |
| 🔬 Scientific & Educational | [`gallery-scientific-and-educational.md`](gallery-scientific-and-educational.md) | No. 122–128 | 7 |
| 👗 Fashion Editorial | [`gallery-fashion-editorial.md`](gallery-fashion-editorial.md) | No. 129–135 | 7 |
| 🎨 Fine Art Painting | [`gallery-fine-art-painting.md`](gallery-fine-art-painting.md) | No. 136–140 | 5 |
| ✏️ More Illustration Styles | [`gallery-more-illustration-styles.md`](gallery-more-illustration-styles.md) | No. 141–146 | 6 |
| 🎥 Cinematic Film References | [`gallery-cinematic-film-references.md`](gallery-cinematic-film-references.md) | No. 147–152 | 6 |
| 💄 Beauty & Lifestyle | [`gallery-beauty-and-lifestyle.md`](gallery-beauty-and-lifestyle.md) | No. 153–154 | 2 |
| 🎟️ Events & Experience | [`gallery-events-and-experience.md`](gallery-events-and-experience.md) | No. 155–156 | 2 |
| 🖋️ Tattoo Design | [`gallery-tattoo-design.md`](gallery-tattoo-design.md) | No. 157–160 | 4 |
| 🖥️ Screen Photography | [`gallery-screen-photography.md`](gallery-screen-photography.md) | No. 161–162 | 2 |

## Loading policy

- Use this index when selecting a category or template; do not read the whole Reference Gallery into context.
- Read `craft.md` when a prompt needs repair or complex layout/text constraints.
- Read one matching category or template for normal requests; read two or three only when hybrid styles require it.
- Preserve `Curated` versus `Author + Source` metadata when adapting examples into README/gallery entries.
- If entries move, update both this index and the corresponding category file in the same PR. Promote to README only when the example belongs in the selected visual showcase.
