# Copyright (c) 2025 GenOrca. All Rights Reserved.

# MCP Router for Utility Tools

from fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import Annotated, Optional
# Updated import to use core.py to avoid circular dependency
from unreal_mcp.core import send_to_unreal, ToolInputError, UnrealExecutionError

util_mcp = FastMCP(name="UtilityMCP", description="Utility tools for Unreal Engine logging and diagnostics.")

UTIL_ACTIONS_MODULE = "UnrealMCPython.util_actions"

@util_mcp.tool(
    name="unreal_get_output_log",
    description="Retrieves recent lines from the Unreal Engine output log. Supports filtering by keyword to find specific errors or warnings.",
    tags={"unreal", "log", "debug", "diagnostics"}
)
async def get_output_log(
    line_count: Annotated[int, Field(description="Number of recent log lines to retrieve.", ge=1, le=500)] = 50,
    keyword: Annotated[Optional[str], Field(description="Filter log lines containing this keyword (case-insensitive). e.g. 'Error', 'Warning', 'LogBlueprintUserMessages'.")] = None
) -> dict:
    """Retrieves recent lines from the Unreal Engine output log."""
    params = {"line_count": line_count}
    if keyword is not None:
        params["keyword"] = keyword
    try:
        return await send_to_unreal(
            action_module=UTIL_ACTIONS_MODULE,
            action_name="ue_get_output_log",
            params=params
        )
    except UnrealExecutionError as e:
        return {"success": False, "message": str(e), "details": e.details}
        return {"success": False, "message": f"An unexpected error occurred: {str(e)}"}