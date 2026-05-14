from google.adk.agents.llm_agent import Agent
from science_agent.tools import periodic_table_lookup, unit_converter

science_agent = Agent(
    model='gemini-2.5-flash',
    name='science_agent',
    description='A helpful assistant for science questions.',
    instruction='You are an expert science teacher. Answer user questions related to physics, chemistry, biology, and the scientific method clearly and accurately. Always use your available tools to perform calculations or look up factual elemental data rather than guessing.',
    tools=[periodic_table_lookup, unit_converter]
)
