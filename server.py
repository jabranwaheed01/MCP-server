from mcp.server.mcpserver import MCPServer

mcp = MCPServer("My MCP Server")

@mcp.tool()
def add (a : int , b : int) -> int :
    """Add two Numbers."""
    return a + b 

@mcp.resource("config://app")
def get_config() -> str:
    """Application configuration"""
    return("App: MCP Project\nVersion: 1.0\nEnvironment: Development")

@mcp.prompt()
def explain_query(query: str) -> str:
    """Create a simple explanation prompt"""
    return f"Explain {query} in simple words."



if __name__ == "__main__":
    mcp.run()