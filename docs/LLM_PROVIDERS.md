# 🤖 LLM Providers — Pricing & Configuration

Choose the right model for your overnight story runs.

## Provider Comparison

| Provider | Model | Input $/1M | Output $/1M | Quality | Speed | Best For |
|----------|-------|-----------|-------------|---------|-------|----------|
| **DeepSeek** | `deepseek-chat` | $0.14 | $0.28 | ⭐⭐⭐⭐ | Fast | Overnight review (cheap) |
| **ModelScope** | `Qwen/Qwen2.5-72B` | Free (2000/day) | Free | ⭐⭐⭐ | Medium | Free tier testing |
| **Kimi** | `moonshot-v1-8k` | Free tier | Free tier | ⭐⭐⭐ | Fast | Free budget runs |
| **OpenRouter** | `deepseek/deepseek-chat` | $0.14 | $0.28 | ⭐⭐⭐⭐ | Fast | Multi-model routing |
| **OpenRouter** | `google/gemini-2.5-pro` | $1.25 | $10.00 | ⭐⭐⭐⭐⭐ | Medium | Best quality review |
| **OpenRouter** | `anthropic/claude-sonnet` | $3.00 | $15.00 | ⭐⭐⭐⭐⭐ | Medium | Premium review |
| **OpenAI** | `gpt-4o` | $2.50 | $10.00 | ⭐⭐⭐⭐⭐ | Fast | Default reviewer |
| **OpenAI** | `gpt-4o-mini` | $0.15 | $0.60 | ⭐⭐⭐ | Very fast | Budget review |

## Recommended Configurations

### 💰 Cheapest Overnight (< $0.01 per batch)

```json
{
  "LLM_BASE_URL": "https://api.deepseek.com/v1",
  "LLM_API_KEY": "your-deepseek-key",
  "LLM_MODEL": "deepseek-chat"
}
```

**Cost for 10 stories × 3 review rounds:** ~$0.005
DeepSeek offers excellent quality at near-zero cost. Best for regular overnight runs.

### 🆓 Completely Free

```json
{
  "LLM_BASE_URL": "https://api-inference.modelscope.cn/v1",
  "LLM_API_KEY": "your-modelscope-key",
  "LLM_MODEL": "Qwen/Qwen2.5-72B"
}
```

**Cost:** $0. Limited to 2000 requests/day (plenty for a batch).
Quality is good enough for initial review rounds.

### ⭐ Best Quality

```json
{
  "LLM_BASE_URL": "https://openrouter.ai/api/v1",
  "LLM_API_KEY": "your-openrouter-key",
  "LLM_MODEL": "google/gemini-2.5-pro"
}
```

**Cost for 10 stories:** ~$0.50-1.00
Use for final quality passes or when you want maximum review quality.

### ⚖️ Balanced (Quality + Cost)

```json
{
  "LLM_BASE_URL": "https://openrouter.ai/api/v1",
  "LLM_API_KEY": "your-openrouter-key",
  "LLM_MODEL": "openai/gpt-4o-mini"
}
```

**Cost for 10 stories:** ~$0.02-0.05
Good reviewer quality at very low cost. Solid middle ground.

## Cost Breakdown Per Batch (10 Stories)

| Stage | Tokens In | Tokens Out | DeepSeek | GPT-4o | GPT-4o-mini |
|-------|-----------|-----------|----------|--------|-------------|
| Bridge (10 concepts) | ~5K | ~3K | $0.001 | $0.04 | $0.001 |
| Review R1 (10 stories) | ~15K | ~10K | $0.005 | $0.14 | $0.008 |
| Review R2 (7 stories) | ~15K | ~8K | $0.004 | $0.12 | $0.006 |
| Improvement R1 (7 stories) | ~15K | ~8K | $0.004 | $0.12 | $0.006 |
| Improvement R2 (5 stories) | ~12K | ~6K | $0.003 | $0.09 | $0.005 |
| **Total** | ~62K | ~35K | **$0.017** | **$0.51** | **$0.026** |

> The writing itself is done by your Claude Code subscription — no extra LLM cost.

## Multi-Provider Strategy

For maximum quality at minimum cost, use different models for different stages:

```
Bridge review:        DeepSeek (cheap — just needs GO/SKIP decision)
First review:         GPT-4o-mini (good enough for structural review)
Improvement review:   GPT-4o (premium quality for final polish)
```

Override per-stage in pipeline:
```
/story-pipeline "theme" — reviewer_model: deepseek-chat
```

Or per-skill:
```
/story-review "file.md" — reviewer_model: gpt-4o
/story-improvement-loop "file.md" — reviewer_model: gpt-4o
```

## Getting API Keys

| Provider | URL | Free Tier? |
|----------|-----|-----------|
| DeepSeek | https://platform.deepseek.com/ | Yes ($5 credit) |
| ModelScope | https://modelscope.cn/ | Yes (2000 req/day) |
| Kimi | https://platform.moonshot.cn/ | Yes (limited) |
| OpenRouter | https://openrouter.ai/ | No (pay-per-use) |
| OpenAI | https://platform.openai.com/ | No (pay-per-use) |

## Security

Store API keys securely:

```bash
# Option 1: Environment variable
export LLM_API_KEY="sk-..."

# Option 2: Second Brain vault (encrypted)
/vault-store LLM_API_KEY "sk-..."
```

Never commit API keys to the repository.
