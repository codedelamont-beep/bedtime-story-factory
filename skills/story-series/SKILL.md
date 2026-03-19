---
name: story-series
description: "Manage book series — character bible persistence across stories, sequel hooks, series branding, read-through optimization. Use when user says 'series', 'sequel', 'book series', 'next book', 'character bible'."
argument-hint: [series-name-or-concept]
---

# Story Series — Multi-Book Production System

Manage series: **$ARGUMENTS**

## Constants

- SERIES_DIR = "series/"
- BOOKS_PER_SERIES = 5-12
- PRICING_BOOK_1 = "$0.99" (loss leader for read-through)
- PRICING_SUBSEQUENT = "$2.99"
- PRICING_BUNDLE = "$7.99" (3-pack)

## Workflow

### Phase 1: Series Bible Creation

```markdown
# Series Bible: "[Series Name]"

## Concept
- **Logline**: [One sentence that sells the entire series]
- **Target age**: [X-X]
- **Series hook**: [Why would a child want book #2?]
- **Parent hook**: [Why would a parent buy the set?]

## Recurring Characters
| Character | Role | Arc Across Series | First Appears |
|-----------|------|-------------------|---------------|
| Little Fox | Protagonist | Grows from fearful → confident | Book 1 |
| Owl | Mentor | Gradually reveals wisdom | Book 1 |
| Badger | Friend | Joins in Book 3, comic relief | Book 3 |

## World Rules
- **Setting**: The Whispery Woods (always the same forest)
- **Time**: Always bedtime/night (consistent mood)
- **Magic system**: [if any — keep consistent]
- **Geography**: Fox's den → River → Owl's tree → Meadow → Moon Hill

## Emotional Arc (Series-Level)
| Book | Theme | What Fox Learns |
|------|-------|-----------------|
| 1 | Asking for help | It's okay to not know the way |
| 2 | Making friends | Different is wonderful |
| 3 | Being brave | Courage is doing it scared |
| 4 | Sharing | The best things multiply |
| 5 | Letting go | Some friends move on |

## Series Branding
- **Cover template**: Same layout, different dominant color per book
- **Title format**: "[Animal]'s [Emotion] [Adventure/Night/etc.]"
- **Refrain**: Each book has its own refrain, but Book 1's refrain echoes in later books
- **Callback**: Each book references at least one moment from a previous book

## Series Continuity Checks
- [ ] Character appearances match across books (character bible)
- [ ] World rules are never contradicted
- [ ] No repeated plots or morals
- [ ] Callbacks are warm, not required (new readers can start anywhere)
- [ ] Difficulty/vocabulary increases slightly across the series
```

### Phase 2: Sequel Hook Insertion

Every book ending should include a subtle sequel hook IN ADDITION to the bedtime landing:

```markdown
## Sequel Hook Patterns

### Pattern A: New Character Tease
"As Fox curled up in her den, she thought she heard singing.
Far away, over the hill, someone new was humming a lullaby."

### Pattern B: Unfinished World
"Fox looked at the other side of the river.
'Tomorrow night,' she whispered. 'Tomorrow night I'll see what's there.'"

### Pattern C: Growth Acknowledgment
"Owl nodded. 'You found your way tonight, Little Fox.'
'But tomorrow,' Fox yawned, 'I want to find a NEW way.'
Owl's eyes sparkled. 'Oh, we will.'"
```

**Rules for sequel hooks:**
- Must come BEFORE the sleepy landing (not after)
- Must not create anxiety (gentle curiosity, not cliffhanger)
- Must work even if the reader never reads book 2

### Phase 3: Series Metadata

For each book in the series, generate:

```markdown
## KDP Series Metadata: "[Series Name]" — Book [N]

### Amazon Series Page
- Series title: "[Series Name]"
- Series position: [N] of [total planned]
- Description: "[series description — same for all books]"

### Book-Specific
- Title: "[Book Title]"
- Subtitle: "[Series Name] Book [N] — A Bedtime Story for Ages [X-X]"
- Description: "[150 words, book-specific, mentions series]"

### Keywords (7)
1. [series name] bedtime story
2. children's picture book [age]
3. [theme] stories for kids
4. bedtime story for [age]-year-olds
5. [character] book
6. read aloud picture book
7. [series name] book [N]

### Back Cover Cross-Sell
"Also in the [Series Name]:
📖 Book 1: [Title] — [one-line hook]
📖 Book 2: [Title] — [one-line hook]
📖 Book 3: [Title] — Coming soon!"

### A+ Content (Amazon Enhanced Brand Content)
- Series banner image (all covers in a row)
- Character introduction cards
- "Perfect for bedtime" lifestyle photo placeholder
- Reader quotes / reviews (add post-launch)
```

### Phase 4: Production Schedule

```markdown
## Series Production Calendar

| Week | Task | Output |
|------|------|--------|
| Week 1 | Series bible + Book 1 concept | series/[name]/SERIES_BIBLE.md |
| Week 1 | Book 1 pipeline (write→review→improve) | stories/book-1_v3_final.md |
| Week 2 | Book 1 illustrations | illustrations/book-1/ |
| Week 2 | Book 1 layout + export | output/book-1/ |
| Week 2 | Book 1 KDP upload | Published! |
| Week 3 | Book 2 pipeline | stories/book-2_v3_final.md |
| Week 3 | Book 2 illustrations | illustrations/book-2/ |
| ... | ... | ... |

Estimated: 1 book per week with overnight pipeline
Revenue ramp: $0 → $50/month → $200/month (at 5 books)
```

### Output: series/[series-slug]/

```
series/[series-slug]/
├── SERIES_BIBLE.md             ← Master document
├── characters/                 ← Shared character bibles
│   ├── fox/
│   ├── owl/
│   └── interactions/
├── world/
│   ├── geography.md
│   ├── rules.md
│   └── settings-palette.md
├── books/
│   ├── book-1/
│   │   ├── concept.md
│   │   ├── sequel-hook.md
│   │   └── kdp-metadata.md
│   ├── book-2/
│   │   └── ...
│   └── ...
├── branding/
│   ├── cover-template.md
│   ├── series-banner.md
│   └── color-per-book.md
└── SERIES_REPORT.md
```

## Key Rules

- **Character bible persists** — same characters must look identical across all books
- **World consistency** — geography and rules never contradict
- **No repeated morals** — each book teaches something new
- **Sequel hooks must be gentle** — curiosity, never anxiety
- **Book 1 stands alone** — readers should NOT need to read prior books
- **Reader graduation** — vocabulary and complexity grow slightly across series
- **Large file handling**: If Write fails, use Bash fallback
