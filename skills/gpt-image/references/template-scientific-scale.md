# Scientific Scale Diagram / 科学尺度缩放图

Use when a science explainer needs a connected view from microscopic detail to a larger structure. Tags: infographic, 3D cutaway, education, micro-to-macro, 科普, 尺度缩放.

## Inputs and defaults

| Slot | Required content or default |
|---|---|
| `{{SUBJECT}}` | Exact subject and intended audience. |
| `{{TITLE}}` | Exact visible title, preserving the user's language. |
| `{{SCALE_FRAMES}}` | Ordered frames, each with a name, supplied/verified size or magnification and unit, a short insight, and a distinct visual detail. Use 6 frames by default, or the user's supplied count. |
| `{{PALETTE}}` | Default: off-white, slate blue, and a restrained amber accent. |
| `{{ASPECT_RATIO}}` | Default: 3:2 landscape; align the actual CLI size with this ratio. |

Resolve scientific values before generation. If the brief is conceptual and has no measured values, label the diagram as schematic and omit numeric scale claims. Related gallery: [Scientific & Educational, No. 122–128](gallery-scientific-and-educational.md), [Infographics, No. 68–74](gallery-infographics-and-field-guides.md).

## Copyable prompt

```text
为“{{SUBJECT}}”设计一张科学尺度缩放信息图，横向构图，比例 {{ASPECT_RATIO}}。
画面准确显示标题：“{{TITLE}}”。

按从微观到宏观的顺序安排以下尺度框：
{{SCALE_FRAMES}}

让每个尺度框表现该层级真正不同的结构和细节，用细线连接相邻层级，明确局部与整体的关系。保持一致的框形、标签位置和阅读方向；各框是独立缩放视窗，不暗示框的大小代表真实物体尺寸。
每框只放尺度名称、提供的数值与单位，以及一句简短洞察。严格使用给定数据；未提供的测量值、倍率和结论不得自行补写。

风格为科学编辑图解与精细三维剖面结合，配色 {{PALETTE}}，背景清爽，结构清晰，标签易读。标题、尺度标签和连接线建立明确的信息层级。
避免重复同一幅细节、无意义放大镜图标、长段文字、混乱连线、错误单位和未经提供的数字。只输出一张完整信息图。
```

## Pitfalls and execution

- A magnified view needs different structural detail at each level; changing only object size is insufficient.
- Keep units and layer order explicit. If numeric scales are absent, include the exact label "示意图 / 不按比例" or its requested-language equivalent.
- For authorized generation, use the existing CLI with `--quality high`; the default ratio matches `--size landscape`. Inspect labels and scale order after generation. This template does not verify scientific claims for the user.

## Attribution

Adapted from freestylefly's [science-scale template](https://github.com/freestylefly/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-infographic). Related source example: [case 380](https://github.com/freestylefly/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-380), attributed there to [@Gdgtify](https://x.com/Gdgtify/status/2051288232613351571). These are adapted instructions, not a newly generated gallery example. See [source and license notes](template-sources.md).
