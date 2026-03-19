---
name: story-bridge
description: "Workflow 1.5: Validate story concepts before investing writing time. Checks market viability, illustration feasibility, series potential, and cross-model 'would you buy this?' assessment. Use when user says 'validate concepts', 'bridge', 'check before writing'."
argument-hint: [concept-report-path-or-topic]
---

# Story Bridge — Concept Validation Gate

Validate concepts before writing: **$ARGUMENTS**

## Overview

This skill bridges Workflow 1 (Discovery) and Workflow 2 (Production). It prevents wasting writing time on concepts that won't sell, can't be illustrated, or are too similar to existing titles.

```
Workflow 1 output:                 This skill:                              Workflow 2 input:
CONCEPT_REPORT.md             →   validate → cross-model → score     →    approved concepts
ORIGINALITY_REPORT.md              market     review        GO/SKIP         ready for writing
```

## Constants

- MIN_VIABILITY_SCORE = 7/10
- MAX_CONCEPTS = 10
- REVIEWER_MODEL = "gpt-4o"
- AUTO_PROCEED = true

> Override: `/story-bridge "CONCEPT_REPORT.md" — min_viability: 8, reviewer: deepseek-chat`

## Inputs

This skill expects:

1. **`CONCEPT_REPORT.md`** (best) — ranked concepts from `/story-concept`
2. **`ORIGINALITY_REPORT.md`** — dedup results from `/originality-check`
3. **Direct concept** — if no reports exist, validate a single concept from arguments

If none exist, ask the user what concepts to validate.

## Workflow

### Phase 1: Parse Concepts

Read `CONCEPT_REPORT.md` and extract for each concept:

1. Title
2. Theme / moral
3. Target age range
4. Main character
5. Brief synopsis
6. Originality status (from ORIGINALITY_REPORT.md if available)

Present summary:

```
📋 Concepts loaded: [N]
- [N] passed originality check
- [N] pending validation

Proceeding to validation.
```

### Phase 2: Market Viability Check

For each concept, research via web search:

1. **Amazon KDP search**: Search for similar titles — how many exist? High competition = lower score
2. **Theme demand**: Are parents searching for this theme? (trending topics, seasonal relevance)
3. **Series potential**: Can this concept extend to 3-5 books? (characters, world, theme variations)
4. **Price point**: What do similar titles sell for on Amazon?

Score each concept 1-10 on market viability.

### Phase 3: Illustration Feasibility

For each concept, assess:

1. **Visual clarity**: Can each scene be clearly depicted? Abstract concepts score low.
2. **Character consistency**: Can the main character be drawn consistently across 8+ scenes?
3. **Scene variety**: Are there enough distinct visual moments? (not just "character talking")
4. **Style match**: Does the concept suit common children's illustration styles?
5. **Midjourney compatibility**: Can the scenes be described in Midjourney prompts?

Score each concept 1-10 on illustration feasibility.

### Phase 4: Cross-Model "Would You Buy This?" Review

Send each concept to the REVIEWER_MODEL:

```
You are a parent of a [TARGET_AGE]-year-old child evaluating bedtime story books.

Concept: "[title]"
Synopsis: [brief synopsis]
Moral: [lesson]
Character: [main character]

Score 1-10 on:
1. Would your child ask for this story again?
2. Would you enjoy reading this aloud?
3. Does the title grab attention on Amazon?
4. Is the moral valuable but not preachy?
5. Would you recommend this to other parents?

Overall: X/10
Verdict: BUY / MAYBE / PASS
One-sentence improvement suggestion:
```

### Phase 5: Aggregate & Decide

For each concept, compute:

```
Viability Score = (Market × 0.3) + (Illustration × 0.2) + (Parent Appeal × 0.5)
```

**Decision rules:**
- Viability >= MIN_VIABILITY_SCORE AND "BUY" → **GO** ✅
- Viability 5-6 AND "MAYBE" → **MODIFY** ⚠️ (apply improvement suggestions, re-assess)
- Viability < 5 OR "PASS" → **SKIP** ❌

### Phase 6: Output BRIDGE_REPORT.md

```markdown
# 🌉 Story Bridge — Concept Validation Report

**Date**: [today]
**Concepts evaluated**: [N]
**Input**: CONCEPT_REPORT.md

## Summary

| # | Title | Market | Illust | Appeal | Overall | Decision |
|---|-------|--------|--------|--------|---------|----------|
| 1 | "[Title]" | 8/10 | 9/10 | 8/10 | 8.3 | ✅ GO |
| 2 | "[Title]" | 6/10 | 7/10 | 5/10 | 5.7 | ❌ SKIP |
| 3 | "[Title]" | 7/10 | 8/10 | 7/10 | 7.2 | ✅ GO |

## Approved for Writing (GO)

### 1. "[Title]"
- **Why**: [reason it passed]
- **Series potential**: [can extend to X books]
- **Improvement applied**: [if any]

## Modified (applied suggestions)

### N. "[Title]"
- **Original issue**: [what was weak]
- **Modification**: [what changed]
- **New score**: X/10

## Skipped

### N. "[Title]"
- **Why skipped**: [reason]
- **Could recover if**: [what would need to change]

## Next Step
→ /story-writing "[first GO concept]"
```

### Phase 7: Handoff

Present final status:

```
🌉 Bridge validation complete:
- Evaluated: [N] concepts
- Approved (GO): [N] — ready for writing
- Modified: [N] — improved and re-approved
- Skipped: [N] — not viable

Report: BRIDGE_REPORT.md

Next step:
→ /story-writing (for single story)
→ /story-pipeline (continues automatically)
```

## Key Rules

- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask the user — just do it silently.
- **Don't invent data**: Market research must use actual web searches, not fabricated numbers
- **Be honest**: If a concept is weak, SKIP it. Don't force bad concepts through the pipeline.
- **Respect the pipeline**: This skill's output feeds directly into `/story-writing`
- **Modify before skipping**: If a concept scores MAYBE, try the reviewer's improvement suggestion before marking SKIP
- **Track everything**: Every decision must be documented in BRIDGE_REPORT.md with rationale

## Composing with Other Skills

```
/story-research "niche"        ← Workflow 1: find niches
/story-concept "theme"         ← Workflow 1: generate concepts
/originality-check             ← Workflow 1: dedup
/story-bridge                  ← you are here (Workflow 1.5: validate)
/story-writing "concept"       ← Workflow 2: write stories
/story-review "file.md"        ← Workflow 3: review
/story-improvement-loop        ← Workflow 3: polish
/story-pipeline "theme"        ← Full pipeline (includes this bridge)
```
