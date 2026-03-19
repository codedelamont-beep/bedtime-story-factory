---
name: story-review
description: "Autonomous multi-round review loop for bedtime stories. Cross-model adversarial review checking age-appropriateness, emotional arc, vocabulary, and readability. Use when user says 'review story', 'quality check', 'auto review'."
argument-hint: [story-file-path]
---

# Story Review — Autonomous Quality Loop

Review and improve: **$ARGUMENTS**

## Constants

- MAX_ROUNDS = 3
- POSITIVE_THRESHOLD = 8/10
- REVIEW_DOC = "STORY_REVIEW.md"
- REVIEWER_MODEL = "gpt-4o"
- HUMAN_CHECKPOINT = false

## State Persistence

Persist state to `REVIEW_STATE.json` after each round for crash recovery:

```json
{
  "round": 2,
  "story_file": "stories/brave-dragon.md",
  "status": "in_progress",
  "last_score": 7.0,
  "last_verdict": "almost",
  "timestamp": "2026-03-19T22:00:00"
}
```

## Review Loop

### Phase A: Send to Reviewer

```
Prompt to REVIEWER_MODEL:
  You are a children's book editor specializing in bedtime stories.
  Review this story for ages [TARGET_AGE].

  [Full story text]

  Score 1-10 on each criterion:
  1. Age-appropriateness (vocabulary, concepts, themes)
  2. Emotional arc (does it wind down to sleepy?)
  3. Readability (sentence length, word complexity)
  4. Engagement (would a child ask for this again?)
  5. Moral clarity (lesson present but not preachy?)
  6. Illustration potential (clear visual scenes?)
  7. Parent appeal (would a parent enjoy reading aloud?)
  8. Bedtime suitability (calming, not stimulating?)

  Overall score: X/10
  Verdict: READY / ALMOST / NEEDS WORK
  Specific fixes needed (ranked by impact):
```

### Phase B: Parse & Decide

- Score >= 8 AND verdict "READY" → STOP, story approved
- Score 6-7 AND verdict "ALMOST" → implement fixes, re-review
- Score < 6 → significant rewrite needed

### Phase C: Implement Fixes

For each fix (highest priority first):
1. Vocabulary swaps (replace hard words)
2. Pacing adjustments (slow down ending)
3. Emotional arc fixes (add warm moments)
4. Sentence restructuring (shorten for age)
5. Moral integration (weave, don't lecture)

### Phase D: Document Round

Append to `STORY_REVIEW.md`:

```markdown
## Round N — "[Story Title]"

### Scores
| Criterion | Score |
|-----------|-------|
| Age-appropriateness | X/10 |
| Emotional arc | X/10 |
| ... | ... |
| **Overall** | **X/10** |

### Fixes Applied
- [list of changes]

### Status: continuing / approved
```

### Termination

1. Update `REVIEW_STATE.json` with `"status": "completed"`
2. Write final verdict to `STORY_REVIEW.md`
3. If approved: move story to `output/approved/`
4. If max rounds without approval: list remaining issues

## Key Rules

- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask the user — just do it silently.
