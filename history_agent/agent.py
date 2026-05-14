from google.adk.agents.llm_agent import Agent
from history_agent.tools import get_now, wikipedia_summary

history_agent = Agent(
    model='gemini-2.5-flash',
    name='history_agent',
    description='A helpful assistant for history questions.',
    instruction='You are an expert history teacher. Answer user questions related to historical events, dates, and historical analysis clearly and accurately. Always use your available tools to check current dates or look up factual summaries of historical events from Wikipedia rather than guessing.',
    tools=[get_now, wikipedia_summary]
)
