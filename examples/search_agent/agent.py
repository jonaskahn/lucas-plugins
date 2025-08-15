"""
Search Agent Implementation
"""

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


class SearchAgent(BasePluginAgent):
    """Web search and information retrieval agent.""" ""

    def __init__(self, metadata: PluginMetadata):
        """Initialize the search agent."""
        super().__init__(metadata)
        self.metadata = metadata

        # Load tools module using OOP helper
        tools_module = helper.load_tools_module(Path(__file__).parent)
        self.search_tools = tools_module.search_tools

    def get_tools(self) -> List:
        """Get available tools.""" ""
        return self.search_tools

    def get_system_prompt(self) -> str:
        """Get system prompt.""" ""
        return (
            "You are the Search Agent specialized in web search and information retrieval. "
            "You have tools for: web_search, search_news, search_academic, search_images. "
            "Understand search intent, use appropriate tools, summarize findings, "
            "cite sources, and provide comprehensive, well-organized responses."
        )
