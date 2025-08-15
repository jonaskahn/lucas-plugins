"""Math Agent Plugin Entry Point."""

import sys
from pathlib import Path

# Add plugins folder to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from lucas.plugins.loader import get_plugin_helper

# Initialize helper and setup environment
helper = get_plugin_helper()
helper.setup_environment()

from lucas.plugins.base import BasePlugin, BasePluginAgent, PluginMetadata

# Load agent module using OOP helper
agent_module = helper.load_agent_module(Path(__file__).parent)
MathAgent = agent_module.MathAgent


class MathPlugin(BasePlugin):
    """Math Plugin Bundle."""

    @staticmethod
    def get_metadata() -> PluginMetadata:
        """Return plugin metadata."""
        return PluginMetadata(
            name="math_agent",
            version="1.0.0",
            description="Simple mathematical calculations operations agent",
            capabilities=[
                "addition",
                "subtraction",
                "multiplication",
                "division",
                "power",
                "modulo",
            ],
            llm_requirements={
                "provider": "openai",
                "model": "gpt-4o",
                "temperature": 0.8,
                "max_tokens": 1024,
            },
        )

    @staticmethod
    def create_agent() -> BasePluginAgent:
        """Create agent instance."""
        return MathAgent(MathPlugin.get_metadata())


# Plugin interface functions (only required ones)
get_metadata = MathPlugin.get_metadata
create_agent = MathPlugin.create_agent
plugin = MathPlugin
