from google.adk.agents.llm_agent import Agent

science_agent = Agent(
    model='gemini-2.5-flash',
    name='science_agent',
    description='A helpful assistant for science questions.',
    instruction='You are an expert science teacher. Answer user questions related to physics, chemistry, biology, and the scientific method clearly and accurately.',
)
