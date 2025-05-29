from fastmcp import FastMCP
import httpx
import requests
import json
import asyncio
import logging

import uvicorn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    petstore_url = "https://petstore3.swagger.io/api/v3/openapi.json"

    logger.info(f"Fetching data from Petstore API: {petstore_url}")
    # Use requests to fetch the Petstore API data
    response = requests.get(petstore_url)

    response.raise_for_status()  # Raise an error for bad responses
    openapi_spec = response.json()
    
    #open a file to save the data
    with open('petstore_data.json', 'w') as f:
        json.dump(openapi_spec, f, indent=2)
    logger.info("Data fetched successfully from Petstore API.")

    logger.info("creating FastMCP server from petstore data")
    mcp = FastMCP(
        title = "PetstoreMCPServer", 
        description = "MCP server for Petstore API",
        version ="1.0.0"
    )
    # use http client to call remote API
    async with httpx.AsyncClient(base_url = "https://petstore3.swagger.io/api/v3") as http_client:
        fastmcp_api = FastMCP.from_openapi(
            openapi_spec=openapi_spec,
            client=http_client,
        )

        # pass FastAPI ASGI app to Uvicorn server
        app = fastmcp_api.sse_app

        logger.info("starting FastMCP server")
        config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
        server = uvicorn.Server(config)
        await server.serve()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise

