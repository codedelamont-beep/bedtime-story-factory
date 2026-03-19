---
name: story-concept
description: "Generate and rank story concepts with craft feasibility scoring. Creates 8-12 unique concepts per niche with hooks, characters, moral lessons, AND craft potential (refrain, sound design, rhythm, character distinctiveness). References CRAFT_GUIDE.md. Use when user says 'generate concepts', 'brainstorm stories', 'create story ideas'."
argument-hint: [niche-or-theme]
---

# Story Concept Generator

Generate publishable story concepts for: **$ARGUMENTS**

## Constants

- CONCEPTS_PER_NICHE = 10
- TARGET_AGE = "3-6"
- REVIEWER_MODEL = "gpt-4o"

## Workflow

### Phase 1: Read Research & Craft Guide

1. Check for `RESEARCH_REPORT.md` — use discovered niches and gaps
2. Read `references/CRAFT_GUIDE.md` — understand craft requirements that concepts must support
3. If no research exists, ask user for theme/niche direction
4. Identify the target niche characteristics

### Phase 2: Concept Generation (with external LLM)

Use cross-model brainstorming for diversity:

```
Prompt to REVIEWER_MODEL:
  You are a children's book author specializing in bedtime stories for ages [TARGET_AGE].
  You understand that great bedtime stories need: rhythm, refrains, sound design,
  show-don't-tell, page-turn hooks, and a distinctive character.

  Theme/Niche: [from research or user input]
  Market gaps: [from research]

  Generate 10 unique bedtime story concepts. For each:
  1. Title (catchy, memorable, max 8 words)
  2. One-sentence hook (the premise that makes a parent pick it up)
  3. Main character (name, species/type, key trait — describable in 5 words)
  4. Core conflict (what goes wrong / what needs solving)
  5. Moral/lesson (what the child learns — shown, not told)
  6. Emotional arc (how the child should FEEL: excited→curious→warm→sleepy)
  7. Bedtime factor (how does it wind down to sleep?)
  8. Series potential (can this character have more adventures?)
  9. Key scenes (3-5 visual moments an illustrator could paint immediately)

  CRAFT FEASIBILITY (required for each concept):
  10. Refrain idea — suggest a repeating phrase that could anchor the story
      Example: "Tiptoe, tiptoe, through the quiet..."
  11. Sound design opportunity — What sounds exist in this world?
      Example: forest = rustling, hooting, creaking, crickets chirping
  12. Rhythm pattern — Does the premise support trochaic, cumulative, or rule-of-three?
  13. Character voice — How does this character speak differently from others?
      Example: Owl always asks questions; Fox narrates with her nose
  14. Golden line potential — Imagine one line from this story that a parent would
      whisper as the child falls asleep.
      Example: "The stars aren't far. They're just your friends turned into light."

  Rules:
  - Every story must end peacefully (this is BEDTIME)
  - No scary elements, violence, or anxiety-inducing plots
  - Characters should be relatable to [TARGET_AGE] children
  - Include diverse characters and settings
  - Vocabulary must match age group
  - Concepts that don't support at least 3 craft techniques score lower
```

### Phase 3: Craft Feasibility Filter

For each concept, evaluate on TWO dimensions:

**Market Viability** (same as before):
1. **Originality**: Does this feel too similar to an existing popular book?
2. **Illustration potential**: Can each scene be clearly visualized?
3. **Parent appeal**: Would a parent choose to read this aloud?
4. **Repeat readability**: Will kids want to hear this again and again?
5. **Bedtime suitability**: Does it actually wind down, not ramp up?

**Craft Potential** (NEW — from CRAFT_GUIDE.md):
6. **Refrain feasibility**: Can a natural refrain emerge from this premise? (1-10)
7. **Sound design richness**: Does the setting offer rich sounds? (1-10)
8. **Rhythm compatibility**: Does the concept suit read-aloud rhythm patterns? (1-10)
9. **Character distinctiveness**: Is the character memorable in 5 words? (1-10)
10. **Golden line potential**: Could this concept produce a whisper-worthy line? (1-10)

```
Market Score = avg(criteria 1-5)
Craft Score = avg(criteria 6-10)
Overall = (Market × 0.4) + (Craft × 0.6)   ← Craft weighted higher!
```

**Elimination rules:**
- Market Score < 6/10 → ELIMINATE (won't sell)
- Craft Score < 6/10 → ELIMINATE (can't be executed well)
- No viable refrain idea → WARN (can proceed but harder)
- Character not describable in 5 words → REWRITE character concept

### Phase 4: Ranking

Rank surviving concepts by:
1. **Craft Score** (highest first — craft is king)
2. **Market fit** (matches identified gaps)
3. **Series potential** (more books = more revenue)
4. **Production ease** (simpler illustration = faster output)

### Output: CONCEPT_REPORT.md

```markdown
# Story Concept Report

**Theme**: [niche/theme]
**Date**: [today]
**Concepts generated**: X → Y survived filtering

## Top Concepts (ranked by craft potential)

### 1. "[Title]" — Craft: X/10 | Market: X/10 | Overall: X/10
- **Hook**: [one sentence]
- **Character**: [name, type, trait] — **5-word test**: "[five words]"
- **Conflict**: [what goes wrong]
- **Moral**: [lesson — shown not told]
- **Emotional arc**: [feeling progression]
- **Bedtime factor**: [how it winds down]
- **Series potential**: YES/NO — [why]
- **Key scenes**: [3-5 visual moments]
- **Market fit**: [why this fills a gap]

#### Craft Blueprint
- **Refrain**: "[suggested repeating phrase]"
- **Sound design**: [sounds in this world]
- **Rhythm**: [trochaic / cumulative / rule-of-three / etc.]
- **Character voice**: [how they speak/think differently]
- **Golden line**: "[candidate golden line]"

### 2. "[Title]" — Craft: X/10 | Market: X/10 | Overall: X/10
[same format]

## Craft Feasibility Matrix

| Concept | Refrain | Sound | Rhythm | Character | Gold Line | Craft Avg |
|---------|---------|-------|--------|-----------|-----------|-----------|
| "[Title 1]" | 9 | 8 | 8 | 9 | 8 | 8.4 |
| "[Title 2]" | 7 | 9 | 7 | 8 | 7 | 7.6 |
| "[Title 3]" | 5 | 6 | 8 | 7 | 6 | 6.4 |

## Eliminated Concepts
| Concept | Market | Craft | Reason |
|---------|--------|-------|--------|
| ... | 7 | 4 | Craft score too low — no refrain possible |
| ... | 3 | 8 | Market score too low — oversaturated niche |

## Recommended Production Order
1. Start with "[Title]" — highest craft score + strong market fit
2. Then "[Title]" — best series potential with craft foundation
```

## Key Rules

- **Craft > Market**: A high-craft concept in a medium market beats a low-craft concept in a hot market. Craft is what makes the book a bestseller; market is what gets it discovered.
- **Refrain is essential**: Concepts without a natural refrain need a WARNING — they're harder to write well
- **5-word character test**: If you can't describe the character in 5 memorable words, redesign them
- **Golden line before writing**: Having a golden line candidate at concept stage saves hours during writing
- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask the user — just do it silently.
