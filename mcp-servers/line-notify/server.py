#!/usr/bin/env python3
"""
LINE Notify MCP Server — sends notifications via LINE Notify API.

Usage in ~/.claude/settings.json:
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
"""

import os
import sys
import json
import urllib.request
import urllib.parse


def send_line_notify(message: str, token: str) -> dict:
    """Send a message via LINE Notify API."""
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = urllib.parse.urlencode({"message": message}).encode("utf-8")
    
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return {"success": True, "status": body.get("status", 200), "message": body.get("message", "ok")}
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        return {"success": False, "status": e.code, "error": error_body}
    except Exception as e:
        return {"success": False, "status": 0, "error": str(e)}


def check_rate_limit(token: str) -> dict:
    """Check LINE Notify rate limit status."""
    url = "https://notify-api.line.me/api/status"
    headers = {"Authorization": f"Bearer {token}"}
    
    req = urllib.request.Request(url, headers=headers, method="GET")
    
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            rate_limit = resp.headers.get("X-RateLimit-Remaining", "unknown")
            rate_reset = resp.headers.get("X-RateLimit-Reset", "unknown")
            return {"remaining": rate_limit, "reset": rate_reset}
    except Exception as e:
        return {"error": str(e)}


def handle_request(request: dict) -> dict:
    """Handle incoming JSON-RPC request."""
    method = request.get("method", "")
    req_id = request.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": "line-notify", "version": "1.0.0"},
            },
        }

    if method == "notifications/initialized":
        return None  # No response needed

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "notify",
                        "description": "Send a notification message via LINE Notify. Use for pipeline progress updates, review scores, and completion alerts.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "message": {
                                    "type": "string",
                                    "description": "The notification message to send. Include emoji for readability. Max ~1000 chars.",
                                },
                            },
                            "required": ["message"],
                        },
                    },
                    {
                        "name": "check_status",
                        "description": "Check LINE Notify rate limit status (1000 messages/hour).",
                        "inputSchema": {
                            "type": "object",
                            "properties": {},
                        },
                    },
                ]
            },
        }

    if method == "tools/call":
        tool_name = request["params"]["name"]
        args = request["params"].get("arguments", {})
        token = os.environ.get("LINE_NOTIFY_TOKEN", "")

        if not token:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({"error": "LINE_NOTIFY_TOKEN not set. Configure in env or vault."}),
                        }
                    ],
                    "isError": True,
                },
            }

        if tool_name == "notify":
            message = args.get("message", "")
            if not message:
                return {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{"type": "text", "text": json.dumps({"error": "message is required"})}],
                        "isError": True,
                    },
                }

            result = send_line_notify(message, token)

            # Retry once on failure
            if not result.get("success"):
                import time
                time.sleep(2)
                result = send_line_notify(message, token)
                if result.get("success"):
                    result["retried"] = True

            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps(result)}],
                    "isError": not result.get("success", False),
                },
            }

        if tool_name == "check_status":
            result = check_rate_limit(token)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps(result)}],
                },
            }

    # Unknown method
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32601, "message": f"Unknown method: {method}"},
    }


def main():
    """Main loop — reads JSON-RPC from stdin, writes to stdout."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
            response = handle_request(request)
            if response is not None:
                sys.stdout.write(json.dumps(response) + "\n")
                sys.stdout.flush()
        except json.JSONDecodeError:
            error_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": "Parse error"},
            }
            sys.stdout.write(json.dumps(error_resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            error_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32603, "message": str(e)},
            }
            sys.stdout.write(json.dumps(error_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
