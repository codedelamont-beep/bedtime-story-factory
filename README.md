# 🌙 Bedtime Story Factory

> AI-powered children's bedtime story production factory. Runs overnight while you sleep — generates, reviews, illustrates, and exports publication-ready stories.

Built on [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)-inspired **skill-chain architecture** — every stage is a plain Markdown `SKILL.md` file. No frameworks, no databases, no Docker.

## ✨ What It Does

Before you sleep, run one command:

```bash
/story-pipeline "10 bedtime stories, ages 3-6, themes: forest animals, space, friendship"
```

Wake up with:
- 📖 10 polished stories with readability scores
- 🎨 Midjourney prompt sheets per scene
- 📱 EPUB/PDF exports ready for KDP publishing

## 🏗️ Pipeline Architecture

```
/story-research → /story-concept → /originality-check → /story-writing → /story-review → /story-illustrate → /story-export
   (trending)      (10 premises)    (dedup vs market)    (full story)     (age-check)     (MJ prompts)       (epub/pdf)
```

### ARIS → Story Factory Mapping

| ARIS Original | Story Factory Equivalent |
|---------------|--------------------------|
| `/research-lit` (survey papers) | `/story-research` — scrape trending kids' themes, KDP bestsellers |
| `/idea-creator` (brainstorm) | `/story-concept` — generate 10 story premises per niche |
| `/novelty-check` (prior work) | `/originality-check` — compare against existing popular titles |
| `/paper-writing` (narrative→PDF) | `/story-writing` — concept→outline→full story→EPUB/PDF |
| `auto-review-loop` (GPT reviews) | `/story-review` — age-appropriateness, emotional arc, vocabulary |
| `/paper-illustration` (diagrams) | `/story-illustrate` — Midjourney prompts per scene |

## 🛠️ Skills

Each skill lives in `skills/` as a standalone `SKILL.md`:

| Skill | Description |
|-------|-------------|
| `story-research` | Market research — trending themes, KDP niches, bestseller analysis |
| `story-concept` | Generate 8-12 story premises per niche with hooks |
| `originality-check` | Compare concepts against existing titles to avoid duplicates |
| `story-writing` | Full story generation — outline → draft → polish |
| `story-review` | Cross-model quality review — readability, age-check, emotional arc |
| `story-illustrate` | Generate Midjourney/image prompts for each scene |
| `story-export` | Format and export to EPUB, PDF, KDP-ready formats |
| `story-pipeline` | Orchestrator — chains all skills for overnight batch runs |

## 💰 Revenue Streams

- **Amazon KDP eBooks** — Publish 10-20 illustrated children's books/month
- **Midjourney illustration packs** — Sell prompt packs on Etsy/Gumroad
- **Story script licensing** — Bulk sales to teachers (Teachers Pay Teachers)
- **Audiobook pipeline** — Export to ElevenLabs TTS → Audible/ACX
- **Stock illustrations** — Submit AI art to Shutterstock/Adobe Stock

## 🚀 Quick Start

1. Clone this repo
2. Have Claude Code (or any SKILL.md-compatible agent) installed
3. Run: `/story-pipeline "5 bedtime stories, ages 3-6"`
4. Go to sleep 🌙
5. Wake up to finished stories ☀️

## 📋 Requirements

- Claude Code subscription (~$20/month) or any LLM agent that reads SKILL.md
- OpenRouter API key (for cross-model review — cheap/free tiers available)
- Midjourney account (optional — for illustration generation)

## 🔑 Key Constants

Override any constant inline: `/story-pipeline "topic" — word_count: 1200, target_age: 6-9`

| Constant | Default | Description |
|----------|---------|-------------|
| `MAX_ROUNDS` | 3 | Review iteration rounds |
| `TARGET_AGE` | "3-6" | Target age group |
| `WORD_COUNT` | 800 | Words per story |
| `OUTPUT_FORMAT` | "markdown, epub" | Export formats |
| `AUTO_PROCEED` | true | Run unattended overnight |
| `ILLUSTRATION_PROMPTS` | true | Generate Midjourney prompts |
| `REVIEWER_MODEL` | "gpt-4o" | Model for cross-review |

## 📄 License

MIT — See [LICENSE](LICENSE)

## 🙏 Credits

Inspired by [ARIS (Auto-Research-In-Sleep)](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) by wanshuiyin.
