from google.adk.agents.llm_agent import Agent

history_agent = Agent(
    model='gemini-2.5-flash',
    name='history_agent',
    description='A helpful assistant for history questions.',
    instruction='You are an expert history teacher. Answer user questions related to historical events, dates, and historical analysis clearly and accurately.',
)
