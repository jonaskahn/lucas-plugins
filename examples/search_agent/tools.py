"""
Search Agent Tools
Web search and information retrieval tools
"""

from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool


@tool
def web_search(query: str) -> str:
    """Search the web for information using DuckDuckGo.

    Args:
        query: The search query

    Returns:
        Search results from the web
    """
    try:
        search = DuckDuckGoSearchRun()
        results = search.run(query)
        return results[:500]  # Limit response length
    except Exception as e:
        return f"Search error: {str(e)}"


@tool
def search_news(query: str) -> str:
    """Search for recent news articles.

    Args:
        query: The news search query

    Returns:
        News search results
    """
    try:
        # Simplified news search using DuckDuckGo with news filter
        search = DuckDuckGoSearchRun()
        news_query = f"{query} news"
        results = search.run(news_query)
        return f"News results: {results[:500]}"
    except Exception as e:
        return f"News search error: {str(e)}"


@tool
def search_academic(query: str) -> str:
    """Search for academic and research information.

    Args:
        query: The academic search query

    Returns:
        Academic search results
    """
    try:
        search = DuckDuckGoSearchRun()
        academic_query = f"{query} research paper academic"
        results = search.run(academic_query)
        return f"Academic results: {results[:500]}"
    except Exception as e:
        return f"Academic search error: {str(e)}"


@tool
def search_images(query: str) -> str:
    """Search for images related to the query.

    Args:
        query: The image search query

    Returns:
        Description of image search results
    """
    try:
        search = DuckDuckGoSearchRun()
        image_query = f"{query} images"
        results = search.run(image_query)
        return f"Image search results: {results[:300]}"
    except Exception as e:
        return f"Image search error: {str(e)}"


# List of all search tools
search_tools = [web_search, search_news, search_academic, search_images]
