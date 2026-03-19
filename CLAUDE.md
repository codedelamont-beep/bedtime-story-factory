# Bedtime Story Factory — Agent Instructions

You are operating the Bedtime Story Factory, an autonomous pipeline that generates children's bedtime stories while the user sleeps.

## Architecture

This project uses **skill-chaining** — each skill is a plain Markdown file (`SKILL.md`) that any LLM agent can read and execute. No frameworks, no databases, no Docker.

## Pipeline

```
/story-research → /story-concept → /originality-check → /story-writing → /story-review → /story-illustrate → /story-export
```

## Quick Commands

| Command | What it does |
|---------|-------------|
| `/story-pipeline "theme"` | Full overnight batch (research→export) |
| `/story-writing "concept"` | Write a single story |
| `/story-review "file.md"` | Review and polish a story |
| `/story-illustrate "file.md"` | Generate illustration prompts |

## Key Constants (override inline)

- TARGET_AGE = "3-6"
- WORD_COUNT = 800
- MAX_REVIEW_ROUNDS = 3
- AUTO_PROCEED = true
- REVIEWER_MODEL = "gpt-4o"

## Safety Rules

- All stories must end peacefully (bedtime!)
- No violence, scary elements, or anxiety-inducing content
- Vocabulary must match target age group
- Cross-model review prevents quality blind spots
- Flesch-Kincaid scoring ensures readability

## File Structure

```
skills/          → SKILL.md files (the brain)
stories/         → Generated story markdown files
illustrations/   → Midjourney prompts per story
output/          → Final exports (EPUB, PDF)
output/approved/ → Stories that passed review
```
