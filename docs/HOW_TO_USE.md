# 📋 How to Use — Bedtime Story Factory

> **Copy-paste each prompt below into Antigravity (or any AI agent).**
> Replace `[THEME]` with your theme once. Replace `[SLUG]` with the filename from the previous stage.
>
> **Project path:** `active/content-tools/bedtime-story-factory`

---

## How It Works

The factory is **18 skill files** (SKILL.md). You paste a prompt → the AI reads the skill → it does the work → files appear in your project.

**No installation. No setup. No code to run.** Just copy-paste prompts.

```
You (paste prompt) → AI reads SKILL.md + CRAFT_GUIDE.md → Output files created
```

---

## Before You Start — Pick a Theme

Examples:
- "forest animals who help each other at bedtime"
- "a little cloud who doesn't know how to rain"
- "ocean creatures learning to sleep"
- "space adventures with a sleepy astronaut"

---

## Quick Start Options

| What you want | Which stages |
|--------------|-------------|
| **1 story, fast (5 min)** | Stage 4 only |
| **1 polished story (20 min)** | Stage 4 → 5 → 6 |
| **Full publishable book** | All stages 1 → 10 |
| **Book series (5 books)** | Stages 1 → 11 |
| **Track sales after publish** | Post-publish stage |

---

## Stage 1: Market Research

**Time:** ~5 min | **Output:** `RESEARCH_REPORT.md`

```
Read the skill file at:
active/content-tools/bedtime-story-factory/skills/story-research/SKILL.md

Execute the story-research skill for this theme: "[THEME]"

Working directory:
active/content-tools/bedtime-story-factory

Follow ALL phases in the skill:
- Phase 1: Scrape Amazon KDP trending themes and bestsellers
- Phase 2: Niche ranking (profitability, competition, demand)
- Phase 3: Competitor craft analysis (analyze WHY top 3 books
  sell — their specific craft techniques)

Save output to: RESEARCH_REPORT.md in the working directory.
Include the competitor craft analysis with the
"steal this / beat this / avoid this" framework.
```

---

## Stage 2: Generate Concepts

**Time:** ~5 min | **Output:** `CONCEPT_REPORT.md`

```
Read the skill file at:
active/content-tools/bedtime-story-factory/skills/story-concept/SKILL.md

Execute the story-concept skill using the research from:
active/content-tools/bedtime-story-factory/RESEARCH_REPORT.md

Generate 8-12 unique bedtime story concepts. For each, include:
1. Title, theme, target age, synopsis
2. Main character with 5-word hook
3. Moral/lesson (never stated explicitly in the story)
4. CRAFT FEASIBILITY SCORES (1-5 each):
   refrain potential, sound design richness, rhythm compatibility,
   character distinctiveness, golden line potential
5. MARKET VIABILITY SCORES from the research data

Rank concepts by COMBINED score (craft 60%, market 40%).
Apply the 5-word character test — reject any character
a 4-year-old wouldn't remember.

Save output to: CONCEPT_REPORT.md in the working directory.
```

---

## Stage 3: Originality Check

**Time:** ~5 min | **Output:** `ORIGINALITY_REPORT.md`

```
Read the skill file at:
active/content-tools/bedtime-story-factory/skills/originality-check/SKILL.md

Execute the originality-check skill on all concepts in:
active/content-tools/bedtime-story-factory/CONCEPT_REPORT.md

For each concept:
1. Search Amazon KDP for similar titles
2. Search Google for similar story premises
3. Check if character is too close to existing popular characters
   (Pigeon, Llama Llama, Corduroy, etc.)
4. Mark as: ORIGINAL ✅ / SIMILAR ⚠️ / DUPLICATE ❌

Save output to: ORIGINALITY_REPORT.md in the working directory.
Replace any DUPLICATE concepts with fresh alternatives.
```

---

## Stage 3.5: Bridge Validation

**Time:** ~5 min | **Output:** `BRIDGE_REPORT.md`

```
Read the skill file at:
active/content-tools/bedtime-story-factory/skills/story-bridge/SKILL.md

Execute the story-bridge skill using:
- CONCEPT_REPORT.md
- ORIGINALITY_REPORT.md

Both in: active/content-tools/bedtime-story-factory/

For each concept that passed originality:
1. Market viability scoring (competition, demand, price point, series potential)
2. Illustration feasibility (can scenes be drawn consistently?)
3. Cross-model "would you buy this?" parent test
4. Aggregate: Viability = (Market × 0.3) + (Illustration × 0.2) + (Parent Appeal × 0.5)

Decision: GO ✅ (≥7) / MODIFY ⚠️ (5-6) / SKIP ❌ (<5)

Save output to: BRIDGE_REPORT.md
List approved concepts in order, ready for writing.
```

