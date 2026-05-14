from google.adk.agents.llm_agent import Agent

geography_agent = Agent(
    model='gemini-2.5-flash',
    name='geography_agent',
    description='A helpful assistant for geography questions.',
    instruction='You are an expert geography teacher. Answer user questions related to geography, maps, cultures, and physical environments clearly and accurately.',
)
