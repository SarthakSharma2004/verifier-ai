from langchain_tavily import TavilySearch
import os


def search_claim(claim: str):
    """
    This function takes a claim string and returns Tavily search results.
    """

    tool = TavilySearch(
        max_results = 3,
        tavily_api_key = os.getenv("TAVILY_API_KEY")
    )

    results = tool.invoke({"query": claim})

    return results