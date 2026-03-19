---
name: story-writing
description: "Full story generation pipeline. Takes a concept and produces a craft-quality bedtime story using bestseller techniques from CRAFT_GUIDE.md — rhythm, sound design, refrain, show-don't-tell, page-turn architecture. Use when user says 'write story', 'generate story', 'create bedtime story'."
argument-hint: [concept-or-title]
---

# Story Writing — Bestseller-Quality Story Generation

Write a complete bedtime story for: **$ARGUMENTS**

> **MANDATORY: Before writing any prose, read `references/CRAFT_GUIDE.md`. Every technique in that guide must be applied.**

## Constants

- WORD_COUNT = 800
- TARGET_AGE = "3-6"
- SPREAD_COUNT = 14 (standard 32-page picture book)
- READING_LEVEL = "Flesch-Kincaid Grade 1-2"

## Workflow

### Phase 1: Character Design

Before outlining, design a memorable character:

```markdown
## Character: [Name]

- **5-word hook**: [e.g., "tiny dragon who can't fly"]
- **Visual quirk**: [what makes them instantly recognizable in illustration]
- **Voice**: [how they speak — e.g., "whispers everything, uses big words wrong"]
- **Contradiction**: [brave but scared of butterflies, strong but needs help opening jars]
- **Catchphrase/Pattern**: [optional repeating phrase — e.g., "Oh my whiskers!"]
```

#### The 5-Word Test
If a 4-year-old can't remember this character after one reading, redesign.

### Phase 2: Spread-by-Spread Outline (14 Spreads)

Map the story to picture book spreads. Each spread = one illustration + text.

```markdown
## Story Outline: "[Title]" — 14 Spreads

### Spread 1: OPENING
- Visual: [what the illustrator draws]
- Text: [1-3 sentences establishing character + world]
- Page-turn hook: [what makes you want to turn the page]

### Spread 2: WANT
- Visual: [character's desire shown visually]
- Text: [show what character wants through action, NOT narration]
- Refrain placement: [first appearance of refrain? yes/no]

### Spread 3-4: FIRST ATTEMPT
- Visual: [...] Action: [...] Result: [almost works, but...]
- End of Spread 4 on a "but..." to create page-turn anticipation

### Spread 5: REACTION
- Visual: [physical emotional response — tail curls, ears droop]
- Text: [show emotion through body, never "she felt sad"]

### Spread 6-7: TRY AGAIN / HELP ARRIVES
- New ally or realization — NOT a lecture
- Refrain appears again (same words, different emotional context)

### Spread 8: MIDPOINT SHIFT
- Perspective change, new information, alliance forms
- Visual: [distinct change in setting/color/lighting]

### Spread 9-10: NEW APPROACH + ALMOST THERE
- Building toward climax — pacing gets tighter
- Shortest sentences yet — urgency through brevity

### Spread 11: CLIMAX
- The moment everything changes — SHOW it
- Minimal text (let the illustration carry the weight)
- Refrain appears in its most powerful form

### Spread 12: RESOLUTION
- Warmth after the storm — not excitement, comfort
- The "golden line" should live here or in Spread 13

### Spread 13: WIND-DOWN
- Returning to safety — back home, parent's arms, familiar place
- Longer vowels, softer consonants, slower rhythm

### Spread 14: GOODNIGHT
- The gentlest spread — whisper-level text
- Sentences descend: 8 words → 5 words → 2-3 words
- Final line passes the "whisper test" (sounds perfect as a whisper)
```

### Phase 3: First Draft — Craft-Quality Writing

Write the full story applying ALL craft techniques:

**Mandatory Techniques (from CRAFT_GUIDE.md):**

1. **Rhythm**: Write in trochaic rhythm for bedtime (STRONG-weak pattern)
2. **Refrain**: Include a repeating phrase 3-5 times across the story
3. **Sound Design**:
   - Minimum 5 onomatopoeia (swish, plop, hush, crunch, etc.)
   - Minimum 3 alliterative phrases ("sleepy stars sparkled softly")
   - Minimum 8 mouth-feel words (cozy, snuggle, whisper, tumble, wobble)
4. **Show Don't Tell**: Zero "she felt [emotion]" sentences — all physical/observable
5. **Page-Turn Architecture**: Every spread ends with anticipation
6. **Never state the moral** — let the reader discover it through the story
7. **Humor layer**: At least 2 child-funny moments AND 1 parent-funny moment
8. **Wind-Down**: Final 3 spreads descend in energy (shorter sentences, softer words)
9. **Golden Line**: One line good enough to be whispered as the child falls asleep

