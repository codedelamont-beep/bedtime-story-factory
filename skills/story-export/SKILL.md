---
name: story-export
description: "Format and export finished stories to EPUB, PDF, and KDP-ready formats. Combines story text with illustration placeholders. Use when user says 'export', 'publish', 'create epub', 'create pdf'."
argument-hint: [story-file-or-directory]
---

# Story Export — Publication Formatting

Export stories for publishing: **$ARGUMENTS**

## Constants

- OUTPUT_DIR = "output/"
- FORMATS = ["markdown", "epub"]
- KDP_TRIM = "8.5x8.5" (square format, popular for kids)

## Workflow

### Phase 1: Compile Story Package

For each approved story in `output/approved/`:

1. Read story markdown with frontmatter
2. Read illustration prompts from `illustrations/[slug]/`
3. Read style guide for cover metadata

### Phase 2: Markdown Export

Clean export with metadata header:
```markdown
---
title: "[Title]"
author: "[Author Name]"
age_range: "3-6"
word_count: 800
isbn: "" # add later
---

# [Title]

[Clean story text with page break markers]
```

### Phase 3: EPUB Generation

Using pandoc or similar:
```bash
pandoc stories/[slug].md \
  --output output/[slug].epub \
  --metadata title="[Title]" \
  --css styles/children-book.css \
  --epub-cover-image illustrations/[slug]/cover.png
```

### Phase 4: KDP Metadata

Generate KDP listing metadata:
```markdown
## KDP Listing: "[Title]"

- **Title**: [title]
- **Subtitle**: A Bedtime Story for Ages [age]
- **Author**: [name]
- **Description**: [150-word book description optimized for Amazon]
- **Keywords** (7 max): [keyword1, keyword2, ...]
- **Categories**: Children's Books > Bedtime & Dreams
- **Age Range**: [min]-[max]
- **Price**: $2.99-$4.99 (ebook) / $9.99-$14.99 (paperback)
```

### Phase 5: Batch Report

```markdown
# Export Report

**Date**: [today]
**Stories exported**: X

| Title | Word Count | Score | EPUB | PDF | KDP Ready |
|-------|------------|-------|------|-----|-----------|
| ... | 800 | 8/10 | ✅ | ✅ | ✅ |

## Files
output/
├── [title-1].epub
├── [title-1]-kdp-metadata.md
├── [title-2].epub
└── ...
```