---

## 🔴 DECISION POINT

Review `BRIDGE_REPORT.md`. Pick which GO concept to write first.

---

## Stage 4: Write the Story

**Time:** ~5 min | **Output:** `stories/[slug]_v0_draft.md`

```
Read these files first (MANDATORY before writing):
1. active/content-tools/bedtime-story-factory/references/CRAFT_GUIDE.md
2. active/content-tools/bedtime-story-factory/skills/story-writing/SKILL.md

Execute the story-writing skill for: "[TITLE OF CHOSEN CONCEPT]"

Using the concept details from:
active/content-tools/bedtime-story-factory/BRIDGE_REPORT.md

Follow ALL phases from the skill:
- Phase 1: Character design (5-word hook, visual quirk, voice, contradiction)
- Phase 2: 14-spread outline (with page-turn hooks per spread)
- Phase 3: Full draft applying ALL craft techniques:
  • Trochaic rhythm pattern
  • Refrain appearing 3-5 times
  • 5+ onomatopoeia, 3+ alliterative phrases, 8+ mouth-feel words
  • Zero "she felt [emotion]" — show-don't-tell only
  • Page-turn anticipation at every spread
  • Wind-down descent in final 3 spreads
  • One golden line (whisper-worthy)
  • Humor layer (child + parent levels)
- Phase 4: Read-aloud verification pass
- Phase 5: Quality checklist

WORD_COUNT = 800, TARGET_AGE = "3-6", SPREAD_COUNT = 14

Save to: stories/[title-slug]_v0_draft.md
Include full frontmatter (refrain, golden_line, sound_word_count).
Use <!-- SPREAD N: [visual description] --> markers.
```

> 💡 **Shortcut:** To write a story without research, skip stages 1-3.5.
> Replace `BRIDGE_REPORT.md` with your own concept in the prompt.

---

## Stage 5: Review

**Time:** ~10 min | **Output:** `stories/[slug]_v1_reviewed.md`

```
Read these files:
1. active/content-tools/bedtime-story-factory/skills/story-review/SKILL.md
2. active/content-tools/bedtime-story-factory/references/CRAFT_GUIDE.md

Execute the story-review skill on:
active/content-tools/bedtime-story-factory/stories/[SLUG]_v0_draft.md

Review using 10 CRAFT CRITERIA (1-10 each):
1. Read-aloud rhythm
2. Sound design (onomatopoeia, alliteration, mouth-feel)
3. Refrain strength
4. Show-don't-tell
5. Page-turn anticipation
6. Character distinctiveness
7. Re-read gravity ("again!" factor)
8. Visual filmability
9. Wind-down quality (final 3 spreads)
10. Golden line

Plus SAFETY GATE: no violence, age-appropriate vocab,
peaceful ending, no anxiety themes.

For each fix: quote current text AND provide replacement.
Implement all fixes.

Save reviewed story to: stories/[SLUG]_v1_reviewed.md
Save review to: STORY_REVIEW.md
Update: SCORE_TRACKER.md
```

---

## Stage 6: Improvement Loop

**Time:** ~5 min | **Output:** `stories/[slug]_v2_improved.md`

```
Read these files:
1. active/content-tools/bedtime-story-factory/skills/story-improvement-loop/SKILL.md
2. active/content-tools/bedtime-story-factory/references/CRAFT_GUIDE.md

Execute the improvement loop on:
active/content-tools/bedtime-story-factory/stories/[SLUG]_v1_reviewed.md

Run 2 rounds of craft-focused improvement using the same 10 criteria.
Round 1: Fix the bottom 3 scoring criteria
Round 2: Polish overall rhythm, sound design, refrain power

Skip if story already scored ≥ 9/10 overall (diminishing returns).

Save to: stories/[SLUG]_v2_improved.md
Update: SCORE_TRACKER.md with improvement scores and Δ column
```

---

## Stage 6.5: Beta Test

**Time:** ~3 min | **Output:** `BETA_TEST_REPORT.md`

