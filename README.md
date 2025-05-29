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

    1. python -m venv .venv 
    2. .\.venv\Scripts\activate
pip install fastmcp, fastapi, uv, requests
```

## Usage

```python


    4. mkdir src
    5. new-item src\main.py
    6. uv run .\src\main.py
    
    7. New terminal (shortcut: Ctrl+ Shift + ` ) 
        a. npx @modelcontextprotocol/inspector
        
        
    8. Open given MCP Inspector url, select Transport type as SSE, URL as http://localhost:8000/sse and click on Connect: 
    
    9. Select "Tool" option and you can now test the MCP tools e.g. AddPet (select id: 10, name: MyPet, scroll down and click "Run Tool" button)
    10. If you get "HTTP error 302: Found" error then check if can you hit swagger on the browser, sometimes public swagger are not accessible. 

    

```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

## License

This project is licensed under the terms specified in the LICENSE file.