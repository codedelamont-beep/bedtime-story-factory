#!/usr/bin/env python3
"""
LLM Chat MCP Server — Generic OpenAI-compatible LLM wrapper.
Enables cross-model story review using any provider (DeepSeek, Kimi, OpenRouter, etc.)

Usage:
  Set env vars: LLM_API_KEY, LLM_BASE_URL, LLM_MODEL
  Then register as MCP server in Claude Code settings.
"""

import os
import json
import sys
import httpx
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

app = Server("llm-chat")

API_KEY = os.environ.get("LLM_API_KEY", "")
BASE_URL = os.environ.get("LLM_BASE_URL", "https://api.deepseek.com/v1")
DEFAULT_MODEL = os.environ.get("LLM_MODEL", "deepseek-chat")


@app.list_tools()
async def list_tools():
    return [
        Tool(
            name="chat",
            description="Send a prompt to an external LLM for review/feedback. "
                        "Use for cross-model story review.",
            inputSchema={
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "The prompt to send to the LLM"
                    },
                    "system": {
                        "type": "string",
                        "description": "Optional system message",
                        "default": "You are a helpful assistant."
                    },
                    "model": {
                        "type": "string",
                        "description": f"Model to use (default: {DEFAULT_MODEL})",
                        "default": DEFAULT_MODEL
                    },
                    "max_tokens": {
                        "type": "integer",
                        "description": "Max tokens in response",
                        "default": 4096
                    }
                },
                "required": ["prompt"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name != "chat":
        return [TextContent(type="text", text=f"Unknown tool: {name}")]

    if not API_KEY:
        return [TextContent(
            type="text",
            text="Error: LLM_API_KEY not set. Configure via environment variable."
        )]

    prompt = arguments.get("prompt", "")
    system = arguments.get("system", "You are a helpful assistant.")
    model = arguments.get("model", DEFAULT_MODEL)
    max_tokens = arguments.get("max_tokens", 4096)

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": prompt}
    ]

    url = f"{BASE_URL.rstrip('/')}/chat/completions"

    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {API_KEY}"
                },
                json={
                    "model": model,
                    "messages": messages,
                    "max_tokens": max_tokens
                }
            )
            response.raise_for_status()
            data = response.json()

            content = data["choices"][0]["message"]["content"]
            model_used = data.get("model", model)
            usage = data.get("usage", {})

            result = f"**Model**: {model_used}\n"
            if usage:
                result += f"**Tokens**: {usage.get('prompt_tokens', '?')} in / {usage.get('completion_tokens', '?')} out\n"
            result += f"\n---\n\n{content}"

            return [TextContent(type="text", text=result)]

    except httpx.HTTPStatusError as e:
        return [TextContent(
            type="text",
            text=f"API Error {e.response.status_code}: {e.response.text}"
        )]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
