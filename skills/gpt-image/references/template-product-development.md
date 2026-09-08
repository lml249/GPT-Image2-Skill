# Product Development Board / 产品研发拆解板

Use when an industrial design concept needs its inspiration, evolution, use, structure, and materials shown together. Tags: industrial design, technical illustration, product, concept, 研发, 拆解板.

## Inputs and defaults

| Slot | Required content or default |
|---|---|
| `{{PRODUCT}}` | Product/furniture/device type and intended user. |
| `{{INSPIRATION}}` | Source shape, natural form, material behavior, or mechanism. |
| `{{DESIGN_INTENT}}` | One sentence connecting intended function with the inspiration. |
| `{{MATERIALS_AND_FACTS}}` | Supplied materials, structural constraints, and confirmed dimensions/specifications. Omit unknown numbers and mark unverified design details as conceptual. |
| `{{ASPECT_RATIO}}` | Default: 3:2 landscape. |

Default to three intermediate form studies and a white background with fine graphite annotations. Related gallery: [Technical Illustration, No. 112–116](gallery-technical-illustration.md), [Product & Food, No. 56–59](gallery-product-and-food.md).

## Copyable prompt

```text
为“{{PRODUCT}}”制作一张产品研发概念拆解板，横向构图，比例 {{ASPECT_RATIO}}。
灵感来源：“{{INSPIRATION}}”。设计意图：“{{DESIGN_INTENT}}”。
材料、结构与已确认规格：{{MATERIALS_AND_FACTS}}。

画面分区：
- 中央放最大的成品概念渲染，清楚展示形态、比例和表面材质。
- 左侧展示灵感观察、轮廓提取和三步形态演化，让各阶段能追溯至同一产品。
- 下方展示使用姿态或人体工学示意，只标注给定的尺寸和角度。
- 右侧展示结构分层或爆炸视图，用对齐关系和细线解释部件如何组合。
- 底部排列材料、表面处理、配色和已确认规格，保持短标签。

使用工业设计提案板的视觉语言：白色或浅灰背景、细线技术图解、克制的色彩、真实材质与清晰阴影。各视图保持同一外形、部件、配色和结构逻辑。
同时呈现分析、演化、使用、结构和材料。避免只给成品广告、随机拼接零件、互相矛盾的视图、长段文字和未提供的参数。对未验证的部分明确标注“概念示意”，不暗示完成工程验证。
```

## Pitfalls and execution

- An exploded view must correspond to the hero object's visible form; inspiration alone does not establish a working mechanism.
- Keep proposed dimensions distinct from verified specifications. Do not claim manufacturability or ergonomic validation from the image.
- For authorized generation, use the existing CLI with `--size landscape --quality high`. For a supplied product image, use a local `-i` reference and state the geometry/material invariants. Inspect agreement between views.

## Attribution

Adapted from freestylefly's [product development template](https://github.com/freestylefly/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/templates.md#tpl-other) and [case 370](https://github.com/freestylefly/awesome-gpt-image-2/blob/b477278bb2a36d4c59655eb0daa4ce48e8dbc4c4/docs/gallery-part-2.md#case-370), attributed there to [@ShamsAmin56](https://x.com/ShamsAmin56/status/2050281206139461780). This is an adapted template, not an original gallery image. See [source and license notes](template-sources.md).
