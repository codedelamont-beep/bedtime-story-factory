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

> **Reference `references/CRAFT_GUIDE.md` for evaluation standards.**

```
Prompt to REVIEWER_MODEL:
  You are a senior children's book editor at a major publishing house.
  You've edited 200+ bestselling picture books. You know what separates
  forgettable AI-generated text from books children beg to hear again.

  Review this bedtime story for ages [TARGET_AGE].

  [Full story text]

  ## SAFETY GATE (Pass/Fail — story is rejected if any fail):
  - [ ] No violence, death, injury, or scary content
  - [ ] Vocabulary appropriate for target age
  - [ ] Ending is peaceful and calming
  - [ ] No abandonment or anxiety themes

  ## CRAFT SCORING (1-10 each):
  1. Read-aloud rhythm — Can you read every sentence without stumbling?
     Do the stressed syllables create a musical pattern?
  2. Sound design — Are there enough onomatopoeia, alliteration, and
     mouth-feel words? Are the words "delicious" to say?
  3. Refrain strength — Is there a repeating phrase? Does it gain
     emotional power each time it appears?
  4. Show-don't-tell — Are emotions shown through physical sensation
     and observable behavior, never stated directly?
  5. Page-turn anticipation — Does each spread end with a hook
     that makes you want to turn the page?
  6. Character distinctiveness — Could a 4-year-old describe this
     character in 5 words after one reading?
  7. Re-read gravity — Would a child say "again!"? Is it bearable
     for a parent on reading #50?
  8. Visual filmability — Can an illustrator see exactly what to draw
     for each spread? Are the scenes specific, not vague?
  9. Wind-down quality — Do the final 3 spreads descend in energy?
     Does the last sentence pass the "whisper test"?
  10. Golden line — Is there one line good enough to whisper as the
      child falls asleep? Quote it.

  Overall craft score: X/10
  Verdict: PUBLISH / ALMOST / NEEDS CRAFT WORK
  
  Specific fixes needed (ranked by impact):
  For each fix, quote the current text and provide the improved version.
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

### Safety Gate: PASS / FAIL

### Craft Scores
| Criterion | Score |
|-----------|-------|
| Read-aloud rhythm | X/10 |
| Sound design | X/10 |
| Refrain strength | X/10 |
| Show-don't-tell | X/10 |
| Page-turn anticipation | X/10 |
| Character distinctiveness | X/10 |
| Re-read gravity | X/10 |
| Visual filmability | X/10 |
| Wind-down quality | X/10 |
| Golden line | X/10 |
| **Overall** | **X/10** |

### Fixes Applied
- [quote original text] → [replacement text]

### Status: continuing / approved
```

### Phase E: Score Progression Tracking

**After every round**, append to `SCORE_TRACKER.md`:

```markdown
## Score Progression: "[Story Title]"

| Round | Time | Rhythm | Sound | Refrain | Show | PageTurn | Char | Reread | Visual | Wind | Gold | Overall | Δ |
|-------|------|--------|-------|---------|------|----------|------|--------|--------|------|------|---------|---|
| R0 draft | HH:MM | X | X | X | X | X | X | X | X | X | X | X.X | — |
| R1 review | HH:MM | X | X | X | X | X | X | X | X | X | X | X.X | +X.X |
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
