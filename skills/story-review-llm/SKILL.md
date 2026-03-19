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

### Phase A: Send to Reviewer (Round 1)

**Save the conversation context** — Round 2 needs to build on Round 1.

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

**Save the response** and store conversation context in `REVIEW_STATE.json`:
```json
{
  "conversation_history": [
    {"role": "system", "content": "You are a children's book editor..."},
    {"role": "user", "content": "[round 1 prompt]"},
    {"role": "assistant", "content": "[round 1 response]"}
  ]
}
```

**If MCP NOT available (curl fallback):**
```bash
# Round 1 — save messages for reuse
MESSAGES='[
  {"role": "system", "content": "You are a children's book editor..."},
  {"role": "user", "content": "[review prompt]"}
]'

curl -s "${LLM_BASE_URL}/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${LLM_API_KEY}" \
  -d "{\"model\": \"${LLM_MODEL}\", \"messages\": ${MESSAGES}, \"max_tokens\": 4096}"

# Save the assistant response for Round 2 context
```

### Phase A2: Send to Reviewer (Round 2+) — WITH CONTEXT

**CRITICAL:** Do NOT send a fresh prompt. Include previous conversation history.

**If MCP available:**
```
mcp__llm-chat__chat:
  system: "You are a children's book editor specializing in bedtime stories."
  prompt: |
    [Previous conversation context from REVIEW_STATE.json]

    --- ROUND 2 UPDATE ---

    Since your last review, we implemented these fixes:
    1. [Fix 1]: [description]
    2. [Fix 2]: [description]

    Here is the updated story:

    [Full updated story text]

    Please re-score using the same 8 criteria.
    Note what improved and what still needs work.
    
    Overall score: X/10
    Verdict: READY / ALMOST / NEEDS WORK
```

**If MCP NOT available (curl fallback):**
```bash
# Round 2+ — include full conversation history
MESSAGES='[
  {"role": "system", "content": "You are a children's book editor..."},
  {"role": "user", "content": "[round 1 prompt]"},
  {"role": "assistant", "content": "[round 1 response]"},
  {"role": "user", "content": "Since your last review, we changed: [fixes]. Here is the updated story: [text]. Re-score."}
]'

curl -s "${LLM_BASE_URL}/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${LLM_API_KEY}" \
  -d "{\"model\": \"${LLM_MODEL}\", \"messages\": ${MESSAGES}, \"max_tokens\": 4096}"
```

This ensures Round 2 knows what was changed and can assess improvement accurately.

### Phase B: Parse & Decide

- Score >= 8 AND "READY" → STOP, approved
- Score 6-7 AND "ALMOST" → implement fixes, re-review (with context)
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

Update `REVIEW_STATE.json` with current state AND updated conversation history.

### Phase E: Score Progression Tracking

**After every round**, append to `SCORE_TRACKER.md`:

```markdown
## Score Progression: "[Story Title]" (LLM: {model_name})

| Round | Time | Age | Arc | Read | Engage | Moral | Illust | Parent | Bedtime | Overall | Δ |
|-------|------|-----|-----|------|--------|-------|--------|--------|---------|---------|---|
| R0 draft | HH:MM | X | X | X | X | X | X | X | X | X.X | — |
| R1 review | HH:MM | X | X | X | X | X | X | X | X | X.X | +X.X |
```

Include the model name so we can compare quality across providers.

### Phase F: Version Output

**CRITICAL:** Do NOT overwrite the input file. Create a NEW versioned file:

- Input: `stories/{slug}_v0_draft.md`
- Output: `stories/{slug}_v1_reviewed.md`

Frontmatter of v1 must include:
```yaml
version: 1
version_label: "reviewed"
previous_version: "stories/{slug}_v0_draft.md"
review_score: X.X
review_rounds: N
reviewer_model: "deepseek-chat"
```

### Termination

1. Update `REVIEW_STATE.json`:
```json
{
  "round": 2,
  "story_file": "stories/{slug}_v0_draft.md",
  "output_file": "stories/{slug}_v1_reviewed.md",
  "status": "completed",
  "final_score": 8.5,
  "score_progression": [5.8, 7.4, 8.5],
  "reviewer_model": "deepseek-chat",
  "timestamp": "2026-03-19T23:00:00"
}
```
2. Move approved stories to `output/approved/`

## Key Rules

- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask — just do it silently.
- Prefer MCP tool over curl when available
- Include previous context in round 2+ prompts
- Document everything in STORY_REVIEW.md
- Be honest — don't game scores
- **Never overwrite input**: Always create `_v1_reviewed.md` from `_v0_draft.md`
- **Track every score**: `SCORE_TRACKER.md` must be updated after EVERY round
- **Include model name**: Score tracker must record which LLM provider was used
