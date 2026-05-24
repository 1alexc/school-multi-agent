from google.adk.agents.llm_agent import Agent
from geography_agent.tools import get_country_info, get_geography_trivia

geography_agent = Agent(
    model='gemini-2.5-flash',
    name='geography_agent',
    description='A helpful assistant for geography questions.',
    instruction='You are an expert geography teacher. Answer user questions related to geography, maps, cultures, and physical environments clearly and accurately.',
    tools=[
        get_country_info,
        get_geography_trivia
    ]
)
