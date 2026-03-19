# LINE Notify MCP Server

No external dependencies required. Uses Python stdlib only (urllib, json).

## Requirements

- Python 3.8+
- LINE Notify token (free at https://notify-bot.line.me/)

## Setup

```bash
export LINE_NOTIFY_TOKEN="your-token-here"
python3 mcp-servers/line-notify/server.py
```

## Claude Code Integration

Add to `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "line-notify": {
      "command": "/usr/bin/python3",
      "args": ["mcp-servers/line-notify/server.py"],
      "env": {
        "LINE_NOTIFY_TOKEN": "your-token-here"
      }
    }
  }
}
```
