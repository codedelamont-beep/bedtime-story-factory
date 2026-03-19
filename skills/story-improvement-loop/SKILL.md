---
name: story-improvement-loop
description: "Autonomously improve a reviewed story via cross-model review → implement fixes → re-score, for 2 rounds. Separate from first review — runs on already-reviewed stories for final polishing. Use when user says 'improve story', 'polish story', 'improvement loop', 'auto improve'."
argument-hint: [story-file-path]
---

# Story Improvement Loop — Review → Fix → Re-Score

Autonomously improve: **$ARGUMENTS**

## Context

This skill runs **after** `/story-review` (Workflow 3a). It takes an already-reviewed story (`_v1_reviewed.md`) and iteratively polishes it through focused improvement passes.

Unlike `/story-review` (which catches structural issues — vocabulary, age-appropriateness, safety), this skill focuses on **prose quality** — rhythm, parent appeal, emotional resonance, and that "read-it-again" magic.

## Constants

- MAX_ROUNDS = 2
- POSITIVE_THRESHOLD = 9/10
- REVIEWER_MODEL = "gpt-4o"
- HUMAN_CHECKPOINT = false
- IMPROVEMENT_LOG = "IMPROVEMENT_LOG.md"

> 💡 Override: `/story-improvement-loop "stories/dragon_v1_reviewed.md" — human checkpoint: true, max_rounds: 3`

## Inputs

1. **`stories/{slug}_v1_reviewed.md`** (best) — already reviewed story
2. **`SCORE_TRACKER.md`** — previous review scores for context
3. **`STORY_REVIEW.md`** — previous round details

If the input file is `_v0_draft.md`, warn: "This story hasn't been reviewed yet. Run `/story-review` first." Then proceed anyway if `AUTO_PROCEED = true`.

## State Persistence (Crash Recovery)

Write `IMPROVEMENT_STATE.json` after each round:

```json
{
  "story_file": "stories/brave-dragon_v1_reviewed.md",
  "current_round": 1,
  "status": "in_progress",
  "last_score": 8.2,
  "score_progression": [7.4, 8.2],
  "timestamp": "2026-03-19T23:30:00"
}
```

**On context window reset / startup:**
1. Check if `IMPROVEMENT_STATE.json` exists
2. If `status == "in_progress"` AND `timestamp` < 24h:
   - Print: "🔄 Resuming improvement of [story_file] from Round [N]"
   - Read `IMPROVEMENT_LOG.md` for previous round details
   - Check if `stories/{slug}_v2_improving.md` exists (working copy)
   - Resume from the next round
3. If `status == "paused_human"`:
   - Print: "⏸ Improvement paused at Round [N]. Pending fixes: [list]"
   - Present fixes and wait for response
4. If `status == "completed"` or file absent → start fresh

**Notification integration:** After each round, call `/story-notify` with improvement score:
```
/story-notify "✨ Improved: [title] — Score: [before] → [after] (+[delta])"
```

## Workflow

### Step 0: Preserve Input

```bash
# Don't modify the reviewed version — we'll create v2
cp stories/{slug}_v1_reviewed.md stories/{slug}_v2_improving.md
```

Work on the `_v2_improving.md` copy. The `_v1_reviewed.md` is preserved.

### Step 1: Collect Story + Context

Read the story text and previous review scores from `SCORE_TRACKER.md`:

```
Previous scores:
- R0 draft: 5.8/10
- R1 review: 7.4/10
- Weakest criteria: [list bottom 3]
```

### Step 2: Round 1 — Prose Quality Review

Send to REVIEWER_MODEL with a **different focus** than the first review:

```
You are a bestselling children's book author and craft editor.
This story has already passed basic review checks.

Now focus on CRAFT refinement using the same 10 criteria:

[Full story text]

Score 1-10 on each:
1. **Read-aloud rhythm** — Musical stress patterns? No stumbles when tired?
2. **Sound design** — Onomatopoeia, alliteration, mouth-feel words?
3. **Refrain strength** — Repeating phrase that gains emotional power?
4. **Show-don't-tell** — Emotions as physical sensation, not stated?
5. **Page-turn anticipation** — Each spread ends with curiosity/tension?
6. **Character distinctiveness** — Describable in 5 words? Unique voice?
7. **Re-read gravity** — Child says "again!" Parent survives reading #50?
8. **Visual filmability** — Illustrator can see exactly what to draw?
9. **Wind-down quality** — Final 3 spreads descend? Whisper test passes?
10. **Golden line** — One line good enough to tattoo on a nursery wall?

Overall: X/10
Verdict: PUBLISH / ALMOST / NEEDS POLISH

For each score < 8, give ONE specific, actionable fix.
```

### Step 2b: Human Checkpoint (if enabled)

**Skip if `HUMAN_CHECKPOINT = false`.**

```
📋 Improvement Round 1 complete.

Score: X/10 — [verdict]
Weakest areas:
1. [criterion]: X/10 — [suggested fix]
2. [criterion]: X/10 — [suggested fix]

Reply "go" to implement all fixes, give custom instructions, "skip 2" to skip specific fixes, or "stop" to end.
```

Parse user response:
- **"go"** → implement all suggested fixes
- **"skip N"** → skip fix #N, implement the rest
- **"stop"** → save current state, terminate
- **Custom text** → use as additional instructions for fixes

