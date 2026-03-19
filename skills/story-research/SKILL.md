---
name: story-research
description: "Market research + competitor craft analysis for children's bedtime stories. Scrapes trending themes, Amazon KDP bestsellers, identifies profitable niches, AND analyzes WHY top books succeed using craft techniques. Use when user says 'research themes', 'find niches', 'what stories sell'."
argument-hint: [age-group-or-niche]
---

# Story Research — Market & Craft Discovery

Research trending children's story themes and profitable niches for: **$ARGUMENTS**

## Constants

- TARGET_AGE = "3-6"
- MAX_NICHES = 10
- TOP_COMPETITORS_TO_ANALYZE = 3
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

### Phase 3: Competitor Craft Analysis (NEW — 10 min)

For the **top 3 bestselling books** in the target niche, analyze their craft techniques using the framework from `references/CRAFT_GUIDE.md`:

#### For Each Top Competitor:

Search for: "[book title] read aloud" or "[book title] pages" or "[book title] text" to find excerpts, reviews, and read-aloud recordings.

```markdown
## Craft Analysis: "[Competitor Title]" by [Author]

### What Makes It Sell (from reviews)
- Top praised element: [what parents/kids love most]
- Most-quoted line: "[the line that appears in reviews]"
- Re-read signals: [do reviews mention reading it 100x?]

### Craft Techniques Identified
| Technique | Used? | Example | Effectiveness |
|-----------|-------|---------|--------------|
| Refrain | ✅/❌ | "[example phrase]" | Strong/Weak/None |
| Sound design | ✅/❌ | "[onomatopoeia examples]" | Strong/Weak/None |
| Rhythm pattern | ✅/❌ | [trochaic/cumulative/etc.] | Strong/Weak/None |
| Show-don't-tell | ✅/❌ | "[emotion shown as action]" | Strong/Weak/None |
| Page-turn hooks | ✅/❌ | "[example hook line]" | Strong/Weak/None |
| Character distinctiveness | ✅/❌ | 5-word description: "[X]" | Strong/Weak/None |
| Wind-down pattern | ✅/❌ | [how it ends — last 3 lines] | Strong/Weak/None |
| Golden line | ✅/❌ | "[the memorable line]" | Strong/Weak/None |

### Illustration Style
- Style: [watercolor / digital / collage / photographic]
- Color palette: [warm / cool / mixed]
- Text placement: [overlay / split / dedicated page]
- Consistency: [same character look throughout? Y/N]

### What We Can Learn
- **Steal this**: [technique worth adopting]
- **Beat this**: [weakness we can improve on]
- **Avoid this**: [what doesn't work despite being popular]
```

#### Craft Pattern Summary

After analyzing 3 competitors:

```markdown
## Craft Patterns in This Niche

### What ALL top books do:
- [pattern found in 3/3 books]
- [pattern found in 3/3 books]

### What MOST top books do:
- [pattern found in 2/3 books]

### What creates the "again!" factor:
- [specific technique that drives re-reads]

### Gaps we can exploit:
- [craft technique none of them use that we can add]
- [weakness all share that we can fix]

### Recommended craft approach for our stories:
- Refrain style: [based on what works in this niche]
- Sound design: [what sounds resonate with this theme]
- Rhythm: [which pattern fits best]
- Wind-down: [how competitors handle sleep transition]
```

### Phase 4: Ranking

Score each niche 1-10 on:
- **Demand** (search volume, review counts)
- **Competition** (fewer = better)
- **Evergreen** (seasonal vs year-round)
- **Illustration friendliness** (easy to visualize = cheaper to produce)
- **Series potential** (can this become 5+ books?)
- **Craft opportunity** (NEW: can we out-craft the competition?)

### Output: RESEARCH_REPORT.md

```markdown
# Story Research Report

**Date**: [today]
**Target Age**: [age group]
**Niches Analyzed**: X
**Top Competitors Analyzed**: 3

## Top Niches (ranked)

### 1. [Niche Name]
- Score: X/10
- Demand: HIGH/MEDIUM/LOW
- Competition: HIGH/MEDIUM/LOW
- Craft opportunity: HIGH/MEDIUM/LOW
- Example titles: [existing books]
- Gap: [what's missing — both market AND craft gaps]
- Series potential: [yes/no, why]
- Keywords: [list]

## Competitor Craft Analysis
[Full analysis for top 3 books — see Phase 3 format]

## Craft Patterns Summary
[What all top books do, what most do, gaps we can exploit]

## Seasonal Opportunities
- [upcoming seasonal niches]

## Recommended Focus
1. [top niche] — because [market reason + craft opportunity]
2. [second niche] — because [market reason + craft opportunity]

## Recommended Craft Approach
Based on competitor analysis:
- Use [X] refrain style (it works in this niche)
- Incorporate [Y] sounds (matches the theme's world)
- Follow [Z] rhythm pattern (proven reader engagement)
- Beat competitors on: [their weakest craft area]
```

## Key Rules

- **Don't invent data**: Market research must use actual web searches, not fabricated numbers
- **Read real reviews**: Extract actual parent quotes, not summaries
- **Craft analysis requires evidence**: Quote specific lines from competitors, not vague impressions
- **Competitor analysis is NOT plagiarism planning**: We study technique, not copy content
- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask the user — just do it silently.
