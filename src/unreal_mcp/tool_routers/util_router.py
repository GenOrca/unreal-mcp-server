# Copyright (c) 2025 GenOrca. All Rights Reserved.

# MCP Router for Utility Tools

from fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import Annotated
# Updated import to use core.py to avoid circular dependency
from unreal_mcp.core import send_to_unreal, ToolInputError, UnrealExecutionError

util_mcp = FastMCP(name="UtilityMCP")

UTIL_ACTIONS_MODULE = "UnrealMCPython.util_actions"