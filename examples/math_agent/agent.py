"""Math Agent Implementation."""

import sys
from pathlib import Path
from typing import List

# Add plugins folder to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from lucas.plugins.loader import get_plugin_helper

# Initialize helper and setup
helper = get_plugin_helper()
helper.setup_environment()

from lucas.plugins.base import BasePluginAgent, PluginMetadata


class MathAgent(BasePluginAgent):
    """Math operations and problem-solving agent."""

    def __init__(self, metadata: PluginMetadata):
        """Initialize the math agent."""
        super().__init__(metadata)
        self.metadata = metadata

        # Load tools module using OOP helper
        tools_module = helper.load_tools_module(Path(__file__).parent)
        self.math_tools = tools_module.math_tools

    def get_tools(self) -> List:
        """Get available tools."""
        return self.math_tools

    def get_system_prompt(self) -> str:
        """Get system prompt."""
        return (
            "You are the Math Agent specialized in mathematical operations. "
            "You have tools for: add, subtract, multiply, divide, power, modulo. "
            "Parse problems, break down calculations, show work step-by-step, "
            "and provide clear results with explanations."
        )
