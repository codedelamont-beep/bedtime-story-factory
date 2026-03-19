---
name: story-character-bible
description: "Create and maintain a character bible with anchor images for visual consistency across all illustrations in a story or series. Use before story-illustrate-generate. Use when user says 'character bible', 'character design', 'character sheet'."
argument-hint: [story-file-or-character-name]
---

# Character Bible — Visual Consistency System

Create character bible for: **$ARGUMENTS**

> This skill creates the foundation for consistent illustrations. It must run BEFORE `story-illustrate-generate`.

## Constants

- OUTPUT_DIR = "characters/"
- ANCHOR_IMAGES = 3 (minimum per character)
- IMAGE_TOOL = "dall-e-3" (or "midjourney", "neolemon")

## Workflow

### Phase 1: Character Extraction

Read the story file and extract all named characters:

```markdown
## Characters Found in "[Story Title]"

| Character | Role | Visual Description | Appearances |
|-----------|------|-------------------|-------------|
| Little Fox | Protagonist | small red fox kit with white-tipped tail | 14 spreads |
| Owl | Helper | elderly grey owl with tiny round spectacles | 5 spreads |
| Moon | Ambient | large pale yellow moon with a gentle face | 8 spreads |
```

### Phase 2: Character Design Document

For EACH character, create a detailed design doc:

```markdown
## Character Design: [Name]

### Identity
- **Species/Type**: small red fox kit
- **Age appearance**: young child equivalent (big eyes, short limbs)
- **Size reference**: about the size of a house cat

### Visual Signature (MUST be consistent in EVERY image)
- **Primary color**: warm cinnamon red (#C1440E)
- **Secondary color**: cream white belly and tail tip (#FFF5E1)
- **Eye color**: warm amber (#FFB347)
- **Eye shape**: large, round, slightly upturned at corners
- **Distinguishing feature**: white-tipped tail that curls when scared
- **Proportions**: head is 1/3 of body (picture book style — big head, small body)

### Style Lock Prompt Fragment
This EXACT text must appear in every generation prompt for this character:
```
a small red fox kit with big round amber eyes, cream white belly,
white-tipped tail, head proportionally large, children's picture book style,
watercolor illustration with soft edges
```

### Expression Sheet (5 Required Expressions)
Generate prompts for:
1. **Neutral/happy** — default expression, slight smile
2. **Curious** — head tilt, ears forward, one paw raised
3. **Scared** — tail curled around legs, ears flat, big eyes
4. **Joyful** — bouncing, tail up, open-mouth smile
5. **Sleepy** — half-closed eyes, yawn, curled up position

### Pose Sheet (5 Required Poses)
1. **Standing** — looking forward (3/4 view)
2. **Walking** — side view, one paw lifted
3. **Sitting** — looking up
4. **Curled up** — sleeping position
5. **With other character** — next to [Owl] for scale reference

### Color Palette
```
Primary:    #C1440E (cinnamon red)
Secondary:  #FFF5E1 (cream white)
Eyes:       #FFB347 (warm amber)
Nose:       #5D4E37 (soft brown)
Accents:    #8B4513 (saddle brown for details)
```

### DO NOT Include
- Sharp claws or teeth
- Realistic fur texture (keep stylized)
- Scary or aggressive poses
- Dark shadows under eyes
```

### Phase 3: Anchor Image Generation

Generate 3 anchor images per character using the Style Lock Prompt:

```markdown
## Anchor Image Prompts

### Anchor 1: Character Reference Sheet
"[Style Lock Fragment], character reference sheet showing front view,
side view, and 3/4 view on white background, soft watercolor,
children's book illustration, high detail, no text" --ar 16:9

### Anchor 2: Emotional Range
"[Style Lock Fragment], showing 4 expressions on white background:
happy, curious, scared, sleepy, children's book illustration,
expression sheet, soft watercolor" --ar 16:9

### Anchor 3: In-Scene Context
"[Style Lock Fragment], sitting in a moonlit forest clearing,
warm lighting, cozy atmosphere, children's book illustration,
soft watercolor, gentle mood" --ar 1:1
```

**Generation Instructions:**
1. Generate Anchor 1 first — this becomes the "gold master"
2. Use Anchor 1 as image reference for Anchors 2-3 (character consistency)
3. If using DALL-E 3: describe character in FULL in every prompt (no shortcuts)
4. If using Midjourney v6+: use `--cref [anchor_url]` for character reference
5. If using Neolemon: upload anchor as reference image

### Phase 4: Multi-Character Relationships

When a story has 2+ characters, generate:

```markdown
## Character Interaction: Fox + Owl

### Scale Reference
"[Fox Style Lock] standing next to [Owl Style Lock], size comparison,
Fox is roughly 1/3 the height of Owl when Owl is perched,
white background, children's book illustration" --ar 16:9

### Together Poses
1. Owl perched on branch above Fox (most common)
2. Fox looking up at Owl (conversation pose)
3. Walking side by side
4. Fox sleeping, Owl watching over
```

### Phase 5: World Design (Settings)

```markdown
## World Design: "[Story Title]"

### Setting Palette
| Setting | Time | Colors | Key Elements | Mood |
|---------|------|--------|-------------|------|
| Forest clearing | Night | Deep blue, silver | Tall trees, moon, fireflies | Mysterious |
| Fox's den | Night | Warm orange, brown | Cozy burrow, moss, roots | Safe |
| Owl's tree | Night | Purple, gold | Ancient oak, tiny window, books | Wise |

### Visual Mood Progression
- Spreads 1-4: Cool blues, distant moonlight → uncertainty
- Spreads 5-8: Warmer tones creeping in → hope
- Spreads 9-12: Warm golden → comfort, friendship
- Spreads 13-14: Soft amber glow → sleep, safety
```

### Output: characters/[story-slug]/

```
characters/[story-slug]/
├── CHARACTER_BIBLE.md          ← Full document
├── fox/
│   ├── design.md               ← Fox's design document
│   ├── style-lock.txt          ← Copy-paste prompt fragment
│   ├── anchor-reference.txt    ← Anchor image prompts
│   └── expressions.txt         ← Expression sheet prompts
├── owl/
│   ├── design.md
│   ├── style-lock.txt
│   └── anchor-reference.txt
├── interactions/
│   └── fox-owl-scale.txt       ← Multi-character prompts
└── world/
    └── settings.md             ← Setting palette & mood progression
```

## Key Rules

- **Style Lock is sacred**: The exact same prompt fragment must appear in EVERY image generation
- **Anchor images first**: Never generate scene illustrations without anchor images
- **Color codes matter**: Use exact hex colors, not "red" or "blue"
- **Large file handling**: If Write fails, use Bash fallback
- **Series persistence**: Character bibles persist across stories in a series
