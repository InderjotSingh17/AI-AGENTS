from llm import llm
from prompts import SUPERVISOR_PROMPT
from schemas import RouteResponse
from coding_agent import coding_agent 
from research_agent import research_agent
from math_agent import math_agent 
structured_llm=llm.with_structured_output(RouteResponse)
def supervisor_agent(query:str):
    prompt=SUPERVISOR_PROMPT.invoke(
        {
            "query":query
        }
    )
    response=structured_llm.invoke(prompt)
    selected_agent=response.agent
    print(f"\nSupervisor selected: {selected_agent}\n")
    if selected_agent == "Coding Agent":
        return coding_agent(query)
    elif selected_agent == "Research Agent":
        return research_agent(query)
    elif selected_agent == "Math Agent":
        return math_agent(query)
    else:
        return "Unable to determine the appropriate agent."