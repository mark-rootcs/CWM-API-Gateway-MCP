from setuptools import setup, find_packages

setup(
    name="mcp-server-api-gateway",
    version="0.1.0",
    description="Model Context Protocol server for general API gateway to ConnectWise Manage",
    author="Jason Smith",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "mcp>=1.3.0",
        "httpx>=0.23.0",
        "pydantic>=1.10.0",
        "aiohttp>=3.8.4",
    ],
    entry_points={
        "console_scripts": [
            "mcp-server-api-gateway=api_gateway_server:main",
        ],
    },
)
