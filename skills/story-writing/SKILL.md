---
name: story-writing
description: "Full story generation pipeline. Takes a concept and produces a complete, polished bedtime story with proper structure, vocabulary, and emotional arc. Use when user says 'write story', 'generate story', 'create bedtime story'."
argument-hint: [concept-or-title]
---

# Story Writing — Full Story Generation

Write a complete bedtime story for: **$ARGUMENTS**

## Constants

- WORD_COUNT = 800
- TARGET_AGE = "3-6"
- READING_LEVEL = "Flesch-Kincaid Grade 1-2"
- REVIEWER_MODEL = "gpt-4o"

## Workflow

### Phase 1: Story Outline

Read concept from `CONCEPT_REPORT.md` or user input. Create outline:

```markdown
## Story Outline: "[Title]"

### Opening (100 words)
- Setting: [where/when]
- Character intro: [who, what they're doing]
- Mood: [warm, cozy, curious]

### Rising Action (200 words)
- Inciting incident: [what changes]
- Character's goal: [what they want]
- First attempt: [what they try]

### Middle (200 words)
- Obstacle: [what goes wrong]
- Help arrives: [friend, mentor, realization]
- Learning moment: [the moral starts forming]

### Resolution (200 words)
- Solution: [how they solve it]
- Moral: [lesson learned]
- Emotional payoff: [warm feeling]

### Wind-Down (100 words)
- Return to safety: [back home, tucked in]
- Sleepy transition: [yawning, stars, quiet]
- Final line: [gentle closing]
```

### Phase 2: First Draft

Write the full story following the outline:

**Writing Rules:**
- Sentences: max 12 words for ages 3-4, max 15 for ages 5-6
- Paragraphs: 2-3 sentences max
- Vocabulary: concrete nouns, simple verbs, sensory words
- Repetition: use rhythmic repetition (kids love it)
- Dialogue: short, expressive, with action tags
- Senses: describe what characters see, hear, feel, smell
- Pacing: slow down in the final quarter
- Last 3 sentences: progressively shorter and quieter

**Banned elements:**
- Violence, death, injury
- Scary monsters (friendly ones OK)
- Abandonment themes
- Loud/exciting endings
- Complex vocabulary without context clues
- Passive voice

### Phase 3: Quality Checks

Run automated checks on the draft:

1. **Word count**: Within ±10% of WORD_COUNT
2. **Readability**: Calculate Flesch-Kincaid grade level
3. **Vocabulary audit**: Flag words above age level
4. **Emotional arc check**: Does it wind down to sleepy?
5. **Moral clarity**: Is the lesson clear but not preachy?
6. **Repetition check**: Are patterns intentional and musical?
7. **Page-turn moments**: Are there natural illustration breaks?

### Phase 4: Polish

1. Replace flagged vocabulary with age-appropriate synonyms
2. Smooth transitions between sections
3. Ensure the ending is genuinely sleepy
4. Add subtle rhyme or rhythm where natural
5. Verify character consistency

### Output: stories/[title-slug].md

```markdown
---
title: "[Title]"
author: "AI Story Factory"
target_age: "3-6"
word_count: [actual count]
readability_score: [Flesch-Kincaid grade]
moral: "[lesson]"
characters: ["name1", "name2"]
themes: ["theme1", "theme2"]
illustration_scenes: 8
date: [today]
---

# [Title]

[Full story text with scene break markers]

<!-- SCENE 1: [description for illustrator] -->
[Story opening...]

<!-- SCENE 2: [description for illustrator] -->
[Story continues...]

...

<!-- SCENE 8: [soft, sleepy closing scene] -->
[Gentle ending...]

The End. 🌙
```

## Key Rules

- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask the user — just do it silently.