**Writing Rules:**
- Sentences: max 12 words for ages 3-4, max 15 for ages 5-6
- Paragraphs: 2-3 sentences max
- Vocabulary: concrete nouns, simple verbs, sensory words
- Dialogue: short, expressive, with action tags (never "said loudly" — use "whispered" or show)
- Final sentence: must sound perfect as a whisper

**Banned elements:**
- Violence, death, injury
- Scary monsters (friendly/silly ones OK)
- Abandonment themes
- Loud/exciting endings
- Complex vocabulary without intuitive context
- Passive voice
- "She felt [emotion]" (use show-don't-tell instead)
- Explicitly stating the moral ("The lesson is...")
- "And then..." sentence starters (lazy transitions)

### Phase 4: Read-Aloud Verification Pass

After the draft is complete, re-read every sentence and check:

1. **Stumble check**: Does any sentence trip the tongue? → Rewrite
2. **Rhythm check**: Is the stress pattern consistent? → Fix broken beats
3. **Sound check**: Are there enough "delicious" words? → Add sensory language
4. **Refrain check**: Does the refrain appear 3+ times? → Add placements
5. **Show-don't-tell audit**: Any "felt" or "was [emotion]"? → Convert to physical
6. **Golden line test**: Can you extract ONE whisper-worthy line? → If not, write one
7. **Parent endurance test**: Would you enjoy reading this 50 times? → If not, add wit

### Phase 5: Quality Checklist

Run the full CRAFT_GUIDE.md checklist:

- [ ] Every sentence passes the read-aloud test
- [ ] Story has a refrain (appears 3+ times)
- [ ] 5+ onomatopoeia / sound words
- [ ] 3+ alliterative phrases
- [ ] 8+ mouth-feel/sensory words
- [ ] Zero "she felt [emotion]" sentences
- [ ] Moral is never stated explicitly
- [ ] Character passes the 5-word test
- [ ] Structure maps to 14 spreads with `<!-- SPREAD -->` markers
- [ ] Humor layer exists (child level AND parent level)
- [ ] Final 3 spreads descend in energy
- [ ] Final sentence passes the "whisper test"
- [ ] Has one golden line
- [ ] Word count within ±10% of WORD_COUNT

### Output: stories/[title-slug]_v0_draft.md

**CRITICAL: Always use versioned filename.** The `_v0_draft` suffix is mandatory.

```markdown
---
title: "[Title]"
author: "AI Story Factory"
version: 0
version_label: "draft"
previous_version: null
target_age: "3-6"
word_count: [actual count]
readability_score: [Flesch-Kincaid grade]
spread_count: 14
characters: ["name1", "name2"]
character_hooks: ["tiny dragon who can't fly", "grumpy cloud who rains too much"]
themes: ["theme1", "theme2"]
refrain: "[the repeating phrase]"
golden_line: "[the whisper-worthy line]"
humor_notes: "[child-funny: X, parent-funny: Y]"
sound_word_count: [actual count]
craft_checklist_passed: true
date: [today]
---

# [Title]

<!-- SPREAD 1: [visual description for illustrator] -->
[Story opening with character introduction...]

<!-- SPREAD 2: [visual description] -->
[Character's desire shown through action...]

...

<!-- SPREAD 13: [warm, returning-home visual] -->
[Wind-down text, softer and slower...]

<!-- SPREAD 14: [the sleepiest scene — moonlight, parent's arms, closed eyes] -->
[Descending sentence lengths...]
[Shorter still...]
[Whisper.]

The End. 🌙
```

### Post-Write Checklist

After writing the story file:
1. Verify the file was saved as `stories/{slug}_v0_draft.md`
2. Verify frontmatter includes all craft metadata (refrain, golden_line, sound_word_count)
3. Log to `SCORE_TRACKER.md` with initial self-assessed scores

## Version Convention

```
_v0_draft.md       ← You produce this (first draft)
_v1_reviewed.md    ← /story-review produces this
_v2_improved.md    ← /story-improvement-loop produces this
_v3_final.md       ← Approved for export
```

**NEVER overwrite a previous version file.** Always create the next version.

## Key Rules

- **ALWAYS read `references/CRAFT_GUIDE.md` before writing** — it contains the techniques
- **Large file handling**: If the Write tool fails, retry using Bash (`cat << 'EOF' > file`)
- **Always version**: Output MUST be `_v0_draft.md`. No exceptions.
- **Frontmatter required**: Every story MUST include version + craft metadata.
- **Read aloud**: If you wouldn't enjoy reading it aloud, rewrite it.
