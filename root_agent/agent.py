from google.adk.agents.llm_agent import Agent

from computer_science_agent.agent import computer_science_agent
from english_agent.agent import english_agent
from geography_agent.agent import geography_agent
from history_agent.agent import history_agent
from maths_agent.agent import maths_agent
from science_agent.agent import science_agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='School coordinator agent that routes student queries to the appropriate subject agent.',
    instruction='''You are a school coordinator.
Your job is to understand student queries, determine the subject of their question, and route the question to the relevant subject agent (computer_science, english, geography, history, maths, or science).
Aggregate the response from the subject agent and present it clearly to the student.
Maintain context of the conversation.
If a student asks a general question, help them directly, but for any subject-specific questions, you MUST delegate to the appropriate specialist agent.''',
    sub_agents=[
        computer_science_agent,
        english_agent,
        geography_agent,
        history_agent,
        maths_agent,
        science_agent
    ]
)
