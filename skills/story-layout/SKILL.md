---
name: story-layout
description: "Create print-ready book layout with text-on-image placement per spread. Generates fixed-layout EPUB and print-ready PDF with correct bleed, margins, and spine for KDP. Use when user says 'layout', 'book layout', 'format for print', 'create pdf'."
argument-hint: [story-file-path]
---

# Story Layout — Print-Ready Book Production

Create print-ready layout for: **$ARGUMENTS**

> **PREREQUISITES:**
> - Story must be at v2 or v3 (post-improvement)
> - Illustrations must exist in `illustrations/[slug]/spreads/`
> - Character bible in `characters/[slug]/`

## Constants

- TRIM_SIZE = "8.5x8.5" (inches, square — most popular KDP children's format)
- BLEED = 0.125 (inches, all sides)
- MARGIN_INNER = 0.5 (inches, gutter side)
- MARGIN_OUTER = 0.375 (inches)
- MARGIN_TOP = 0.375 (inches)
- MARGIN_BOTTOM = 0.5 (inches)
- DPI = 300
- COLOR_PROFILE = "sRGB" (KDP accepts sRGB for paperback interior)
- PAGES = 32 (standard picture book)
- FONT_BODY = "Andika" (default — designed for early literacy)
- FONT_SIZE = 16pt (14pt minimum for print readability)
- LINE_HEIGHT = 1.8

## Typography Guide

Children's book fonts must have: large x-height, clear letterforms, distinct 'a'/'o'/'e', and feel warm — NOT clinical.

| Font | Style | Best For | Free? |
|------|-------|----------|-------|
| **Andika** ⭐ | Sans-serif, early literacy | Ages 2-5 (best legibility for new readers) | ✅ Google Fonts |
| **Georgia** | Serif, elegant | Ages 4-6 (warm, traditional feel) | ✅ System font |
| **Sassoon Primary** | Sans-serif, handwritten feel | Ages 2-4 (matches how children learn letters) | ❌ Paid |
| **Century Schoolbook** | Serif, textbook classic | Ages 5-7 (slightly older, classic picture book) | ✅ System font |
| **Quicksand** | Sans-serif, rounded | Ages 2-5 (modern, friendly, great for whimsy) | ✅ Google Fonts |

**Rules:**
- **14pt minimum** for body text in print (smaller = parents squint in dim bedtime light)
- **16pt recommended** for ages 2-4
- Never use more than 2 fonts per book (body + title/display)
- Title font can be more expressive (handwritten, decorative), body must be readable
- Line height ≥ 1.8 for young readers (generous spacing aids tracking)
- Dark text on light background ONLY (avoid light text on dark — hard to read by lamplight)

## KDP Specifications

### Page Structure (32 Pages)

```
Page 1:   [blank or half-title]
Page 2:   [blank or publisher info]
Page 3:   Title page (title, author, illustrator)
Page 4:   Copyright page + dedication
Pages 5-32: Story spreads (14 spreads × 2 pages = 28 pages)
Page 32:  Back matter (about author / "also by" / QR code)
```

### Trim Size Details (8.5×8.5 Square)

```
Trim:   8.5" × 8.5"
Bleed:  8.75" × 8.75" (with 0.125" bleed on all sides)
Pixels: 2625 × 2625 at 300dpi (bleed included)
Safe zone: 8.0" × 7.75" (keep important text/images within)
```

### Cover Specifications

```
Front cover:  8.75" × 8.75" (with bleed)
Spine width:  0.002252" × page count (32 pages ≈ 0.072" for white paper)
Back cover:   8.75" × 8.75" (with bleed)
Full wrap:    17.572" × 8.75" (front + spine + back)
Pixels:       5272 × 2625 at 300dpi
```

## Workflow

### Phase 1: Story-to-Spread Mapping

Map the story text to specific pages:

```markdown
## Spread Mapping: "[Title]"

| Spread | Pages | Story Section | Text Length | Illustration |
|--------|-------|---------------|-------------|-------------|
| — | 1-2 | Half-title + blank | — | Decorative |
| — | 3-4 | Title + copyright | — | Title illustration |
| 1 | 5-6 | Opening paragraph | 35 words | spread-01.png |
| 2 | 7-8 | Fox discovers... | 45 words | spread-02.png |
| ... | ... | ... | ... | ... |
| 14 | 31-32 | Goodnight | 20 words | spread-14.png |
```

### Phase 2: Text Placement Design

For each spread, determine where text goes relative to the illustration:

```markdown
## Text Placement: Spread [N]

### Layout Type: [full-bleed / split / text-block]

#### Option A: Full-Bleed Illustration + Text Overlay
- Image: fills entire spread (bleeds off all edges)
- Text position: [top-left / bottom-center / right-third]
- Text background: semi-transparent white box (opacity 0.85)
- Font: Georgia 16pt, line-height 1.8
- Text color: #2C1810 (dark brown)

#### Option B: Split Layout (Left Text, Right Image)
- Left page: text only on cream background (#FEF9F0)
- Right page: full-bleed illustration
- Text: centered vertically, left-aligned

#### Option C: Text Block on Color Field
- Image: placed at top or bottom half
- Text: on solid color field matching scene palette
- Color: [hex from character bible world design]
```

### Phase 3: Generate HTML Pages

Create an HTML file for each spread (for PDF conversion):

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    @page {
      size: 8.75in 8.75in; /* with bleed */
      margin: 0;
    }
    body {
      margin: 0;
      padding: 0;
      width: 8.75in;
      height: 8.75in;
    }
    .spread {
      position: relative;
      width: 100%;
      height: 100%;
    }
    .illustration {
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      object-fit: cover;
    }
    .text-overlay {
      position: absolute;
      bottom: 0.75in;
      left: 0.625in;
      right: 0.625in;
      background: rgba(255, 255, 255, 0.88);
      padding: 0.25in 0.375in;
      border-radius: 8px;
      font-family: Georgia, serif;
      font-size: 16pt;
      line-height: 1.8;
      color: #2C1810;
    }
  </style>
</head>
<body>
  <div class="spread">
    <img class="illustration" src="spread-01.png" alt="Scene 1">
    <div class="text-overlay">
      <p>Little Fox stood very still. The trees looked different in the dark.</p>
    </div>
  </div>
</body>
</html>
```

### Phase 4: Title Page & Front/Back Matter

Generate formatted pages for:

1. **Half-Title** (page 1): Just the title, large, centered
2. **Title Page** (page 3): Title, author, illustrator, small illustration
3. **Copyright** (page 4): © notice, AI disclosure, ISBN, age range
4. **Dedication** (page 4): "For all the little ones who aren't quite ready for sleep"
5. **Back Matter** (page 32): About the author, QR code to series page, "also by"

### Phase 5: Cover Assembly

```markdown
## Cover Layout

### Front Cover (8.75" × 8.75")
- Full-bleed key illustration from story
- Title: [font, size, position, color]
- Author: [font, size, position]
- Age badge: "Ages 3-6" rounded pill, bottom-right

### Spine (0.072" wide)
- Title: vertical text, 6pt minimum
- Author: vertical text below title

### Back Cover (8.75" × 8.75")
- Solid color from palette, 80% opacity
- 150-word description (center-aligned)
- Barcode placeholder (bottom-right, 2" × 1.5")
- Age range badge
- Price: "$X.99"
- "Also available in this series:" [if applicable]
```

### Phase 6: PDF Generation

```bash
# Interior PDF (using wkhtmltopdf or Chrome headless)
for page in pages/*.html; do
  wkhtmltopdf --page-width 8.75in --page-height 8.75in \
    --dpi 300 --no-margins "$page" "pdf/$(basename $page .html).pdf"
done

# Merge into single PDF
pdfunite pdf/page-*.pdf output/[slug]-interior.pdf

# Cover PDF (single page wrap)
wkhtmltopdf --page-width 17.572in --page-height 8.75in \
  --dpi 300 --no-margins cover/wrap.html output/[slug]-cover.pdf
```

### Phase 7: Fixed-Layout EPUB (for Kindle)

For Kindle picture books, create fixed-layout EPUB (not reflowable):

```xml
<!-- content.opf additions for fixed layout -->
<meta property="rendition:layout">pre-paginated</meta>
<meta property="rendition:orientation">landscape</meta>
<meta property="rendition:spread">none</meta>
```

Each page is a fixed-size HTML page with embedded images.

### Output: output/[slug]/

```
output/[slug]/
├── interior/
│   ├── page-01.html          ← HTML per page
│   ├── page-02.html
│   ├── ...
│   └── page-32.html
├── pdf/
│   ├── [slug]-interior.pdf   ← Print-ready interior (300dpi, bleed)
│   └── [slug]-cover.pdf      ← Print-ready cover wrap
├── epub/
│   └── [slug].epub           ← Fixed-layout EPUB for Kindle
├── cover/
│   ├── front.png             ← Front cover image
│   ├── back.png              ← Back cover image
│   └── wrap.png              ← Full cover wrap (front + spine + back)
├── LAYOUT_REPORT.md          ← Summary, QC results
└── [slug]-kdp-upload.json    ← KDP metadata ready for upload
```

## Key Rules

- **Fixed layout only** — picture books are NOT reflowable (never use standard EPUB)
- **Bleed is mandatory** — 0.125" on all sides for print
- **Safe zone** — keep all important content 0.25" from trim edge
- **300dpi minimum** — check every image before including
- **Text readability** — minimum 14pt on print, high contrast against background
- **KDP AI disclosure** — include in copyright page (mandatory since 2023)
- **Large file handling**: If Write fails, use Bash fallback