```
Read the skill file at:
active/content-tools/bedtime-story-factory/skills/story-beta-test/SKILL.md

Execute beta test on:
active/content-tools/bedtime-story-factory/stories/[SLUG]_v2_improved.md

Simulate 5 reader personas:
1. 😴 Tired Parent — reading at 8pm for the 47th time
2. 👶 Child at target age — would they say "again!"?
3. 📚 Public Librarian — shelf-worthy? how does it compare to classics?
4. 🏪 Bookshop Owner — would this sell? gift potential?
5. 📝 Developmental Editor — craft quality? what to cut/add?

Each persona gives:
- Overall impression (1-2 sentences)
- RECOMMEND / HESITATE / PASS verdict
- Strongest moment (quote it)
- Weakest moment (quote it + fix)
- One specific revision suggestion

CONSENSUS:
- 4-5 recommend → PROCEED ✅
- 3 recommend → one more improvement round
- ≤2 recommend → back to Stage 6 ❌

Save to: BETA_TEST_REPORT.md
```

---

## 🔴 DECISION POINT

Beta test passed (4+ recommend) → continue to Stage 7.
If not → go back to Stage 6 with the feedback.

---

## Stage 7: Character Bible

**Time:** ~10 min | **Output:** `characters/[slug]/` folder

```
Read the skill file at:
active/content-tools/bedtime-story-factory/skills/story-character-bible/SKILL.md

Execute for:
active/content-tools/bedtime-story-factory/stories/[SLUG]_v2_improved.md

For EACH character in the story, create:
1. Visual design doc (species, hex colors, proportions, features)
2. Style Lock Prompt Fragment (exact text for EVERY image prompt)
3. Expression sheet (5 emotions: neutral, curious, scared, joyful, sleepy)
4. Pose sheet (5 poses: standing, walking, sitting, curled, with others)
5. Color palette with exact hex values

For multi-character stories: scale reference + together poses.
For settings: world design with mood progression:
  Spreads 1-4: cool blues → uncertainty
  Spreads 5-8: warmer tones → hope
  Spreads 9-12: warm golden → comfort
  Spreads 13-14: soft amber → sleep

Generate 3 anchor image prompts per character.

Save to: characters/[SLUG]/ with design.md, style-lock.txt,
anchor-reference.txt per character + world/settings.md
```

---

## Stage 8: Illustrations

**Time:** ~5 min per spread | **Output:** `illustrations/[slug]/` folder

```
Read the skill file at:
active/content-tools/bedtime-story-factory/skills/story-illustrate/SKILL.md

Execute for:
active/content-tools/bedtime-story-factory/stories/[SLUG]_v2_improved.md

Load character bible from:
active/content-tools/bedtime-story-factory/characters/[SLUG]/

For each of 14 spreads + 1 cover (15 images):
1. Scene analysis (characters, action, setting, mood, composition)
2. Prompt using Style Lock Fragment + scene + mood colors
3. Include exact hex codes from character bible
4. Always add "no text, no typography, no words, no letters"

Model selection (see skill for full guide):
- FLUX 1.1 Pro ⭐ recommended (best character consistency)
- Ideogram (for scenes with readable text/signs)
- DALL-E 3 (quick prototyping)
- Midjourney v6 (artistic quality, use --cref for consistency)

QC per image (11 checks including eye focus + finger count).

Post-processing:
- Upscale to 2550×2550px at 300dpi
- DALL-E: Real-ESRGAN 4x upscale required
- FLUX: minor upscale from 2048 native

Save to: illustrations/[SLUG]/ with spreads/ and prompts/ folders.
```

> ⚠️ **Without API keys:** I create all prompts + QC specs.
> You generate images manually, then I QC them.

---

## Stage 9: Layout

**Time:** ~5 min | **Output:** `output/[slug]/` folder

```
Read the skill file at:
active/content-tools/bedtime-story-factory/skills/story-layout/SKILL.md

Execute for:
active/content-tools/bedtime-story-factory/stories/[SLUG]_v2_improved.md

Using illustrations from:
active/content-tools/bedtime-story-factory/illustrations/[SLUG]/

Specs:
- TRIM: 8.5×8.5" square
- BLEED: 0.125" all sides (total 8.75×8.75")
- PAGES: 32
- DPI: 300
- FONT: Andika (ages 2-5) or Georgia (ages 4-6+)
- FONT_SIZE: 16pt, LINE_HEIGHT: 1.8

Create:
1. Spread mapping (story text → 32 pages)
2. Text placement per spread (full-bleed / split / text-on-color)
3. HTML page per spread (exact KDP dimensions)
4. Title page, copyright (with AI disclosure), dedication, back matter
5. Cover wrap: front (8.75") + spine (0.072") + back (8.75")

Save to: output/[SLUG]/ with interior/, cover/, LAYOUT_REPORT.md
```

---

## Stage 10: KDP Export

**Time:** ~2 min | **Output:** `output/[slug]/` complete package

