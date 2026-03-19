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

## Key Rules

- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask the user — just do it silently.
