---
name: story-illustrate
description: "Generate actual illustrations for each spread using anchor images for character consistency. Produces print-ready images (300dpi, correct aspect ratio) with style-locked prompts. Requires character bible from /story-character-bible. Use when user says 'illustrate', 'generate images', 'create illustrations'."
argument-hint: [story-file-path]
---

# Story Illustration — Full Image Generation Pipeline

Generate illustrations for: **$ARGUMENTS**

> **PREREQUISITE:** Run `/story-character-bible` first. This skill requires anchor images and style-lock prompts from `characters/[slug]/`.

## Constants

- STYLE = "watercolor children's book illustration"
- SPREADS = 14 (matching story structure)
- COVER = true
- ASPECT_RATIO_INTERIOR = "1:1" (square for 8.5x8.5)
- ASPECT_RATIO_COVER = "2:3" (tall for front cover)
- DPI = 300 (print-ready)
- MIN_RESOLUTION = "2048x2048" (interior), "2048x3072" (cover)
- IMAGE_TOOL = "flux" (recommended) or "dall-e-3", "midjourney", "ideogram", "neolemon"

## Model Selection Guide

Choose the right model for the job:

| Model | Best For | Character Consistency | Speed | Cost |
|-------|----------|----------------------|-------|------|
| **FLUX 1.1 Pro** ⭐ | Watercolor/painterly, character consistency | ⭐⭐⭐⭐⭐ (multi-ref conditioning) | 4.5s/image | ~$0.04/img |
| **Ideogram** | Pages with text/signs/labels in scene | ⭐⭐⭐⭐ | 8s/image | ~$0.05/img |
| **DALL-E 3** | Quick prototyping, prompt adherence | ⭐⭐⭐ | 15s/image | ~$0.04/img |
| **Midjourney v6** | Artistic quality, stylized looks | ⭐⭐⭐⭐ (--cref flag) | 30s/image | ~$0.01/img |
| **Neolemon** | End-to-end with action editor | ⭐⭐⭐⭐⭐ (built-in) | varies | $30-60/book |

### Model-Specific Instructions

#### FLUX 1.1 Pro (Recommended)
```
API: https://api.bfl.ml/v1/flux-pro-1.1
Character consistency: Use multi-reference conditioning
  → Upload 2-3 anchor images as "reference_images"
  → Set "reference_strength": 0.75 (balance consistency vs creativity)
Prompt suffix: "children's picture book illustration, soft watercolor edges"
Output: 2048×2048 native (no upscaling needed)
Important: FLUX respects hex color codes in prompts
```

#### Ideogram
```
API: https://api.ideogram.ai/generate
Best use case: When illustration contains readable text (signs, labels, book spines)
Text accuracy: 90%+ (far better than any other model)
Prompt suffix: "children's book illustration, clean edges"
Use for: Title page, cover (where title text appears in scene), any scene with signs
```

#### DALL-E 3 (via OpenAI API)
```
API: https://api.openai.com/v1/images/generations
model: "dall-e-3"
quality: "hd"
Character consistency: NO native support → must describe character fully in every prompt
Prompt style: Be extremely verbose with character description (DALL-E 3 follows instructions well)
Limitation: Max 1024×1792 native → requires upscaling for 300dpi print
```

#### Midjourney v6+ (via API or Discord)
```
Character consistency: --cref [anchor_image_url] --cw 100
Style lock: --sref [style_reference_url] --sw 100
Prompt suffix: --ar 1:1 --q 2 --s 750
Important: Keep prompts under 60 words (Midjourney works better with shorter prompts)
```

## Workflow

### Phase 1: Load Character Bible

Read from `characters/[slug]/`:
1. Load all `style-lock.txt` files — these go in EVERY prompt
2. Load `world/settings.md` — color palette per spread
3. Load `interactions/` — multi-character scale reference

### Phase 2: Spread-by-Spread Generation

For each `<!-- SPREAD N -->` marker in the story:

#### Step 1: Scene Analysis
```markdown
- Spread: [N]
- Story text: "[excerpt]"
- Characters present: [list]
- Action: [what's happening]
- Setting: [where]
- Time/Lighting: [from mood progression]
- Emotion: [what the illustration should convey]
- Composition: [foreground/mid/background elements]
```

#### Step 2: Prompt Construction

**Formula (every prompt follows this exactly):**
```
[Scene description], [Character Style Lock Fragment(s)],
[setting from world design], [mood lighting from progression],
[color palette hex values from bible], children's picture book,
watercolor illustration, soft rounded edges, warm palette,
no text, no typography, no words, no letters,
--ar [ratio] --quality 2
```

**Rules:**
- Include the FULL Style Lock Fragment for every character in the scene
- Never abbreviate character description ("the fox" → use full description)
- Include exact color hex values for consistency
- Always include "no text, no typography" (AI loves adding random text)
- Reference the mood progression (spreads 1-4: cool, 5-8: warming, 9-14: warm/golden)

