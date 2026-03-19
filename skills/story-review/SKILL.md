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

## State Persistence & Recovery

Persist state to `REVIEW_STATE.json` after each round for crash recovery:

```json
{
  "round": 2,
  "story_file": "stories/brave-dragon_v0_draft.md",
  "status": "in_progress",
  "last_score": 7.0,
  "last_verdict": "almost",
  "conversation_history": [],
  "timestamp": "2026-03-19T22:00:00"
}
```

**On context window reset / startup:**
1. Check if `REVIEW_STATE.json` exists
2. If `status == "in_progress"` AND `timestamp` < 24h:
   - Print: "🔄 Resuming review of [story_file] from Round [N]"
   - Read `STORY_REVIEW.md` for previous round details
   - Continue from next round
3. If `status == "paused_human"`:
   - Print: "⏸ Review paused at Round [N]. Pending fixes: [list]"
   - Present fixes and wait for response
4. If `status == "completed"` or file absent: start fresh
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

### Phase B2: Human Checkpoint

**Skip if `HUMAN_CHECKPOINT = false` (default).** When false, auto-proceed with all fixes.

**When `HUMAN_CHECKPOINT = true`:**

Present the review summary and wait for user response:

```
📋 Review Round [N]: "[Story Title]"

Score: [X.X]/10 — [verdict]
Weakest areas:
1. [criterion]: [X]/10 — [suggested fix]
2. [criterion]: [X]/10 — [suggested fix]
3. [criterion]: [X]/10 — [suggested fix]

Reply with one of:
• "go"           → implement all fixes
• "skip 2"       → skip fix #2, implement the rest
• "skip 1,3"     → skip fixes #1 and #3
• "stop"         → save state, halt review (resume later)
• "custom: ..."  → use your instructions instead of fixes
```

**Response Parsing:**

| Response | Action |
|----------|--------|
| `go` | Implement all suggested fixes, continue to next round |
| `skip N` | Skip fix #N, implement all others |
| `skip N,M` | Skip fixes #N and #M, implement all others |
| `stop` | Save `REVIEW_STATE.json` with current state, halt. Resume with `/story-review "file.md"` |
| `custom: [text]` | Ignore reviewer fixes. Use user's custom instructions as the fix spec |
| (empty / timeout 60s) | If `AUTO_PROCEED = true`: treat as "go". Otherwise: wait. |

**State on stop:**
```json
{
  "status": "paused_human",
  "round": 2,
  "pending_fixes": ["fix1", "fix2", "fix3"],
  "timestamp": "2026-03-19T23:00:00"
}
```

On resume: detect `"status": "paused_human"`, present pending fixes again.

### Phase C: Implement Fixes

For each fix (highest priority first, respecting skip directives):
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
| Readability | X/10 |
| Engagement | X/10 |
| Moral clarity | X/10 |
| Illustration potential | X/10 |
| Parent appeal | X/10 |
| Bedtime suitability | X/10 |
| **Overall** | **X/10** |

### Fixes Applied
- [list of changes]

### Status: continuing / approved
```

### Phase E: Score Progression Tracking

**After every round**, append to `SCORE_TRACKER.md`:

```markdown
## Score Progression: "[Story Title]"

| Round | Time | Age | Arc | Read | Engage | Moral | Illust | Parent | Bedtime | Overall | Δ |
|-------|------|-----|-----|------|--------|-------|--------|--------|---------|---------|---|
| R0 draft | HH:MM | X | X | X | X | X | X | X | X | X.X | — |
| R1 review | HH:MM | X | X | X | X | X | X | X | X | X.X | +X.X |
```

This enables batch analysis: which criteria improve most, what's consistently weak, and where to focus prompts.

### Phase F: Version Output

**CRITICAL:** Do NOT overwrite the input file. Create a NEW versioned file:

- Input: `stories/{slug}_v0_draft.md`
- Output: `stories/{slug}_v1_reviewed.md`

Frontmatter of v1 must include:
```yaml
version: 1
version_label: "reviewed"
previous_version: "stories/{slug}_v0_draft.md"
review_score: X.X
review_rounds: N
```

### Termination

1. Update `REVIEW_STATE.json`:
```json
{
  "round": 2,
  "story_file": "stories/brave-dragon_v0_draft.md",
  "output_file": "stories/brave-dragon_v1_reviewed.md",
  "status": "completed",
  "final_score": 8.5,
  "score_progression": [5.8, 7.4, 8.5],
  "timestamp": "2026-03-19T23:00:00"
}
```
2. Write final verdict to `STORY_REVIEW.md`
3. If approved: copy to `output/approved/`
4. If max rounds without approval: list remaining issues
5. Update `SCORE_TRACKER.md` with final entry

## Key Rules

- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask the user — just do it silently.
- **Never overwrite input**: Always create `_v1_reviewed.md` from `_v0_draft.md`
- **Track every score**: `SCORE_TRACKER.md` must be updated after EVERY round
- **State persistence**: `REVIEW_STATE.json` survives context window resets
