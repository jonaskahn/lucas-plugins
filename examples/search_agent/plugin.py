"""Search Agent Plugin Entry Point."""

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
SearchAgent = agent_module.SearchAgent


class SearchPlugin(BasePlugin):
    """Search Plugin Bundle."""

    @staticmethod
    def get_metadata() -> PluginMetadata:
        """Return plugin metadata."""
        return PluginMetadata(
            name="search_agent",
            version="1.0.0",
            description="Web search and information retrieval agent",
            capabilities=[
                "web_search",
                "news_search",
                "academic_search",
                "image_search",
                "information_lookup",
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
        """Create Search Agent instance."""
        return SearchAgent(SearchPlugin.get_metadata())


plugin = SearchPlugin