#### Step 3: Generation & QC

For each image generated:

```markdown
## QC Checklist — Spread [N]

- [ ] Character face matches anchor image
- [ ] Character outfit/colors correct
- [ ] Character proportions correct (head size, limb length)
- [ ] No extra fingers or malformed hands
- [ ] No text or typography in image
- [ ] Color palette matches world design
- [ ] Mood/lighting matches progression for this spread
- [ ] Scene matches story text
- [ ] Style consistent with previous spreads
- [ ] Resolution ≥ 2048px on shortest side
```

**If QC fails:**
1. Regenerate with adjusted prompt (add "NOT [problem]")
2. Maximum 3 regeneration attempts per spread
3. Log failures in `ILLUSTRATION_QC.md`

### Phase 3: Style Consistency Check

After all spreads are generated, compare them side-by-side:

```markdown
## Style Consistency Audit

| Check | Status |
|-------|--------|
| Character proportions consistent across all spreads | ✅/❌ |
| Color palette consistent (no random blue shifts) | ✅/❌ |
| Art style consistent (watercolor throughout, no photorealism) | ✅/❌ |
| Lighting follows mood progression (cool→warm→golden) | ✅/❌ |
| No anachronisms (modern objects in fantasy setting) | ✅/❌ |
| Character aging/regression (should be same age throughout) | ✅/❌ |
```

Regenerate any spreads that fail consistency check.

### Phase 4: Cover Generation

```
"[Title]" children's picture book cover,
[Main character Style Lock Fragment] in [key iconic scene],
[art style], warm inviting colors, bedtime theme,
professional book cover composition, centered character,
[color palette from bible], no text, no typography,
--ar 2:3 --quality 2
```

Generate 3 cover variants. Select the one with best character likeness.

### Phase 5: Post-Processing Requirements

For each final image, document required post-processing:

```markdown
## Post-Processing: Spread [N]

- [ ] Upscale to 300dpi at 8.5" × 8.5" (2550 × 2550px minimum)
- [ ] Color profile: sRGB (for digital) / CMYK (for print)
- [ ] Add 0.125" bleed on all sides (for KDP print)
- [ ] No compression artifacts visible at 100% zoom
- [ ] File format: PNG (lossless) or TIFF
```

### Phase 6: Character Sheet Reference for Series

Save a master reference for reuse in future stories:

```markdown
## Series Reference: [Character Name]

### Prompt That Produced Best Results
"[exact prompt that generated the best anchor image]"

### Model & Settings Used
- Model: [dall-e-3 / midjourney v6 / etc.]
- Settings: [quality, style, seed if applicable]

### Notes for Future Books
- [what worked, what to avoid]
```

### Output: illustrations/[title-slug]/

```
illustrations/[title-slug]/
├── CHARACTER_BIBLE_REF.md      ← Link to characters/[slug]/
├── spreads/
│   ├── spread-01.png           ← Actual generated images
│   ├── spread-02.png
│   ├── ...
│   ├── spread-14.png
│   └── cover-front.png
├── prompts/
│   ├── spread-01.txt           ← Exact prompts used
│   ├── spread-02.txt
│   ├── ...
│   └── cover.txt
├── qc/
│   └── ILLUSTRATION_QC.md      ← QC results per spread
├── style-guide.md              ← Visual style reference
└── ILLUSTRATION_REPORT.md      ← Summary of all images
```

### ILLUSTRATION_REPORT.md Format

```markdown
# Illustration Report: "[Title]"

**Date**: [today]
**Tool**: [dall-e-3 / midjourney / etc.]
**Total spreads**: 14 + 1 cover
**Regenerations needed**: [N]
**Style consistency score**: [X/10]

| Spread | Description | QC Pass | Regens | Final Prompt |
|--------|-------------|---------|--------|--------------|
| 1 | Fox in moonlit clearing | ✅ | 0 | [truncated] |
| 2 | Fox looking around, ears up | ✅ | 1 | [truncated] |
| ... | ... | ... | ... | ... |
| Cover | Fox and Owl under stars | ✅ | 2 | [truncated] |

## Issues Found
- Spread 4: had to regenerate due to hand malformation
- Spread 9: color shifted too blue, re-prompted with hex codes

## Series Reuse
Character anchors saved to `characters/[slug]/` for future books.
```

## Key Rules

- **Character bible is prerequisite** — never generate without anchor images
- **Style Lock in every prompt** — the full character description, every time
- **No text in images** — always include "no text, no typography" in prompt
- **QC every image** — check face, proportions, hands, colors before accepting
- **300dpi minimum** — anything less is not print-ready
- **Save prompts** — exact prompt stored next to each image for reproducibility
- **Large file handling**: If Write fails, use Bash fallback
