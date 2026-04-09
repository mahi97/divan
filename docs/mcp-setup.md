# MCP Server Setup

MCP (Model Context Protocol) servers extend Claude Code with external service integrations. Most are configured automatically by their corresponding plugins.

## Automatic Setup

These MCP servers are configured when you install their plugins:

| Server | Plugin | Auth |
|--------|--------|------|
| GitHub Copilot | github | OAuth (github.com/login) |
| Vercel | vercel | OAuth (vercel.com) |
| Supabase | supabase | OAuth |
| Hugging Face | huggingface-skills | OAuth (huggingface.co) |
| Greptile | greptile | OAuth (auth.greptile.com) |
| Context7 | context7 | None (embedded) |

## First-Time Authentication

After installing plugins, each MCP server needs one-time OAuth authentication:

1. Start Claude Code
2. Use a feature that requires the MCP server (e.g., create a GitHub issue)
3. Claude will prompt you to authenticate via browser
4. Complete the OAuth flow
5. Token is cached in `~/.claude/.credentials.json`

## Manual MCP Configuration

To add custom MCP servers, create or edit `.mcp.json` in your project root:

```json
{
  "mcpServers": {
    "my-server": {
      "command": "npx",
      "args": ["-y", "my-mcp-server"],
      "env": {
        "API_KEY": "your-key"
      }
    }
  }
}
```

Or for HTTP-based MCP servers:

```json
{
  "mcpServers": {
    "my-server": {
      "type": "http",
      "url": "https://my-server.example.com/mcp"
    }
  }
}
```

## Troubleshooting

- **Auth expired**: Delete the server's entry from `~/.claude/.credentials.json` and re-authenticate
- **Server not responding**: Check `claude mcp list` for status
- **Missing tools**: Ensure the plugin is enabled in `~/.claude/settings.json`
