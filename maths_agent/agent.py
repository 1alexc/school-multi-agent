from google.adk.agents.llm_agent import Agent
from maths_agent.tools import (
    solve_quadratic,
    calculate_geometry_properties,
    differentiate_polynomial,
    evaluate_definite_integral
)

maths_agent = Agent(
    model='gemini-2.5-flash',
    name='maths_agent',
    description='A helpful assistant for mathematics, algebra, geometry, and calculus questions. Capable of solving quadratic equations, calculating geometric shape properties (area, volume, perimeter), differentiating polynomials, and evaluating definite integrals.',
    instruction='You are an expert mathematics teacher. Answer user questions related to math, algebra, geometry, and calculus clearly and accurately. Always use your available tools to solve equations, calculate geometric properties, differentiate polynomials, or integrate functions rather than guessing or performing calculations manually.',
    tools=[
        solve_quadratic,
        calculate_geometry_properties,
        differentiate_polynomial,
        evaluate_definite_integral
    ]
)
