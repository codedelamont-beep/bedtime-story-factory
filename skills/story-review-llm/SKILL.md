---
name: story-review-llm
description: "Autonomous story review loop using any OpenAI-compatible LLM API. Works with DeepSeek, MiniMax, Kimi, or any provider. Use for cheap/free overnight review runs."
argument-hint: [story-file-path]
---

# Story Review (Generic LLM) — Autonomous Quality Loop

Review and improve: **$ARGUMENTS**

## Constants

- MAX_ROUNDS = 3
- POSITIVE_THRESHOLD = 8/10
- REVIEW_DOC = "STORY_REVIEW.md"

## LLM Configuration

This skill uses **any OpenAI-compatible API** via the `llm-chat` MCP server or curl fallback.

### Via MCP Server (Recommended)

Add to `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "llm-chat": {
      "command": "/usr/bin/python3",
      "args": ["mcp-servers/llm-chat/server.py"],
      "env": {
        "LLM_API_KEY": "your-api-key",
        "LLM_BASE_URL": "https://api.deepseek.com/v1",
        "LLM_MODEL": "deepseek-chat"
      }
    }
  }
}
```

### Supported Providers (Cheapest First)

| Provider | Base URL | Model | Cost |
|----------|----------|-------|------|
| **DeepSeek** | `https://api.deepseek.com/v1` | `deepseek-chat` | ~Free tier |
| **ModelScope** | `https://api-inference.modelscope.cn/v1` | `Qwen/Qwen2.5-72B` | 2000 free/day |
| **Kimi** | `https://api.moonshot.cn/v1` | `moonshot-v1-8k` | Free tier |
| **OpenRouter** | `https://openrouter.ai/api/v1` | `deepseek/deepseek-chat` | Pay-per-use |
| **OpenAI** | `https://api.openai.com/v1` | `gpt-4o` | $$ |

## Review Loop

### Phase A: Send to Reviewer

**If MCP available:**
```
mcp__llm-chat__chat:
  system: "You are a children's book editor specializing in bedtime stories."
  prompt: |
    Review this bedtime story for ages [TARGET_AGE].

    [Full story text]

    Score 1-10 on each:
    1. Age-appropriateness (vocabulary, concepts)
    2. Emotional arc (winds down to sleepy?)
    3. Readability (sentence length, complexity)
    4. Engagement (would a child ask again?)
    5. Moral clarity (lesson present, not preachy?)
    6. Illustration potential (clear visual scenes?)
    7. Parent appeal (enjoy reading aloud?)
    8. Bedtime suitability (calming, not stimulating?)

    Overall score: X/10
    Verdict: READY / ALMOST / NEEDS WORK
    Specific fixes (ranked by impact):
```

**If MCP NOT available (curl fallback):**
```bash
curl -s "${LLM_BASE_URL}/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${LLM_API_KEY}" \
  -d '{
    "model": "'${LLM_MODEL}'",
    "messages": [
      {"role": "system", "content": "You are a children's book editor..."},
      {"role": "user", "content": "[review prompt]"}
    ],
    "max_tokens": 4096
  }'
```

### Phase B: Parse & Decide

- Score >= 8 AND "READY" → STOP, approved
- Score 6-7 AND "ALMOST" → implement fixes, re-review
- Score < 6 → significant rewrite

### Phase C: Implement Fixes

Priority order:
1. Vocabulary swaps (replace hard words)
2. Pacing adjustments (slow down ending)
3. Emotional arc fixes
4. Sentence restructuring
5. Moral integration

### Phase D: Document Round

Append to `STORY_REVIEW.md` with scores, fixes, raw response.

Update `REVIEW_STATE.json` with current state.

### Termination

Set `REVIEW_STATE.json` status to `"completed"`. Move approved stories to `output/approved/`.

## Key Rules

- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask — just do it silently.
- Prefer MCP tool over curl when available
- Include previous context in round 2+ prompts
- Document everything in STORY_REVIEW.md
- Be honest — don't game scores
