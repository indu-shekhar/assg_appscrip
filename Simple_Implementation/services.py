from datetime import datetime

from fastapi import HTTPException
import google.generativeai as genai
from duckduckgo_search import DDGS

from settings import GEMINI_API_KEY, logger


def search_market_data(sector: str) -> str:
    """Look up fresh sector news via DuckDuckGo."""
    logger.info("Searching data for sector: %s", sector)
    query = f"trade opportunities {sector} sector India market analysis {datetime.now().year}"

    results_text = ""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
            if not results:
                return "No immediate search results found."

            for res in results:
                results_text += (
                    f"Title: {res['title']}\n"
                    f"Snippet: {res['body']}\n"
                    f"Source: {res['href']}\n\n"
                )
    except Exception as exc:  # pragma: no cover - passthrough logging
        logger.error("Search failed: %s", exc)
        return f"Error collecting external data: {exc}"

    return results_text


def analyze_with_gemini(sector: str, market_data: str) -> str:
    """Send collected data to Gemini for a markdown report."""
    if not GEMINI_API_KEY:
        return "Error: GEMINI_API_KEY is not set in the environment."

    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-2.5-flash-lite")

        prompt = f"""
        You are an expert Trade Analyst specializing in the Indian Market.

        Analyze the following search results for the '{sector}' sector in India.

        Search Data:
        {market_data}

        Generate a comprehensive Market Analysis Report in Markdown format.
        The report must include:
        1. **Executive Summary**: Brief overview of the sector currently.
        2. **Key Trade Opportunities**: Specific areas for export/import or investment.
        3. **Risks & Challenges**: Regulatory, economic, or logistical barriers.
        4. **Market Trends**: Emerging trends based on the data.
        5. **Conclusion**: Strategic recommendation.

        Keep the tone professional and actionable.
        """

        response = model.generate_content(prompt)
        return response.text
    except Exception as exc:
        logger.error("Gemini Analysis failed: %s", exc)
        raise HTTPException(status_code=500, detail=f"AI Analysis failed: {exc}")
