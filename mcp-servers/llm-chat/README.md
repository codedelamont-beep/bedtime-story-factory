# LLM Chat MCP Server

A lightweight MCP server that wraps any OpenAI-compatible LLM API as an MCP tool.
This enables cross-model review in the story pipeline using cheap/free models.

## Setup

```bash
pip install -r requirements.txt
```

## Configuration

Set via environment variables:
- `LLM_API_KEY` — API key for the provider
- `LLM_BASE_URL` — Base URL (e.g., `https://api.deepseek.com/v1`)
- `LLM_MODEL` — Model name (e.g., `deepseek-chat`)

## Add to Claude Code

```json
{
  "mcpServers": {
    "llm-chat": {
      "command": "python3",
      "args": ["mcp-servers/llm-chat/server.py"],
      "env": {
        "LLM_API_KEY": "your-key",
        "LLM_BASE_URL": "https://api.deepseek.com/v1",
        "LLM_MODEL": "deepseek-chat"
      }
    }
  }
}
```

## Supported Providers

| Provider | Base URL | Models |
|----------|----------|--------|
| DeepSeek | `https://api.deepseek.com/v1` | `deepseek-chat`, `deepseek-reasoner` |
| OpenRouter | `https://openrouter.ai/api/v1` | Any model on OpenRouter |
| OpenAI | `https://api.openai.com/v1` | `gpt-4o`, `gpt-4o-mini` |
| Kimi | `https://api.moonshot.cn/v1` | `moonshot-v1-8k` |
| ModelScope | `https://api-inference.modelscope.cn/v1` | `Qwen/Qwen2.5-72B` |
