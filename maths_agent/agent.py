from google.adk.agents.llm_agent import Agent

maths_agent = Agent(
    model='gemini-2.5-flash',
    name='maths_agent',
    description='A helpful assistant for mathematics questions.',
    instruction='You are an expert mathematics teacher. Answer user questions related to math, algebra, geometry, and calculus clearly and accurately.',
)
