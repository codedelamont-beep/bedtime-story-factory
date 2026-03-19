# 🌙 Bedtime Story Factory

> AI-powered children's bedtime story production pipeline. Runs overnight while you sleep — generates, reviews, polishes, illustrates, and exports publication-ready stories.

Built on [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)-inspired **skill-chain architecture** — every stage is a plain Markdown `SKILL.md` file. No frameworks, no databases, no Docker.

## ✨ What It Does

Before you sleep, run one command:

```bash
/story-pipeline "10 bedtime stories about magical forest animals"
```

Wake up with:
- 📖 10 polished stories with score progression (avg 9.2/10)
- 🎨 Midjourney prompt sheets per scene (8 scenes × 10 stories)
- 📱 EPUB + KDP metadata ready for publishing
- 📊 Full production report with quality analytics
- 📲 LINE notifications on your phone during the night

## 🏗️ Pipeline Architecture (8 Stages)

```
Stage 1   Stage 2   Stage 3     Stage 3.5   Stage 4   Stage 5    Stage 6    Stage 7    Stage 8
Research → Concept → Original → Bridge   → Write  → Review  → Improve → Illustrate → Export
  5min     5min      5min       5min      5min/ea  10min/ea   5min/ea   3min/ea     2min
```

**Typical overnight run (10 stories): ~4-5 hours → wake up ☕**

### Version Pipeline

```
v0_draft.md  →  v1_reviewed.md  →  v2_improved.md  →  v3_final.md
  (writing)       (structural)       (prose quality)      (approved)
  Score: 5-6      Score: 7-8         Score: 8-9          Score: 9+
```

## 🛠️ Skills (13 total)

| Skill | Workflow | Description |
|-------|----------|-------------|
| `story-research` | 1: Discovery | Market research — trending themes, KDP niches |
| `story-concept` | 1: Discovery | Generate 8-12 story premises with hooks |
| `originality-check` | 1: Discovery | Deduplicate against existing titles |
| `story-bridge` | 1.5: Bridge | Validate concepts (market, illustration, parent appeal) |
| `story-writing` | 2: Production | Full story generation with versioned output |
| `story-review` | 3a: Review | Cross-model quality review with human checkpoints |
| `story-review-llm` | 3a: Review | Review via cheap LLMs (DeepSeek, Qwen) |
| `story-improvement-loop` | 3b: Polish | 2-round craft-focused prose polishing |
| `story-illustrate` | 4: Output | Generate Midjourney prompts per scene |
| `story-export` | 4: Output | EPUB + KDP metadata export |
| `story-notify` | Throughout | LINE Notify push notifications |
| `story-analytics` | On-demand | Production dashboard and trends |
| `story-pipeline` | Orchestrator | Full overnight pipeline (all stages) |

## 🛡️ Reliability Features

| Feature | Description |
|---------|-------------|
| **Crash Recovery** | `PIPELINE_STATE.json` saves progress — resumes from last stage |
| **Idempotent Stages** | Checks output files before re-processing |
| **Error Isolation** | One story fails → skip it, continue batch |
| **Phone Notifications** | LINE Notify at each milestone |
| **Human Checkpoints** | Optional: pause for "go/skip/stop/custom" commands |
| **Score Progression** | Full tracking: v0→v1→v2 scores per criterion |

## 💰 Revenue Streams

- **Amazon KDP eBooks** — Publish 10-20 illustrated children's books/month
- **Midjourney illustration packs** — Sell prompt packs on Etsy/Gumroad
- **Story script licensing** — Bulk sales (Teachers Pay Teachers)
- **Audiobook pipeline** — Export to ElevenLabs TTS → Audible/ACX
- **Stock illustrations** — Submit AI art to Shutterstock/Adobe Stock

## 🚀 Quick Start

1. Clone this repo
2. Have Claude Code installed
3. Optional: configure MCP servers (see [docs/SETUP.md](docs/SETUP.md))
4. Run: `/story-pipeline "5 bedtime stories about friendly dragons"`
5. Go to sleep 🌙
6. Wake up to finished stories ☀️

## 📋 Requirements

| Requirement | Required? | Cost |
|------------|-----------|------|
| Claude Code subscription | Yes | ~$20/mo |
| LLM API key (review) | Optional | $0-0.02/batch (DeepSeek) |
| LINE Notify token | Optional | Free |
| Midjourney account | Optional | ~$10/mo |

## 🔑 Key Constants

Override any constant inline: `/story-pipeline "topic" — word_count: 1200, target_age: 6-9`

| Constant | Default | Description |
|----------|---------|-------------|
| `TARGET_AGE` | "3-6" | Target age group |
| `WORD_COUNT` | 800 | Words per story |
| `MAX_REVIEW_ROUNDS` | 3 | Review iteration limit |
| `MAX_STORIES` | 10 | Stories per batch |
| `AUTO_PROCEED` | true | Run unattended overnight |
| `HUMAN_CHECKPOINT` | false | Pause for user review |
| `REVIEWER_MODEL` | "gpt-4o" | Cross-review model |
| `NOTIFICATION_LEVEL` | "all" | all / milestones / final |

## 📖 Documentation

| Guide | Description |
|-------|-------------|
| [SETUP.md](docs/SETUP.md) | Zero to first batch in 10 minutes |
| [LLM_PROVIDERS.md](docs/LLM_PROVIDERS.md) | Model comparison, pricing, configurations |
| [WORKFLOW_DIAGRAM.md](docs/WORKFLOW_DIAGRAM.md) | Visual pipeline with Mermaid diagrams |
| [NARRATIVE_REPORT_EXAMPLE.md](docs/NARRATIVE_REPORT_EXAMPLE.md) | What a completed run looks like |

## 📄 License

MIT — See [LICENSE](LICENSE)

## 🙏 Credits

Inspired by [ARIS (Auto-Research-In-Sleep)](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) by wanshuiyin.
