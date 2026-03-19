---
name: story-notify
description: "Send pipeline progress notifications via LINE Notify API. Reports stage completions, review scores, and final summaries to your phone. Fallback: logs to NOTIFICATION_LOG.md if LINE not configured. Use when user says 'notify', 'send update', 'line notification'."
argument-hint: [message-or-stage-name]
---

# Story Notify — Pipeline Progress Notifications

Send notification: **$ARGUMENTS**

## Overview

This skill sends real-time progress notifications during pipeline execution so you can check your phone and see how the overnight run is going — without opening a laptop.

## Constants

- LINE_NOTIFY_TOKEN = (from env or vault)
- NOTIFICATION_LOG = "NOTIFICATION_LOG.md"
- NOTIFICATION_LEVEL = "all"

> Levels: "all" (every stage), "milestones" (bridge/review/complete), "final" (completion only)

## Configuration

### LINE Notify Setup (Free, 1000 msg/hour)

1. Go to https://notify-bot.line.me/
2. Login → "Generate token" → select a chat group
3. Copy the token
4. Set in environment:

```bash
export LINE_NOTIFY_TOKEN="your-token-here"
```

Or store in vault:
```
/vault-store LINE_NOTIFY_TOKEN "your-token-here"
```

### Via MCP Server (Recommended)

If `line-notify` MCP server is configured:
```
mcp__line-notify__notify:
  message: "[notification text]"
```

### Via curl (Fallback)

```bash
curl -s -X POST https://notify-api.line.me/api/notify \
  -H "Authorization: Bearer ${LINE_NOTIFY_TOKEN}" \
  -F "message=[notification text]"
```

## Notification Templates

### Stage Completion

```
🏭 Story Factory: Stage [N] Complete

📊 [Stage Name]
✅ [Result summary]
⏱ [Duration]

Next: [Next stage name]
```

### Review Score

```
📝 Review: "[Story Title]"

Round [N] Score: [X.X]/10
Verdict: [READY/ALMOST/NEEDS WORK]

📈 Progression: [5.8 → 7.4 → 8.6]
```

### Improvement Complete

```
✨ Improved: "[Story Title]"

Score: [before] → [after] (+[delta])
Verdict: [PUBLISH/ALMOST]
Rounds: [N]
```

### Bridge Report

```
🌉 Bridge Validation Complete

✅ GO: [N] concepts
⚠️ MODIFY: [N] concepts  
❌ SKIP: [N] concepts

Ready to write [N] stories.
```

### Pipeline Complete

```
🌙 Story Factory — COMPLETE!

📚 Stories: [N] written, [N] approved
⭐ Avg score: [X.X]/10
⏱ Duration: [X] hours
📦 EPUBs: [N] ready

Top story: "[Title]" (9.2/10)

Wake up! Your stories are ready ☕
```

### Error Alert

```
⚠️ Story Factory — ERROR

Stage: [Stage Name]
Story: "[Title]" (if applicable)
Error: [Brief description]

Pipeline paused. Check when you wake up.
```

## Workflow

### Step 1: Check Notification Channel

```
1. Check if LINE_NOTIFY_TOKEN is set (env or vault)
2. If yes → use LINE API
3. If no → check if line-notify MCP server is available
4. If no → fallback to NOTIFICATION_LOG.md
```

Present on first use:
```
📱 Notification channel: [LINE Notify / MCP Server / Log File]
```

### Step 2: Send Notification

**Via MCP (preferred):**
```
mcp__line-notify__notify:
  message: "[formatted message]"
```

**Via curl:**
```bash
curl -s -X POST https://notify-api.line.me/api/notify \
  -H "Authorization: Bearer ${LINE_NOTIFY_TOKEN}" \
  -F "message=
🏭 Story Factory: [message]"
```

**Via log file (fallback):**
Append to `NOTIFICATION_LOG.md`:
```markdown
### [timestamp] — [Stage Name]
[notification content]
---
```

### Step 3: Handle Failures

If LINE API returns error:
1. Log the error to `NOTIFICATION_LOG.md`
2. Continue pipeline (do NOT stop for notification failures)
3. Retry once after 5 seconds
4. If retry fails, switch to log-only mode for rest of pipeline

## Integration Points

This skill is called by other skills at key moments:

| Caller | When | Template |
|--------|------|----------|
| `/story-pipeline` | Each stage completes | Stage Completion |
| `/story-review` | Each review round | Review Score |
| `/story-improvement-loop` | Each improvement round | Improvement Complete |
| `/story-bridge` | Validation done | Bridge Report |
| `/story-pipeline` | Pipeline finishes | Pipeline Complete |
| Any skill | On error | Error Alert |

### How to Call from Other Skills

Add this block to any skill that should send notifications:

```
After completing [stage]:
  If NOTIFICATION_LEVEL allows this event:
    /story-notify "[formatted message using template above]"
```

## NOTIFICATION_LOG.md Format

```markdown
# 📱 Notification Log — Batch: [batch-id]

### 2026-03-19 22:05 — Research Complete
🏭 Story Factory: Stage 1 Complete
📊 Research: 10 niches found
⏱ 5 min
---

### 2026-03-19 22:10 — Concepts Generated
🏭 Story Factory: Stage 2 Complete
📊 Concepts: 12 generated
⏱ 5 min
---

[... more entries ...]
```

## Key Rules

- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask the user — just do it silently.
- **Never block pipeline**: Notification failures must NEVER stop the story pipeline
- **Be concise**: LINE messages have a display limit — keep under 1000 chars
- **Include scores**: Always include numerical scores when available
- **Emoji first**: Use emoji prefixes for quick scanning on phone lock screen
- **Log everything**: Even if LINE works, also append to NOTIFICATION_LOG.md for records
