from google.adk.agents.llm_agent import Agent

computer_science_agent = Agent(
    model='gemini-2.5-flash',
    name='computer_science_agent',
    description='A helpful assistant for computer science questions.',
    instruction='You are an expert computer science teacher. Answer user questions related to computer science, programming, and algorithms clearly and accurately.',
)
