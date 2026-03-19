---
name: story-market-monitor
description: "Post-publish optimization: track KDP sales, KENP reads, reviews, rankings. A/B test descriptions, adjust pricing, identify what's working. Run weekly or after launch. Use when user says 'how are sales', 'check performance', 'market monitor', 'optimize listings'."
argument-hint: [book-title-or-series-name]
---

# Story Market Monitor — Post-Publish Optimization

Monitor and optimize: **$ARGUMENTS**

> Run this skill **after** books are published on KDP. It's the feedback loop that tells you what's working and what to change.

## Constants

- REVIEW_INTERVAL = "weekly"
- MIN_REVIEWS_FOR_ANALYSIS = 5
- PRICE_TEST_DURATION = "14 days"
- KDP_DASHBOARD_URL = "https://kdp.amazon.com/en_US/bookshelf"

## Workflow

### Phase 1: Performance Snapshot

Collect current data (manually from KDP dashboard or via KDP API if available):

```markdown
## Performance Snapshot: "[Title/Series]"

**Date**: [today]
**Days since launch**: X

### Sales Data
| Book | Ebook Units | KU Pages Read | Paperback Units | Revenue (est) |
|------|-------------|---------------|-----------------|---------------|
| Book 1 | X | X,XXX | X | $XX.XX |
| Book 2 | X | X,XXX | X | $XX.XX |
| Total | X | X,XXX | X | $XX.XX |

### Rankings
| Book | Best Sellers Rank | Category Rank | Category |
|------|------------------|---------------|----------|
| Book 1 | #XX,XXX | #XX | Children > Bedtime |
| Book 2 | #XX,XXX | #XX | Children > Bedtime |

### Review Summary
| Book | Total Reviews | Avg Rating | Most Recent |
|------|--------------|------------|-------------|
| Book 1 | X | X.X⭐ | "[quote]" |
```

### Phase 2: Review Intelligence

Analyze published reviews for quality signals:

```markdown
## Review Analysis: "[Title]"

### What Parents Love (positive signals)
| Signal | Frequency | Example Quote |
|--------|-----------|---------------|
| Re-read request | X mentions | "My daughter asks for this every night" |
| Read-aloud quality | X mentions | "Flows beautifully when reading aloud" |
| Illustration praise | X mentions | "The watercolors are gorgeous" |
| Emotional impact | X mentions | "Made us both tear up at the end" |
| Golden line quoted | X mentions | "[specific line parents quote]" |

### What Parents Dislike (improvement signals)
| Signal | Frequency | Example Quote | Action |
|--------|-----------|---------------|--------|
| Too short | X mentions | "Wish it was longer" | Consider longer version |
| Text hard to read | X mentions | "Font too small on images" | Adjust layout |
| Not sleepy enough | X mentions | "Wound up, not down" | Review wind-down |
| AI art noticed | X mentions | "Illustrations look AI" | Improve image quality |

### Craft Feedback Loop
| Craft Element | Review Evidence | Working? |
|---------------|----------------|----------|
| Refrain | Parents quote it → YES | ✅ |
| Sound design | Kids make the sounds → YES | ✅ |
| Golden line | Appears in reviews → YES | ✅ |
| Wind-down | "Falls asleep before the end" → YES | ✅ |
| Character | "Loves [name]" → YES | ✅ |
```

### Phase 3: Read-Through Analysis (Series)

For series, track how many Book 1 readers buy Book 2+:

```markdown
## Read-Through Analysis: "[Series Name]"

| Metric | Value | Industry Avg |
|--------|-------|-------------|
| Book 1 → Book 2 readthrough | X% | 30-50% |
| Book 2 → Book 3 readthrough | X% | 40-60% |
| Average books per reader | X.X | 2.5 |
| Lifetime reader value | $X.XX | $5-10 |

### Read-Through Optimization
If readthrough < 40%:
- [ ] Check sequel hook visibility in Book 1 ending
- [ ] Add "Also in this series" page to Book 1
- [ ] Verify series page setup on Amazon
- [ ] Consider Book 1 free promotion to seed funnel
```

### Phase 4: Listing Optimization

```markdown
## A/B Test Plan: "[Title]"

### Description Test
- Version A (current): "[first 50 chars of current description]..."
- Version B (test): "[first 50 chars of new description]..."
- Duration: 14 days
- Metric: Click-through rate (impressions → detail page views)

### Keyword Optimization
| Current Keyword | Search Volume | Rank | Replace With |
|----------------|---------------|------|-------------|
| [keyword 1] | LOW | #XX | [better keyword] |
| [keyword 2] | HIGH | #XX | Keep |

### Cover Test (if applicable)
- Test different tagline on cover
- Test different color emphasis
- Metric: Sales conversion rate
```

### Phase 5: Pricing Experiments

```markdown
## Pricing Experiment: "[Title]"

### Current State
- Ebook: $X.99 → selling X units/day
- Paperback: $X.99 → selling X units/day

### Experiment (14-day test)
| Change | From | To | Expected Impact |
|--------|------|----|----|
| Ebook price | $2.99 | $0.99 | +300% units, -50% revenue per unit |
| KU enrollment | No | Yes | +KENP reads, unknown impact on sales |

### Results (fill after 14 days)
| Metric | Before | After | Δ |
|--------|--------|-------|---|
| Daily ebook sales | X | X | +X% |
| Daily revenue | $X | $X | +X% |
| Daily KENP pages | X | X | +X% |
| Rankings | #XX | #XX | ↑/↓ |

### Decision: KEEP / REVERT / ADJUST
```

### Phase 6: Competitive Monitoring

```markdown
## Market Changes

### New Competitors
| Title | Launch Date | Price | Rank | Threat Level |
|-------|------------|-------|------|-------------|
| "[New Book]" | [date] | $X.99 | #XX | HIGH/MED/LOW |

### Category Trends
- [any shifts in what's selling]
- [new themes gaining traction]
- [seasonal opportunities approaching]

### Our Response
- [ ] [action item based on market changes]
```

### Output: MARKET_MONITOR.md

Updated weekly/monthly with cumulative data.

```
monitoring/
├── MARKET_MONITOR.md              ← Rolling performance log
├── snapshots/
│   ├── 2026-03-20.md              ← Weekly snapshots
│   ├── 2026-03-27.md
│   └── ...
├── experiments/
│   ├── pricing-test-book1.md      ← Experiment logs
│   └── description-ab-test.md
└── REVIEW_DIGEST.md               ← Analyzed review quotes
```

## Key Rules

- **Data over feelings**: Make decisions based on numbers, not guesses
- **14-day minimum tests**: Don't change pricing/description for at least 14 days
- **Review mining is gold**: Actual parent quotes reveal more than any metric
- **Read-through is the metric**: For series, readthrough rate matters more than individual book sales
- **Track craft feedback**: When parents quote your golden line, the craft guide is working
- **Large file handling**: If Write fails, use Bash fallback
