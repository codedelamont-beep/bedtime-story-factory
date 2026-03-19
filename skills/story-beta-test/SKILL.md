---
name: story-beta-test
description: "Simulate beta reader feedback from multiple personas (parent, child, librarian, bookshop owner). Run after improvement loop and before character bible. Validates emotional impact, re-read desire, and purchase intent. Use when user says 'beta test', 'test readers', 'beta feedback', 'would kids like this'."
argument-hint: [story-file-path]
---

# Story Beta Test — Simulated Reader Feedback

Run beta test on: **$ARGUMENTS**

> **Context:** Professional publishers use beta readers before finalizing. This skill simulates that process using diverse LLM personas to catch blind spots that review/improvement missed — specifically: emotional resonance, purchase intent, and the "again! again!" factor.

## Constants

- PERSONAS = 5
- REVIEWER_MODEL = "gpt-4o"
- PASS_THRESHOLD = 4/5 personas recommend
- INPUT_VERSION = "v2_improved" or "v3_final"

## When to Run

```
/story-writing → /story-review → /story-improvement-loop
                                         ↓
                                  /story-beta-test ← YOU ARE HERE
                                         ↓
                              /story-character-bible → /story-illustrate → ...
```

Run AFTER improvement loop, BEFORE illustrations (no point illustrating a story that won't sell).

## Workflow

### Phase 1: Prepare Test Materials

Read the story file and extract:
1. Full story text (latest version)
2. Target age range
3. Character names and types
4. Theme/moral
5. Craft elements used (refrain, sound design, golden line)

### Phase 2: Persona Simulation

Send the story to REVIEWER_MODEL with 5 different personas. Each persona reads the COMPLETE story and gives structured feedback.

#### Persona 1: Tired Parent (Primary Buyer)

```
You are a tired parent of a [TARGET_AGE]-year-old child. It's 8pm, you've had
a long day at work, and your child wants a bedtime story. You picked up this
book at a bookshop.

Read this story as if reading it aloud to your child:

[Full story text]

Answer honestly:
1. Did you stumble on any sentences while reading? Which ones?
2. Did your voice naturally get softer toward the end?
3. Was there a line that made you smile despite being tired?
4. Would you read this again tomorrow night without dreading it?
5. Rate: How many times could you read this before going insane? (1-50+)
6. Would you buy another book by this author? YES/NO
7. What would you change? (One thing only)

Overall: RECOMMEND / MEH / RETURN
```

#### Persona 2: The Child (Target Reader)

```
You are a [TARGET_AGE]-year-old child being read this story at bedtime.
Think like a child — simple, honest, emotional.

[Full story text]

Answer in simple, childlike responses:
1. What was your favorite part?
2. Was there a scary part? What was it?
3. Did you want to say any of the words along with the grown-up?
4. What would you name the [main character] if you could?
5. Tell me what happened in the story (in your own words — max 3 sentences)
6. Do you want to hear it again? YES / MAYBE / NO
7. Would you like a stuffed animal of [character]? YES / NO

Overall: AGAIN! AGAIN! / OKAY / BORING
```

#### Persona 3: Children's Librarian (Quality Gatekeeper)

```
You are a children's librarian with 15 years of experience curating
bedtime story collections. You read 200+ children's books per year
and know what circulates vs what sits on the shelf.

[Full story text]

Professional assessment:
1. Would you add this to your bedtime story collection? Why?
2. What age range would you shelve this under?
3. How does this compare to current popular titles in this niche?
4. Does it work for read-aloud story time? (group setting)
5. Is the vocabulary level correct for the stated age range?
6. Are there any sensitivity concerns? (cultural, gender, disability representation)
7. What one change would make this circulate more?

Comparable titles: Name 2-3 published books this reminds you of.
Overall: ACQUIRE / CONSIDER / PASS
```

#### Persona 4: Bookshop Owner (Commercial Viability)

```
You are an independent children's bookshop owner. You need to decide
whether to stock this title. You see thousands of new releases.

[Full story text]

Commercial assessment:
1. Does the title grab attention on a shelf? Would you display face-out?
2. Would this sell as a gift? (grandparent buying for grandchild)
3. Is there series potential? (parents coming back for book 2)
4. What section would you shelve this in?
5. Price point: What would customers pay for this? ($X.99)
6. Would you hand-sell this to a customer asking for bedtime recommendations?
7. What's the one-sentence pitch you'd use?

Overall: STOCK / MAYBE / PASS
```

#### Persona 5: Developmental Editor (Craft Expert)

```
You are a developmental editor specializing in children's picture books.
You've edited 100+ published titles including award winners.

[Full story text]

Craft assessment:
1. Does the opening grab within the first spread?
2. Is the refrain earning its repetitions, or is it lazy?
3. Does the story earn the ending, or does it just... stop?
4. Is there a "turn" — a moment where the story surprises or deepens?
5. Show me the weakest paragraph and rewrite it in 2 sentences.
6. Show me the strongest paragraph and explain why it works.
7. Is this ready for illustration, or does the text still need work?

Overall: READY FOR ILLUSTRATION / ONE MORE PASS / SIGNIFICANT REWORK
```

### Phase 3: Aggregate Results

```markdown
## Beta Test Summary: "[Title]"

### Verdict Board

| Persona | Verdict | Key Signal |
|---------|---------|-----------|
| Tired Parent | RECOMMEND / MEH / RETURN | "Would read X more times" |
| Child (age X) | AGAIN! / OKAY / BORING | "Favorite part: [X]" |
| Librarian | ACQUIRE / CONSIDER / PASS | "Comparable to: [titles]" |
| Bookshop Owner | STOCK / MAYBE / PASS | "Would hand-sell: YES/NO" |
| Dev Editor | READY / ONE MORE / REWORK | "Strongest line: [X]" |

### Consensus: X/5 RECOMMEND → PASS / REVISE / FAIL

### Red Flags (unanimous or majority concerns)
- [Any issue raised by 3+ personas]

### Golden Signals (what everyone loved)
- [Any positive raised by 3+ personas]
```

### Phase 4: Decision Rules

| Result | Action |
|--------|--------|
| 5/5 recommend | → Proceed to character bible/illustration |
| 4/5 recommend | → Implement the 1 dissenter's top suggestion, proceed |
| 3/5 recommend | → Run one more improvement round targeting weak areas, re-test |
| ≤2/5 recommend | → Send back to improvement loop with all persona feedback |

### Phase 5: Revision Suggestions (if needed)

If score < 4/5, compile actionable fixes:

```markdown
## Required Revisions

### From Tired Parent:
- "[Specific sentence that caused stumble]" → rewrite for flow

### From Child:
- "[Part that was boring]" → add more action/sound/interaction

### From Librarian:
- "[Sensitivity concern]" → adjust language/representation

### From Bookshop Owner:
- "[Why it wouldn't sell]" → adjust hook/title/premise

### From Dev Editor:
- "[Weakest paragraph]" → "[their suggested rewrite]"
```

### Output: BETA_TEST_REPORT.md

```markdown
# Beta Test Report: "[Title]"

**Date**: [today]
**Version tested**: v2_improved / v3_final
**Personas**: 5
**Consensus**: X/5 RECOMMEND

## Full Persona Responses

### 1. Tired Parent
[Full response]

### 2. Child (age X)
[Full response]

### 3. Children's Librarian
[Full response]

### 4. Bookshop Owner
[Full response]

### 5. Developmental Editor
[Full response]

## Decision: PROCEED / REVISE / REWORK
## Required Revisions: [if any]
```

## Key Rules

- **Run AFTER improvement, BEFORE illustrations** — don't waste image generation on untested stories
- **All 5 personas must respond** — skip none
- **Be honest** — if the child persona says "boring", that's a signal
- **One revision only** — if beta test fails twice, the concept may be weak (send back to bridge)
- **Track re-test scores** — if a story needed revision, log both test results
- **Large file handling**: If Write fails, use Bash fallback
