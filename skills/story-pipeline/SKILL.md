---
name: story-pipeline
description: "Full overnight story production pipeline. Chains all skills: research → concept → originality → writing → review → illustrate → export. Run before bed, wake up to finished stories. Use when user says 'story pipeline', 'overnight run', 'batch stories', 'full pipeline'."
argument-hint: [batch-description]
---

# Story Pipeline — Overnight Production Factory

End-to-end story production for: **$ARGUMENTS**

## Constants

- AUTO_PROCEED = true
- MAX_STORIES = 10
- TARGET_AGE = "3-6"
- WORD_COUNT = 800
- MAX_REVIEW_ROUNDS = 3
- ILLUSTRATION_PROMPTS = true
- OUTPUT_FORMAT = "markdown, epub"
- REVIEWER_MODEL = "gpt-4o"
- HUMAN_CHECKPOINT = false
- NOTIFICATION_LEVEL = "all"

> Override: `/story-pipeline "5 space stories" — target_age: 6-9, word_count: 1200`

## Batch Scheduling

Plan multiple overnight runs ahead of time:

```
/story-pipeline "theme" — schedule: nightly, nights: 5
```

This generates `BATCH_SCHEDULE.md`:

```markdown
# 📅 Batch Schedule

| Night | Date | Theme | Stories | Status |
|-------|------|-------|---------|--------|
| 1 | 2026-03-20 | magical forest animals | 10 | ⬜ Pending |
| 2 | 2026-03-21 | ocean adventures | 10 | ⬜ Pending |
| 3 | 2026-03-22 | space bedtime journeys | 10 | ⬜ Pending |
| 4 | 2026-03-23 | dinosaur friendship | 10 | ⬜ Pending |
| 5 | 2026-03-24 | garden fairy tales | 10 | ⬜ Pending |
```

**Theme generation:** If only one theme is given, the pipeline auto-generates related themes for subsequent nights using the research skill's niche data.

**On each night run:**
1. Read `BATCH_SCHEDULE.md`
2. Find first ⬜ Pending night
3. Run pipeline for that theme
4. Update status to ✅ Complete with score summary
5. User runs `/story-pipeline` each night (or sets up cron for Claude Code)

## Pipeline

```
Stage 1     Stage 2      Stage 3         Stage 3.5       Stage 4         Stage 5        Stage 6
Research → Concepts → Originality →   Bridge     →  Write Each  → Review Each → Improve Each →
(5 min)    (5 min)    (5 min)       (5 min)       (5 min each)  (10 min each)  (5 min each)

 Stage 7            Stage 8            Stage 9       Stage 10      Stage 11
→ Char Bible  →  Illustrate Each  →  Layout Each  → Export All → Series Wrap
  (10 min)       (5 min each)       (5 min each)    (2 min)      (5 min)
```

**Total for 10 stories: ~6-7 hours. Perfect for overnight.**

### Stage 1: Research

```
/story-research "$ARGUMENTS"
```

Output: `RESEARCH_REPORT.md` with ranked niches.

### Stage 2: Concept Generation

```
/story-concept "[top niche from research]"
```

Output: `CONCEPT_REPORT.md` with 10+ ranked concepts.

**Gate 1** (if AUTO_PROCEED=false): Present top concepts, wait for approval.

### Stage 3: Originality Check

```
/originality-check "[each concept]"
```

Output: `ORIGINALITY_REPORT.md`. Replace any REJECTED concepts with new ones.

### Stage 3.5: Bridge Validation (NEW)

```
/story-bridge
```

Output: `BRIDGE_REPORT.md` with GO / MODIFY / SKIP per concept.
Only concepts marked **GO** proceed to writing. This prevents wasting write time on weak concepts.

**Gate 2** (if AUTO_PROCEED=false): Present bridge report, wait for approval.

### Stage 4: Story Writing (batch)

For each approved concept (up to MAX_STORIES):
```
/story-writing "[concept]"
```

Output: `stories/[title-slug]_v0_draft.md` per story. (Versioned!)

### Stage 5: Auto Review (batch)

For each story:
```
/story-review "stories/[title-slug]_v0_draft.md"
```

Output: `stories/[title-slug]_v1_reviewed.md`. Stories polished to score >= 8/10 or flagged.

### Stage 6: Improvement Loop (NEW)

For each reviewed story that scored < 9/10:
```
/story-improvement-loop "stories/[title-slug]_v1_reviewed.md"
```

Output: `stories/[title-slug]_v2_improved.md`. 2 rounds of craft-focused polishing.
Skip if story already scored >= 9/10 after review (diminishing returns).

### Stage 7: Character Bible (batch)

