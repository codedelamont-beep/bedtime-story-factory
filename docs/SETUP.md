# 🏭 Bedtime Story Factory — Setup Guide

Get from zero to your first batch of bedtime stories in under 10 minutes.

## Prerequisites

| Requirement | Required? | Notes |
|------------|-----------|-------|
| **Claude Code** | Yes | Subscription with `/slash-command` support |
| **GitHub account** | Yes | For cloning the repo |
| **OpenRouter API key** | Optional | For cross-model review (cheaper alternatives, see [LLM_PROVIDERS.md](./LLM_PROVIDERS.md)) |
| **LINE Notify token** | Optional | For phone notifications during overnight runs |

## Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/codedelamont-beep/bedtime-story-factory.git
cd bedtime-story-factory
```

### 2. Open in Claude Code

```bash
claude
```

Claude will automatically read `CLAUDE.md` and understand the project architecture.

### 3. Run your first story

```
/story-writing "A shy moon who learns to shine"
```

This generates a single story in `stories/` — takes about 2 minutes.

### 4. Run your first batch (overnight mode)

```
/story-pipeline "magical forest animals" — max_stories: 5
```

This runs the full 8-stage pipeline:

```
Research → Concepts → Originality → Bridge → Writing → Review → Improve → Illustrate → Export
```

For 5 stories, expect ~2 hours. For 10, ~4-5 hours. Perfect for overnight.

## MCP Server Configuration

### LLM Chat Server (Cross-Model Review)

Add to `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "llm-chat": {
      "command": "/usr/bin/python3",
      "args": ["mcp-servers/llm-chat/server.py"],
      "env": {
        "LLM_API_KEY": "your-openrouter-or-deepseek-key",
        "LLM_BASE_URL": "https://api.deepseek.com/v1",
        "LLM_MODEL": "deepseek-chat"
      }
    }
  }
}
```

### LINE Notify Server (Phone Notifications)

```json
{
  "mcpServers": {
    "line-notify": {
      "command": "/usr/bin/python3",
      "args": ["mcp-servers/line-notify/server.py"],
      "env": {
        "LINE_NOTIFY_TOKEN": "your-line-notify-token"
      }
    }
  }
}
```

Get your LINE token free at: https://notify-bot.line.me/

## Directory Structure

After your first run, you'll see:

```
bedtime-story-factory/
├── CLAUDE.md                    ← Agent instructions (read automatically)
├── skills/                      ← SKILL.md files (the brain)
│   ├── story-research/          ← Market research
│   ├── story-concept/           ← Concept generation
│   ├── originality-check/       ← Deduplication
│   ├── story-bridge/            ← Concept validation gate
│   ├── story-writing/           ← Full story generation
│   ├── story-review/            ← Cross-model review
│   ├── story-review-llm/        ← Review via cheap LLMs
│   ├── story-improvement-loop/  ← Prose polishing (2 rounds)
│   ├── story-illustrate/        ← Midjourney prompt generation
│   ├── story-export/            ← EPUB + KDP export
│   ├── story-notify/            ← LINE push notifications
│   └── story-pipeline/          ← Full overnight orchestrator
├── mcp-servers/
│   ├── llm-chat/                ← Cross-model review server
│   └── line-notify/             ← LINE Notify server
├── stories/                     ← Generated stories (versioned)
│   ├── brave-dragon_v0_draft.md
│   ├── brave-dragon_v1_reviewed.md
│   └── brave-dragon_v2_improved.md
├── illustrations/               ← Midjourney prompts per story
├── output/                      ← Final exports (EPUB, PDF)
│   └── approved/                ← Stories that passed review
└── docs/                        ← You are here
```

## Override Defaults

Every skill accepts inline overrides:

```
/story-pipeline "space adventures" — target_age: 6-9, word_count: 1200, max_stories: 3
/story-review "file.md" — human_checkpoint: true, reviewer_model: gpt-4o
/story-improvement-loop "file.md" — max_rounds: 3
```

## Overnight Checklist

Before going to bed:

1. ✅ Run `/story-pipeline "your theme"`
2. ✅ Verify first stage completes (Research — ~5 min)
3. ✅ Check LINE notification arrives on phone
4. ✅ Go to sleep 😴
5. ☕ Wake up to finished stories in `output/approved/`

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "MCP server not found" | Check `~/.claude/settings.json` paths are correct |
| "API key invalid" | Verify key in env or use `brain_vault_get` |
| Pipeline stuck | Check `PIPELINE_STATE.json` — delete to restart fresh |
| Review loops forever | Check `MAX_REVIEW_ROUNDS` (default: 3) |
| No LINE notification | Check `LINE_NOTIFY_TOKEN` is set, try `/story-notify "test"` |
| Large file write fails | Skills auto-retry with Bash fallback — this should self-heal |

## Next Steps

- 📖 [LLM Providers](./LLM_PROVIDERS.md) — choose the cheapest/best model for overnight runs
- 🔄 [Workflow Diagram](./WORKFLOW_DIAGRAM.md) — visual pipeline overview
- 📊 [Narrative Report Example](./NARRATIVE_REPORT_EXAMPLE.md) — what a completed run looks like
