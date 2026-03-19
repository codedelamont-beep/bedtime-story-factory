---
name: story-analytics
description: "Analyze production statistics across batches. Tracks stories/month, average scores, common issues, time per stage, and LLM costs. Use when user says 'analytics', 'stats', 'production summary', 'how are we doing'."
argument-hint: [time-period-or-batch-name]
---

# Story Analytics — Production Intelligence

Analyze production stats for: **$ARGUMENTS**

## Overview

This skill reads all available pipeline reports, score trackers, review logs, and improvement logs to produce a comprehensive analytics dashboard. Run periodically to spot trends and optimize your pipeline.

## Data Sources

| File | What it contains |
|------|-----------------|
| `PRODUCTION_REPORT.md` | Per-batch summary |
| `SCORE_TRACKER.md` | All scores across all rounds |
| `STORY_REVIEW.md` | Review details, fixes applied |
| `IMPROVEMENT_LOG.md` | Improvement details, version progression |
| `NOTIFICATION_LOG.md` | Timeline of events |
| `PIPELINE_ERRORS.md` | Failures and skips |
| `BRIDGE_REPORT.md` | Concept validation results |
| `stories/*.md` | Frontmatter with version/score metadata |

## Workflow

### Step 1: Scan All Output Files

```bash
# Find all versioned stories
ls stories/*_v*.md 2>/dev/null | wc -l

# Find all production reports  
ls PRODUCTION_REPORT*.md 2>/dev/null | wc -l

# Count approved stories
ls output/approved/*.md 2>/dev/null | wc -l
```

### Step 2: Extract Metrics

Parse frontmatter from all story files to collect:

- Total stories produced (all versions)
- Total stories approved (in output/approved/)
- Average scores at each version stage (v0, v1, v2)
- Most common review issues
- Average improvement delta per round
- Stories per batch
- Time per batch (from PRODUCTION_REPORT.md timestamps)

### Step 3: Generate Analytics Report

Create/overwrite `ANALYTICS.md`:

```markdown
# 📊 Story Factory — Analytics Dashboard

**Report generated**: [today]
**Period**: [time period or "all time"]

## Production Summary

| Metric | Value |
|--------|-------|
| Total batches run | X |
| Total stories drafted (v0) | X |
| Total stories reviewed (v1) | X |
| Total stories improved (v2) | X |
| Total stories approved | X |
| Approval rate | X% |
| Average pipeline duration | X hours |

## Quality Metrics

### Score Progression (averages)

| Version | Avg Score | Typical Range |
|---------|-----------|---------------|
| v0 draft | X.X/10 | X-X |
| v1 reviewed | X.X/10 | X-X |
| v2 improved | X.X/10 | X-X |
| Final | X.X/10 | X-X |

### Average Improvement by Stage

```
Draft → Review:      +X.X points (structural fixes)
Review → Improve R1: +X.X points (prose quality)
Improve R1 → R2:     +X.X points (final polish)
Total pipeline:       +X.X points average
```

### Weakest Criteria (most common < 8/10)

| Rank | Criterion | Avg Score | Times < 8 |
|------|-----------|-----------|----------|
| 1 | [criterion] | X.X | X times |
| 2 | [criterion] | X.X | X times |
| 3 | [criterion] | X.X | X times |

### Strongest Criteria

| Rank | Criterion | Avg Score |
|------|-----------|-----------|
| 1 | [criterion] | X.X |
| 2 | [criterion] | X.X |

## Bridge Performance

| Metric | Value |
|--------|-------|
| Concepts evaluated | X |
| GO rate | X% |
| MODIFY rate | X% |
| SKIP rate | X% |
| Avg viability score | X.X/10 |

## Cost Analysis (if LLM cost data available)

| Item | Cost |
|------|------|
| Avg cost per story (review) | $X.XX |
| Avg cost per batch | $X.XX |
| Total LLM spend | $X.XX |

## Recommendations

Based on the data:

1. **[Recommendation based on weakest criteria]**
   - e.g., "Bedtime suitability scores lowest — add explicit wind-down instructions to writing prompts"

2. **[Recommendation based on bridge data]**
   - e.g., "30% of concepts are SKIPped at bridge — tighten concept generation prompts"

3. **[Recommendation based on improvement data]**
   - e.g., "Improvement R2 adds only +0.3 — consider reducing MAX_ROUNDS to 1 for cost savings"

## Top Stories

| # | Title | Final Score | Batch |
|---|-------|------------|-------|
| 1 | "[Title]" | 9.5/10 | [batch] |
| 2 | "[Title]" | 9.4/10 | [batch] |
| 3 | "[Title]" | 9.3/10 | [batch] |
```

### Step 4: Present Summary

```
📊 Analytics complete!

Stories: [N] produced, [N] approved ([X]% rate)
Quality: avg [X.X]/10 final score
Weakest: [criterion] (avg [X.X])
Cost: $[X.XX] total across [N] batches

Full report: ANALYTICS.md
```

## Key Rules

- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask the user — just do it silently.
- **Don't fabricate data** — only report what's actually in the files
- **Include recommendations** — data without action items is useless
- **Track trends** — if multiple batches exist, show improvement over time
- **Cost-conscious** — always include cost recommendations
