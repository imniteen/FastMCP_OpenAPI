# FastMCP OpenAPI

FastMCP OpenAPI is a Python-based API framework for interacting with the MCP (Managed Contract Platform) system.

## Overview

This project provides a streamlined interface to access and manage contracts through the MCP platform using modern Python APIs.

## Features

- RESTful API endpoints for contract management
- OpenAPI specification compliance
- Authentication and authorization mechanisms
- Comprehensive data validation
- Scalable architecture
## Installation

```bash
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# Install dependencies
pip install fastmcp fastapi uv requests
```

## Usage

```python
# Set up project structure
mkdir src
new-item src\main.py
uv run .\src\main.py

# Testing with MCP Inspector
# 1. Open a new terminal (Ctrl+Shift+`)
npx @modelcontextprotocol/inspector

# 2. In the MCP Inspector:
#    - Set Transport type to SSE
#    - Set URL to http://localhost:8000/sse
#    - Click Connect
#    - Select "Tool" option
#    - Test tools (e.g., AddPet with id: 10, name: MyPet)
#    - Click "Run Tool" button

# Note: If you encounter "HTTP error 302: Found", verify the Swagger UI 
# is accessible in your browser as some public Swagger instances may be restricted.
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

## License

This project is licensed under the terms specified in the LICENSE file.