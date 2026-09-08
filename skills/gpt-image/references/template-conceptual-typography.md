# Conceptual Typography Poster / 概念字体海报

Use when the exact title should form the main visual structure of a finished poster. Tags: typography, editorial poster, campaign, cultural, 字体, 海报.

## Inputs and defaults

| Slot | Required content or default |
|---|---|
| `{{TITLE}}` | Exact title, including punctuation, script, and capitalization. |
| `{{METAPHOR}}` | One visual metaphor derived from the title's meaning or the user's brief. |
| `{{TYPE_DIRECTION}}` | Default: bold custom-looking letterforms, legible counters, deliberate spacing, subtle ink texture. |
| `{{PALETTE}}` | Default: warm paper, near-black type, and one accent suited to the theme. |
| `{{ASPECT_RATIO}}` | Default: 2:3 portrait. |

Choose one coherent metaphor when the brief leaves it open. Do not require a portrait for a person's name. Related gallery: [Typography & Posters, No. 33–45](gallery-typography-and-posters.md).

## Copyable prompt

```text
设计一张完整的概念字体海报，比例 {{ASPECT_RATIO}}。
唯一主标题必须逐字准确显示：“{{TITLE}}”。保留给定文字的语言、标点、大小写和字序。

字体构成主视觉：{{TYPE_DIRECTION}}。标题在远处也应清晰可读，字形变化必须保留识别性。
以“{{METAPHOR}}”作为唯一核心视觉隐喻。让相关物体、人物或景观穿过、托起、框住或投影到字形，与文字共同表达主题；保留字形关键笔画。

配色：{{PALETTE}}。利用大小对比、负空间、有限元素和克制的纸张印刷质感建立层级。全部视觉细节服务标题含义。
输出一张成品海报。避免多方案网格、展示板、样机、过程说明、无关图标、额外大字标题、随机文字和难以辨认的字形。不要翻译或改写主标题。
```

## Pitfalls and execution

- Literal title text must survive metaphor and stylization; avoid obscuring distinguishing strokes.
- A poster request should not become a font specimen or moodboard. Add a secondary line only when the user supplies or requests it.
- For authorized generation, use the existing CLI with `--quality high`; the default ratio matches `--size portrait`. Check every title character in the output.

## Attribution

Adapted from freestylefly's [conceptual typography template](https://github.com/freestylefly/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-poster) and [case 355](https://github.com/freestylefly/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-355), attributed there to [@dotey](https://x.com/dotey/status/2048793351290327381). This is an adapted template, not an original gallery image. See [source and license notes](template-sources.md).
