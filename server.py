import os
from mcp.server.fastmcp import FastMCP

# 创建 MCP 服务，但不注册任何工具
mcp = FastMCP("Empty Tools Test Server")

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        stateless_http=True,
        json_response=True,
    )
