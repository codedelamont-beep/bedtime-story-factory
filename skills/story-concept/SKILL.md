---
name: story-concept
description: "Generate and rank story concepts/premises for children's bedtime stories. Creates 8-12 unique concepts per niche with hooks, characters, and moral lessons. Use when user says 'generate concepts', 'brainstorm stories', 'create story ideas'."
argument-hint: [niche-or-theme]
---

# Story Concept Generator

Generate publishable story concepts for: **$ARGUMENTS**

## Constants

- CONCEPTS_PER_NICHE = 10
- TARGET_AGE = "3-6"
- REVIEWER_MODEL = "gpt-4o"

## Workflow

### Phase 1: Read Research

1. Check for `RESEARCH_REPORT.md` — use discovered niches and gaps
2. If no research exists, ask user for theme/niche direction
3. Identify the target niche characteristics

### Phase 2: Concept Generation (with external LLM)

Use cross-model brainstorming for diversity:

```
Prompt to REVIEWER_MODEL:
  You are a children's book author specializing in bedtime stories for ages [TARGET_AGE].

  Theme/Niche: [from research or user input]
  Market gaps: [from research]

  Generate 10 unique bedtime story concepts. For each:
  1. Title (catchy, memorable, max 8 words)
  2. One-sentence hook (the premise that makes a parent pick it up)
  3. Main character (name, species/type, key trait)
  4. Core conflict (what goes wrong / what needs solving)
  5. Moral/lesson (what the child learns)
  6. Emotional arc (how the child should FEEL: excited→curious→warm→sleepy)
  7. Bedtime factor (how does it wind down to sleep?)
  8. Series potential (can this character have more adventures?)
  9. Illustration notes (key visual scenes, 3-5 per story)

  Rules:
  - Every story must end peacefully (this is BEDTIME)
  - No scary elements, violence, or anxiety-inducing plots
  - Characters should be relatable to [TARGET_AGE] children
  - Include diverse characters and settings
  - Vocabulary must match age group
  - Rhyming is optional but note if the concept suits it
```

### Phase 3: First-Pass Filter

For each concept, evaluate:

1. **Originality**: Does this feel too similar to an existing popular book?
2. **Illustration potential**: Can each scene be clearly visualized?
3. **Parent appeal**: Would a parent choose to read this aloud?
4. **Repeat readability**: Will kids want to hear this again and again?
5. **Bedtime suitability**: Does it actually wind down, not ramp up?

Eliminate concepts scoring < 6/10 on any criterion.

### Phase 4: Ranking

Rank surviving concepts by:
- Market fit (matches identified gaps)
- Uniqueness (stands out from competition)
- Series potential (more books = more revenue)
- Production ease (simpler illustration = faster output)

### Output: CONCEPT_REPORT.md

```markdown
# Story Concept Report

**Theme**: [niche/theme]
**Date**: [today]
**Concepts generated**: X → Y survived filtering

## Top Concepts (ranked)

### 1. "[Title]"
- **Hook**: [one sentence]
- **Character**: [name, type, trait]
- **Conflict**: [what goes wrong]
- **Moral**: [lesson]
- **Emotional arc**: [feeling progression]
- **Bedtime factor**: [how it winds down]
- **Series potential**: YES/NO — [why]
- **Key scenes**: [3-5 visual moments]
- **Market fit**: [why this fills a gap]

## Eliminated Concepts
| Concept | Reason |
|---------|--------|
| ... | Too similar to [existing book] |
| ... | Not suitable for bedtime (too exciting) |

## Recommended Production Order
1. Start with "[Title]" — strongest market fit
2. Then "[Title]" — best series potential
```

## Key Rules

- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask the user — just do it silently.