```
Read the skill file at:
active/content-tools/bedtime-story-factory/skills/story-export/SKILL.md

Execute for:
active/content-tools/bedtime-story-factory/output/[SLUG]/

Generate:
1. KDP metadata JSON (title, 7 keywords, 2 BISAC categories, pricing)
2. Book description (A+ optimized HTML, golden line as hook)
3. A+ Content plan (hero banner, character cards, comparison chart)
4. Copyright page with AI disclosure (MANDATORY since 2023)
5. Pricing strategy:
   - Book 1 ebook: $0.99 (loss leader)
   - Book 2+ ebook: $2.99
   - Paperback: $12.99
6. Pre-upload QC checklist (15 items)

Save to: output/[SLUG]/ with metadata/, marketing/, legal/ folders.
Save summary to: EXPORT_REPORT.md
```

---

## Stage 11: Series Setup (Optional)

**Time:** ~5 min | **Output:** `series/[slug]/` folder

```
Read the skill file at:
active/content-tools/bedtime-story-factory/skills/story-series/SKILL.md

Execute for: "[YOUR SERIES NAME]"

Working directory:
active/content-tools/bedtime-story-factory

Create:
1. Series bible (logline, characters, world rules, arc per book)
2. Plan 5 books with unique themes (no repeated morals)
3. Sequel hooks (gentle curiosity, never cliffhangers)
4. Branding (cover template, title format, callbacks)
5. KDP series metadata + cross-sell back cover
6. Production calendar (1 book per week)

Save to: series/[series-slug]/ with SERIES_BIBLE.md
```

---

## Post-Publish: Market Monitoring

**Time:** ~5 min | **Output:** `monitoring/` folder

```
Read the skill file at:
active/content-tools/bedtime-story-factory/skills/story-market-monitor/SKILL.md

Execute for: "[YOUR BOOK TITLE]"

Working directory:
active/content-tools/bedtime-story-factory

Set up:
1. Performance snapshot template (sales, KENP, rankings)
2. Review intelligence (extract craft feedback from parent quotes)
3. Read-through analysis for series
4. A/B test plan for description (14-day minimum)
5. Pricing experiment design
6. Competitor monitoring

Save to: monitoring/ with MARKET_MONITOR.md and experiment logs.
```

---

## Pipeline at a Glance

```
Stage 1     Stage 2      Stage 3         Stage 3.5
Research → Concepts → Originality →   Bridge     →
(5 min)    (5 min)    (5 min)       (5 min)

Stage 4         Stage 5        Stage 6       Stage 6.5
Write Each  → Review Each → Improve Each → Beta Test →
(5 min each)  (10 min each)  (5 min each)  (3 min each)

Stage 7          Stage 8              Stage 9        Stage 10
Char Bible  →  Illustrate Each  →  Layout Each  → Export All
(10 min)       (5 min each)       (5 min each)    (2 min)
```

**Total for 1 story (research to export): ~1 hour**
**Total for 10 stories: ~7-8 hours (perfect for overnight)**

---

## File Structure After a Full Run

```
bedtime-story-factory/
├── RESEARCH_REPORT.md           ← Stage 1 output
├── CONCEPT_REPORT.md            ← Stage 2 output
├── ORIGINALITY_REPORT.md        ← Stage 3 output
├── BRIDGE_REPORT.md             ← Stage 3.5 output
├── STORY_REVIEW.md              ← Stage 5 review records
├── SCORE_TRACKER.md             ← Quality scores across all stories
├── BETA_TEST_REPORT.md          ← Stage 6.5 reader feedback
├── EXPORT_REPORT.md             ← Stage 10 summary
├── stories/                     ← Your stories (versioned)
│   ├── tiny-dragon_v0_draft.md
│   ├── tiny-dragon_v1_reviewed.md
│   └── tiny-dragon_v2_improved.md
├── characters/                  ← Character bibles + style locks
│   └── tiny-dragon/
├── illustrations/               ← Generated images + prompts
│   └── tiny-dragon/
├── output/                      ← Final book packages
│   └── tiny-dragon/
│       ├── interior/
│       ├── pdf/
│       ├── epub/
│       ├── metadata/
│       ├── marketing/
│       └── legal/
├── series/                      ← Series bibles (if applicable)
└── monitoring/                  ← Post-publish tracking
```

---

## Tips

1. **Start with Stage 4** if you already have a story idea — skip research
2. **The craft guide is everything** — it's what makes our stories better than AI slop
3. **Don't skip Stages 5-6.5** — review + improve + beta test = quality guarantee
4. **One stage per chat** works best — files persist on disk between chats
5. **Override defaults** — add "target age 6-9" or "word count 1200" to any prompt
6. **Version files never overwrite** — v0 → v1 → v2 → v3, always safe
