from google.adk.agents.llm_agent import Agent

english_agent = Agent(
    model='gemini-2.5-flash',
    name='english_agent',
    description='A helpful assistant for english and literature questions.',
    instruction='You are an expert English teacher. Answer user questions related to English literature, grammar, writing, and language arts clearly and accurately.',
)
