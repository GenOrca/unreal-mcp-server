# unreal-mcp-server

unreal-mcp-server is a Python-based server that implements the Model Context Protocol (MCP) for Unreal Engine. 
It enables smooth communication between MCP clients (e.g., Claude, Cursor, Windsurf) and the Unreal Editor, and is intended to be used together with the Unreal-MCPython Plugin.

## Key Features

- MCP server for communication with Unreal Engine
- Built-in routers for various operations (e.g., Actor, Asset, Editor, etc)
- Supports Python 3.11 and later

# Installation

Clone the repository:

```bash
git clone https://github.com/your-org/unreal-mcp-server.git
cd unreal-mcp-server
```

# Running the Server

You can start the MCP server with the following command:
```bash
uv --directory absolute/path/to/unreal-mcp-server run src/unreal_mcp/main.py
```

# Example Configuration (Using Claude, VSCode, Cursor)

The following is an example configuration for launching the MCP server from Claude, VSCode, or Cursor:

```json
{
    "mcpServers": {
        "unreal-mcpython": {
            "command": "uv",
            "args": [
                "--directory",
                "/absolute/path/to/unreal-mcp-server",  // e.g., D:/GitHub/unreal-mcp-server
                "run",
                "src/unreal_mcp/main.py"
            ]
        }
    }
}
```

This configuration approach works similarly across editors like VSCode and Cursor.

# License

This project is licensed under the Apache-2.0 License. See the LICENSE file for details.