---
name: story-illustrate
description: "Generate Midjourney/AI image prompts for each scene in a story. Creates consistent character descriptions, scene compositions, and style guides. Use when user says 'illustrate', 'generate prompts', 'image prompts'."
argument-hint: [story-file-path]
---

# Story Illustration — AI Image Prompt Generator

Generate illustration prompts for: **$ARGUMENTS**

## Constants

- STYLE = "watercolor children's book illustration"
- ASPECT_RATIO = "1:1"
- SCENES_PER_STORY = 8
- PROMPT_FORMAT = "midjourney" (or "flow", "dalle")

## Workflow

### Phase 1: Character Design Sheet

Create a consistent character description for Midjourney:

```markdown
## Character Sheet: [Character Name]

- Species/Type: [e.g., small red dragon]
- Key features: [e.g., round eyes, tiny wings, green belly]
- Expression style: [e.g., wide-eyed, friendly, soft]
- Color palette: [e.g., warm reds, soft greens]
- Size reference: [e.g., about the size of a cat]
- Clothing/accessories: [e.g., striped scarf]

### Reference prompt:
"[character description], watercolor children's book illustration style,
soft edges, warm colors, white background, character sheet" --ar 1:1
```

### Phase 2: Scene Prompts

For each `<!-- SCENE -->` marker in the story:

1. Read the scene description and surrounding text
2. Identify: setting, characters present, action, mood, time of day
3. Generate a Midjourney-optimized prompt

**Prompt formula:**
```
[scene description], [character] from "[story title]",
[art style], [mood lighting], [color palette],
children's book illustration, soft watercolor,
no text, no typography --ar [ratio] --style raw --quality 2
```

**Rules:**
- Maintain character consistency across all scenes
- Reference the character sheet description in every prompt
- Progressive mood shift: scenes get warmer/softer toward the end
- Final scene should be the sleepiest/coziest
- No scary/dark imagery even if the story has mild tension

### Phase 3: Style Guide

Generate a style guide for visual consistency:

```markdown
## Style Guide: "[Story Title]"

- Art style: Soft watercolor, rounded shapes
- Color palette: [5 hex colors]
- Line weight: Soft, no hard outlines
- Background style: Simple, not busy
- Mood progression: Bright → Warm → Golden → Moonlit
- Typography style: [for cover/title]
```

### Phase 4: Cover Prompt

Generate the book cover prompt:
```
"[Title]" children's book cover, [main character] in [key scene],
[art style], warm inviting colors, bedtime theme,
no text, professional book cover composition --ar 2:3 --quality 2
```

### Output: illustrations/[title-slug]/

```
illustrations/[title-slug]/
├── character-sheet.md
├── style-guide.md
├── prompts/
│   ├── scene-01.txt
│   ├── scene-02.txt  
│   ├── ...
│   ├── scene-08.txt
│   └── cover.txt
└── ILLUSTRATION_REPORT.md
```
