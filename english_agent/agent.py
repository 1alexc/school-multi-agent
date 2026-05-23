from google.adk.agents.llm_agent import Agent
from english_agent.tools import (
    check_readability_and_style,
    search_literary_devices,
    get_classic_literature_guide,
    search_gutenberg_books
)

english_agent = Agent(
    model='gemini-2.5-flash',
    name='english_agent',
    description='A helpful assistant for English, grammar, and literature questions. Capable of analyzing text readability and writing style, looking up literary devices and study guides, and searching Project Gutenberg for classic public-domain books.',
    instruction='You are an expert English teacher. Answer user questions related to English literature, grammar, writing, and language arts clearly and accurately. Always use your available tools to analyze text readability and style, lookup literary devices, refer to classic book study guides, or search Project Gutenberg for ebooks rather than guessing.',
    tools=[
        check_readability_and_style,
        search_literary_devices,
        get_classic_literature_guide,
        search_gutenberg_books
    ]
)