For each approved story (or series), create character bible:
```
/story-character-bible "stories/[title-slug]_v2_improved.md"
```

Output: `characters/[slug]/` with style-lock prompts, anchor image prompts, color palettes.

### Stage 8: Illustration (batch)

For each approved story (latest version):
```
/story-illustrate "stories/[title-slug]_v2_improved.md"
```

Output: `illustrations/[slug]/spreads/` with actual generated images + QC reports.

### Stage 9: Layout (batch)

For each illustrated story:
```
/story-layout "stories/[title-slug]_v2_improved.md"
```

Output: `output/[slug]/` with fixed-layout EPUB + print-ready PDF with bleed.

### Stage 10: Export

```
/story-export "output/approved/"
```

Output: KDP-compliant metadata, AI disclosure, descriptions, pricing strategy.

### Stage 11: Series (optional)

If batch is part of a series:
```
/story-series "[series-name]"
```

Output: Series bible, sequel hooks, Amazon A+ content, branding guidelines.

### Final Report

```markdown
# 🌙 Story Factory — Production Report

**Batch**: $ARGUMENTS
**Date**: [start] → [end]
**Duration**: X hours

## Production Summary

| Stage | Status | Output |
|-------|--------|--------|
| Research | ✅ | 10 niches found |
| Concepts | ✅ | 12 generated, 10 survived |
| Originality | ✅ | 10 passed, 0 rejected |
| Bridge | ✅ | 8 GO, 1 MODIFY, 1 SKIP |
| Writing | ✅ | 9 stories drafted (v0) |
| Review | ✅ | 9 reviewed (v1), avg 7.8/10 |
| Improve | ✅ | 7 improved (v2), avg 9.1/10 |
| Char Bible | ✅ | 9 character bibles created |
| Illustration | ✅ | 126 images generated (14 spreads × 9) |
| Layout | ✅ | 9 print-ready PDFs + EPUBs |
| Export | ✅ | 9 KDP packages ready |
| Series | ✅ | Series bible + sequel hooks |

## Stories Produced

| # | Title | v0 | v1 | v2 | Final | Words | Status |
|---|-------|-----|-----|-----|-------|-------|--------|
| 1 | "[Title]" | 5.8 | 7.4 | 9.1 | 9.1 | 812 | ✅ Ready |
| 2 | "[Title]" | 6.2 | 8.5 | — | 8.5 | 795 | ✅ Ready |
| ... | ... | ... | ... | ... | ... | ... | ... |

## Revenue Estimate
- KDP ebooks (9 titles × $2.99): potential $X/mo at Y sales/day
- Illustration packs: 72 prompts ready for Midjourney

## Next Steps
- [ ] Run Midjourney prompts (feed illustration/*.txt)
- [ ] Upload EPUBs to KDP
- [ ] Create KDP listings from metadata files
- [ ] Schedule next batch: /story-pipeline "[next theme]"
```

## Typical Overnight Timeline

| Time | Stage | Can Sleep? |
|------|-------|------------|
| 22:00 | Start pipeline | Not yet |
| 22:05 | Research + Concepts done | Almost |
| 22:10 | Originality checked | Almost |
| 22:15 | Bridge validated | Yes ✅ |
| 22:15-23:00 | Writing 10 stories (v0) | Yes ✅ |
| 23:00-01:00 | Reviewing all stories (v0→v1) | Yes ✅ |
| 01:00-01:50 | Improving stories (v1→v2) | Yes ✅ |
| 01:50-02:20 | Illustrating | Yes ✅ |
| 02:20-02:25 | Exporting | Yes ✅ |
| 06:00 | You wake up → stories ready | ☕ |

## State Persistence (Crash Recovery)

On each stage completion, save `PIPELINE_STATE.json`:

```json
{
  "pipeline_id": "batch-20260319-2200",
  "batch_description": "$ARGUMENTS",
  "current_stage": 4,
  "current_story_index": 3,
  "total_stories": 10,
  "status": "in_progress",
  "started_at": "2026-03-19T22:00:00",
  "last_updated": "2026-03-19T23:15:00",
  "stage_results": {
    "1_research": { "status": "complete", "output": "RESEARCH_REPORT.md" },
    "2_concepts": { "status": "complete", "output": "CONCEPT_REPORT.md", "count": 12 },
    "3_originality": { "status": "complete", "passed": 10, "rejected": 2 },
    "4_writing": { "status": "in_progress", "completed": 3, "pending": 7 },
    "5_review": { "status": "pending" },
    "6_illustrate": { "status": "pending" },
    "7_export": { "status": "pending" }
  },
  "stories": [
    { "slug": "brave-dragon", "status": "v0_draft", "review_score": null },
    { "slug": "sleepy-owl", "status": "v1_reviewed", "review_score": 8.2 }
  ]
}
```

