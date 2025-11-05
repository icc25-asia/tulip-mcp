# Tulip MCP

This a Model Context Protocol server implementation for [Tulip](https://github.com/OpenAttackDefenseTools/tulip).

## Setup

Use `TULIP_API_BASE_URL` environment variable to set the Tulip API base URL. Example: `http://localhost:3000/api`.

This project uses uv for dependency management. To install dependencies, run:

```bash
uv install
```

To run the server, use:

```bash
uv run mcp run main.py --transport streamable-http
```

You can use `mcp.json` for VSCode integration. Refer to [.vscode/mcp.json](.vscode/mcp.json) for an example configuration.
