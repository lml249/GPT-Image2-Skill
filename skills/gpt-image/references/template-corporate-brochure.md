# Corporate Brochure Visual System / 企业画册视觉系统

Use for a raster preview of a coordinated brochure or a specified brochure page. Tags: brand, editorial, corporate, publishing, 企业画册, 品牌.

This produces image concepts. Requests for editable documents, real page layout files, or print-ready PDFs need an appropriate document/layout workflow. Do not describe this output as an editable brochure.

## Inputs and defaults

| Slot | Required content or default |
|---|---|
| `{{BRAND}}` | Brand name and industry/product/solution. |
| `{{CONTENT}}` | Supplied titles, concise copy, facts, and requested sections; do not invent clients, performance claims, or contact details. |
| `{{BRAND_SYSTEM}}` | Provided logo, colors, type direction and references; default to a restrained navy/off-white editorial system if unspecified. |
| `{{VIEW}}` | Default: one overview board containing cover, back cover, and four interior-page previews. For a requested single page, use only that page. |
| `{{ASPECT_RATIO}}` | Default: 3:2 landscape for the overview; use the requested page ratio for a single page. |

An overview is one image, not six image API outputs. Set CLI `-n` only from the user's actual image count. Related gallery: [Brand Systems, No. 60–62](gallery-brand-systems-and-identity.md), [Typography & Posters](gallery-typography-and-posters.md).

## Copyable prompt

```text
为“{{BRAND}}”设计企业画册的视觉方案，输出 {{VIEW}}，画面比例 {{ASPECT_RATIO}}。

统一品牌规范：{{BRAND_SYSTEM}}。
准确使用以下给定内容与事实：
{{CONTENT}}

以封面与封底、企业介绍、产品或技术、应用场景、案例与合作信息作为可选页面角色，只展示本次要求且有内容支持的部分。
全套页面共享网格、页边距、标题层级、字体方向、配色和图像语言。各页有明确主视觉和充足留白，建立封面与内页的识别关系。
准确显示给定的短标题和关键标签。总览中的正文区域保持简洁；没有提供正文时使用留白，不生成伪装成真实文案的微小字符。不得自行添加客户标志、业绩数字、认证、地址或电话。

呈现清楚的画册视觉预览，页序可辨，图像与文字层级统一。避免每页更换品牌风格、文字拥挤、无依据的数据和额外页面。该输出是栅格视觉方案。
```

## Pitfalls and execution

- Do not compress full paragraphs into small page thumbnails. If exact body copy is essential, work on the relevant single page or use a document/layout workflow.
- For provided logo/product references, assign each local input a role and preserve those elements during edits.
- For authorized overview generation, use the existing CLI with `--size landscape --quality high`. Check cross-page branding and supplied facts. Do not automatically generate individual pages after the overview.

## Attribution

Adapted from freestylefly's [corporate brochure template](https://github.com/freestylefly/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-document) and [case 453](https://github.com/freestylefly/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-453), attributed there to [@MrLarus](https://x.com/MrLarus/status/2056974720893939950). This is an adapted visual template, not an original gallery image. See [source and license notes](template-sources.md).
