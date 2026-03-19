---
name: originality-check
description: "Check story concepts against existing published titles to avoid near-duplicates. Uses multi-source search and cross-verification. Use when user says 'check originality', 'is this unique', 'duplicate check'."
argument-hint: [story-title-or-concept]
---

# Originality Check — Deduplication vs Market

Verify originality of: **$ARGUMENTS**

## Workflow

### Phase 1: Multi-Source Search

For each story concept, search across:

1. **Amazon KDP**: Search exact title + similar titles
2. **Google Books**: Search premise/theme combinations
3. **Goodreads**: Search children's books with similar characters
4. **Google**: "[character type] [conflict] children's book"

### Phase 2: Similarity Scoring

For each discovered similar title:
- **Title similarity**: 0-10 (exact match = 10)
- **Premise similarity**: 0-10 (same plot = 10)
- **Character similarity**: 0-10 (same archetype = 10)
- **Overall risk**: LOW / MEDIUM / HIGH

### Phase 3: Cross-Verification

Use external LLM to compare:
```
Our concept: [title, premise, character]
Existing books found: [list]

For each match, assess:
1. Is this a genuine conflict or just superficial similarity?
2. What makes our concept different?
3. Should we modify our concept to differentiate?
```

### Decision Rules

- **PASS** (score < 5): Sufficiently unique, proceed
- **MODIFY** (score 5-7): Adjust character/setting to differentiate
- **REJECT** (score > 7): Too similar, generate replacement concept

### Output: ORIGINALITY_REPORT.md

```markdown
# Originality Check Report

| Concept | Similar Titles Found | Risk | Verdict |
|---------|---------------------|------|---------|
| "[Title 1]" | 2 similar | LOW | PASS |
| "[Title 2]" | 1 near-match | HIGH | MODIFY |

## Details per concept
### "[Title]"
- Closest match: "[Existing Book]" by [Author]
- Similarity: X/10
- Key difference: [what makes ours unique]
- Recommendation: PASS / MODIFY [how] / REJECT
```
