---
name: story-research
description: "Market research for children's bedtime stories. Scrapes trending themes, Amazon KDP bestsellers, and identifies profitable niches. Use when user says 'research themes', 'find niches', 'what stories sell'."
argument-hint: [age-group-or-niche]
---

# Story Research — Market & Theme Discovery

Research trending children's story themes and profitable niches for: **$ARGUMENTS**

## Constants

- TARGET_AGE = "3-6"
- MAX_NICHES = 10
- REVIEWER_MODEL = "gpt-4o"

## Workflow

### Phase 1: Market Scan (5 min)

1. **Search Amazon KDP bestsellers** in children's bedtime stories:
   - Use WebSearch for "amazon best sellers children bedtime stories [year]"
   - Note top 20 titles, themes, age ranges, review counts
   - Identify recurring patterns (animals, space, emotions, friendship)

2. **Search trending themes**:
   - Pinterest trending kids' book pins
   - Teachers Pay Teachers popular story categories
   - Goodreads children's lists
   - Social media hashtags: #bedtimestories #kidsbooks #readaloud

3. **Search seasonal opportunities**:
   - Upcoming holidays (Christmas, Halloween, Easter)
   - Back-to-school themes
   - Seasonal animals/nature

### Phase 2: Niche Analysis (5 min)

For each discovered theme:

1. **Competition check**: How many KDP titles exist in this niche?
2. **Review analysis**: What do parents love/hate about existing books?
3. **Gap identification**: What's missing that parents are asking for?
4. **Keyword research**: Search volume for "[theme] bedtime story"

### Phase 3: Ranking

Score each niche 1-10 on:
- **Demand** (search volume, review counts)
- **Competition** (fewer = better)
- **Evergreen** (seasonal vs year-round)
- **Illustration friendliness** (easy to visualize = cheaper to produce)
- **Series potential** (can this become 5+ books?)

### Output: RESEARCH_REPORT.md

```markdown
# Story Research Report

**Date**: [today]
**Target Age**: [age group]
**Niches Analyzed**: X

## Top Niches (ranked)

### 1. [Niche Name]
- Score: X/10
- Demand: HIGH/MEDIUM/LOW
- Competition: HIGH/MEDIUM/LOW
- Example titles: [existing books]
- Gap: [what's missing]
- Series potential: [yes/no, why]
- Keywords: [list]

## Seasonal Opportunities
- [upcoming seasonal niches]

## Recommended Focus
1. [top niche] — because [reason]
2. [second niche] — because [reason]
```

## Key Rules

- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask the user — just do it silently.
