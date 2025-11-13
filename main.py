from mcp.server.fastmcp.server import stdio_server
from weather import mcp

def main():
    stdio_server(mcp)

if __name__ == "__main__":
    main()