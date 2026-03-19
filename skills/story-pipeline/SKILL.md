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

> Override: `/story-pipeline "5 space stories" — target_age: 6-9, word_count: 1200`

## Pipeline

```
Stage 1    Stage 2      Stage 3         Stage 4       Stage 5      Stage 6      Stage 7
Research → Concepts → Originality → Write Each → Review Each → Illustrate → Export All
(5 min)    (5 min)    (5 min)       (5 min each)  (10 min each) (3 min each) (2 min)
```

**Total for 10 stories: ~3-4 hours. Perfect for overnight.**

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

### Stage 4: Story Writing (batch)

For each approved concept (up to MAX_STORIES):
```
/story-writing "[concept]"
```

Output: `stories/[title-slug].md` per story.

### Stage 5: Auto Review (batch)

For each story:
```
/story-review "stories/[title-slug].md"
```

Output: Each story polished to score >= 8/10 or flagged for manual review.

### Stage 6: Illustration Prompts (batch)

For each approved story:
```
/story-illustrate "stories/[title-slug].md"
```

Output: `illustrations/[slug]/` with Midjourney prompts per scene.

### Stage 7: Export

```
/story-export "output/approved/"
```

Output: EPUB files + KDP metadata for each story.

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
| Writing | ✅ | 10 stories written |
| Review | ✅ | 8 approved, 2 need manual review |
| Illustration | ✅ | 80 scene prompts generated |
| Export | ✅ | 8 EPUBs ready |

## Stories Produced

| # | Title | Score | Words | Status |
|---|-------|-------|-------|--------|
| 1 | "[Title]" | 9/10 | 812 | ✅ Ready |
| 2 | "[Title]" | 8/10 | 795 | ✅ Ready |
| ... | ... | ... | ... | ... |

## Revenue Estimate
- KDP ebooks (8 titles × $2.99): potential $X/mo at Y sales/day
- Illustration packs: 80 prompts ready for Midjourney

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
| 22:10 | Originality checked | Yes ✅ |
| 22:10-23:00 | Writing 10 stories | Yes ✅ |
| 23:00-01:00 | Reviewing all stories | Yes ✅ |
| 01:00-01:30 | Illustrating | Yes ✅ |
| 01:30-01:35 | Exporting | Yes ✅ |
| 06:00 | You wake up → 10 stories ready | ☕ |

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

## Key Rules

- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask the user — just do it silently.
- **State persistence**: ALWAYS save `PIPELINE_STATE.json` after each stage completes
- **Resume-safe**: On crash/context-reset, check state file and continue — do NOT restart
- **Version tracking**: NEVER overwrite story files — always create next `_vN_` version