### Step 3: Implement Round 1 Fixes

Priority order (prose quality focused):

| Issue | Fix Pattern |
|-------|-------------|
| Rhythm breaks | Rewrite sentences for read-aloud flow, vary length |
| Flat sensory | Add what character sees, hears, feels, smells |
| Weak character voice | Add distinctive speech patterns, reactions |
| Low emotional hit | Deepen the "warm moment" — show don't tell |
| Parent boredom | Add subtle humor, wordplay, or clever reference |
| No re-read hook | Add a catchphrase, refrain, or interactive moment |
| Jarring ending | Progressively shorter sentences, softer words, fade to quiet |
| No memorable line | Craft one "quotable" line parents will remember |

### Step 4: Round 2 — Final Polish Review

Send updated story to REVIEWER_MODEL again:

```
This is Round 2 of improvement.

Previous scores: [round 1 scores]
Changes made since Round 1:
1. [Fix 1]
2. [Fix 2]

[Full updated story text]

Same 8 criteria. Re-score and note what improved.
```

### Step 4b: Human Checkpoint (if enabled)

Same as Step 2b.

### Step 5: Implement Round 2 Fixes

Typical Round 2 fixes are subtle:
- Polish the "golden line" (the one memorable moment)
- Ensure the last 3 sentences are progressively shorter and quieter
- Add one more sensory detail to the opening scene
- Smooth any transitions that still feel rushed

### Step 6: Version Output

Create final version:

- Output: `stories/{slug}_v2_improved.md`

Frontmatter must include:
```yaml
version: 2
version_label: "improved"
previous_version: "stories/{slug}_v1_reviewed.md"
improvement_score: X.X
improvement_rounds: 2
score_progression: [5.8, 7.4, 8.6, 9.1]
```

### Step 7: Score Progression Update

Append to `SCORE_TRACKER.md`:

```markdown
## Score Progression: "[Story Title]" (Improvement Loop)

| Round | Time | Rhythm | Sound | Refrain | Show | PageTurn | Char | Reread | Visual | Wind | Gold | Overall | Δ |
|-------|------|--------|-------|---------|------|----------|------|--------|--------|------|------|---------|---|
| R1 review input | — | — | — | — | — | — | — | — | — | — | — | 7.4 | — |
| R2 improve-1 | HH:MM | X | X | X | X | X | X | X | X | X | X | X.X | +X.X |
| R3 improve-2 | HH:MM | X | X | X | X | X | X | X | X | X | X | X.X | +X.X |
```

### Step 8: Document Results

Create/append to `IMPROVEMENT_LOG.md`:

```markdown
# Improvement Log: "[Story Title]"

## Score Progression

| Round | Score | Verdict | Key Changes |
|-------|-------|---------|-------------|
| Input (v1) | 7.4/10 | — | Baseline from /story-review |
| Improve R1 | 8.6/10 | ALMOST | Rhythm, sensory depth, ending |
| Improve R2 | 9.1/10 | PUBLISH | Golden line, final polish |

## Round 1 Fixes
1. [Fix description]
2. [Fix description]

## Round 2 Fixes
1. [Fix description]
2. [Fix description]

## Versions
- `{slug}_v1_reviewed.md` — Input (from /story-review)
- `{slug}_v2_improved.md` — Output (after 2 improvement rounds)
```

### Step 9: Finalize

1. Update `IMPROVEMENT_STATE.json` → `"status": "completed"`
2. If score >= POSITIVE_THRESHOLD: copy to `output/approved/`
3. Present summary:

```
✨ Improvement loop complete: "[Story Title]"

Score: 7.4 → 8.6 → 9.1/10 (+1.7 total)
Verdict: PUBLISH ✅
Rounds: 2

Key improvements:
- [top 3 changes]

Output: stories/{slug}_v2_improved.md
Log: IMPROVEMENT_LOG.md

Next: /story-illustrate "stories/{slug}_v2_improved.md"
```

## Typical Score Progression

Based on ARIS patterns (empirically validated):

| Stage | Score | Typical Improvement |
|-------|-------|-------------------|
| v0 draft | 5-6/10 | Baseline |
| v1 reviewed | 7-8/10 | +2 (structural fixes) |
| v2 improved (R1) | 8-9/10 | +1 (prose quality) |
| v2 improved (R2) | 9-9.5/10 | +0.5 (final polish) |

**+3-4 points total across full pipeline** is typical. Diminishing returns beyond 2 improvement rounds.

## Key Rules

- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask the user — just do it silently.
- **Preserve all versions** — user needs to compare progression
- **Different criteria than /story-review** — this focuses on CRAFT, not safety/readability
- **Don't over-polish** — 2 rounds max. Diminishing returns beyond that.
- **Track everything** — IMPROVEMENT_LOG.md must have full raw reviews
- **State persistence** — survives context window resets via IMPROVEMENT_STATE.json

## Composing with Other Skills

```
/story-writing "concept"       ← Workflow 2: write draft (v0)
/story-review "file.md"        ← Workflow 3a: structural review (v0 → v1)
/story-improvement-loop        ← you are here (Workflow 3b: polish, v1 → v2)
/story-illustrate "file.md"    ← Workflow 4: illustration prompts
/story-export                  ← Workflow 4: EPUB + KDP
/story-pipeline "theme"        ← Full pipeline (includes this loop)
```