**On startup:**
1. Check if `PIPELINE_STATE.json` exists
2. If `status == "in_progress"` AND `last_updated` < 24h → RESUME from saved stage
3. If `status == "completed"` or file absent → start fresh
4. On resume: skip completed stages, continue from `current_stage` + `current_story_index`

**After each stage:** overwrite state file. On completion: set `"status": "completed"`.

## Version Tracking

Stories flow through pipeline with versioned filenames:

```
/story-writing     → stories/{slug}_v0_draft.md
/story-review      → stories/{slug}_v1_reviewed.md  (reads v0, outputs v1)
/story-improve     → stories/{slug}_v2_improved.md   (reads v1, outputs v2)
/story-export      → reads latest version for export
```

The pipeline always operates on the **latest version** of each story file.

## Error Recovery (Context Window Reset)

**CRITICAL for overnight runs.** Claude Code context windows can reset during long batches. This section ensures graceful recovery.

### On New Context Window

When the pipeline agent starts in a new context window (e.g. after crash or reset):

```
1. Read PIPELINE_STATE.json
2. If status == "in_progress":
   a. Print: "🔄 Resuming pipeline from Stage [N], Story [M]/[total]"
   b. Check which output files already exist:
      - stories/*_v0_draft.md → writing stage outputs
      - stories/*_v1_reviewed.md → review stage outputs  
      - stories/*_v2_improved.md → improvement stage outputs
   c. Skip stories that already have output files for current stage
   d. Resume from first incomplete story in current stage
3. If status == "completed":
   a. Print: "✅ Pipeline already completed. Run with new topic to start fresh."
4. If file missing:
   a. Start fresh pipeline
```

### Partial Stage Recovery

For batch stages (writing, review, improvement, illustration):

```python
# Pseudocode for resuming batch stages
for story in state.stories:
    expected_output = f"stories/{story.slug}_v{stage_version}_{label}.md"
    if file_exists(expected_output):
        print(f"  ⏭ Skipping {story.slug} — already has {label}")
        continue
    else:
        print(f"  ▶ Processing {story.slug}")
        execute_stage(story)
        update_state(story)
```

### Error During Execution

If any stage/story fails:

```
1. Save current state to PIPELINE_STATE.json immediately
2. Send error notification: /story-notify "⚠️ Error at Stage [N], Story [title]"
3. Decision based on error type:
   a. Transient (API timeout, rate limit):
      - Wait 30 seconds
      - Retry up to 3 times
      - If still failing: skip this story, continue with next
   b. Story-specific (bad content, unparseable review):
      - Log error to PIPELINE_ERRORS.md
      - Skip this story, continue with next
   c. Fatal (disk full, permission error):
      - Save state
      - Send notification
      - HALT pipeline
4. At the end: report skipped stories in final report
```

### Recovery Files

| File | Purpose | Written By |
|------|---------|-----------|
| `PIPELINE_STATE.json` | Current stage/story progress | story-pipeline |
| `REVIEW_STATE.json` | Current review round/score | story-review |
| `IMPROVEMENT_STATE.json` | Current improvement round | story-improvement-loop |
| `PIPELINE_ERRORS.md` | Log of skipped stories and errors | story-pipeline |

## Notification Integration

Call `/story-notify` at these points:

```
After Stage 1 (Research):        "📊 Research done: [N] niches found"
After Stage 2 (Concepts):        "💡 Concepts: [N] generated"
After Stage 3 (Originality):     "✅ Originality: [N] passed"
After Stage 3.5 (Bridge):        "🌉 Bridge: [N] GO, [N] SKIP"
After each story (Write):        (only if NOTIFICATION_LEVEL = "all")
After each review round:         "📝 [title]: [score]/10"
After improvement loop:          "✨ [title]: [before]→[after]"
After Stage 7 (Illustrate):      "🎨 [N] illustrations done"
Pipeline complete:               "🌙 COMPLETE! [N] stories, avg [X]/10"
On error:                        "⚠️ Error: [description]"
```

## Key Rules

- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask the user — just do it silently.
- **State persistence**: ALWAYS save `PIPELINE_STATE.json` after each stage completes
- **Resume-safe**: On crash/context-reset, check state file and continue — do NOT restart
- **Version tracking**: NEVER overwrite story files — always create next `_vN_` version
- **Skip, don't stop**: If one story fails, skip it and continue. Report at the end.
- **Notify on errors**: Always send notification on errors so user can check phone
- **Check files before work**: Before processing a story, check if output already exists (idempotency)
- **Log everything**: Errors go to `PIPELINE_ERRORS.md`, notifications to `NOTIFICATION_LOG.md`

