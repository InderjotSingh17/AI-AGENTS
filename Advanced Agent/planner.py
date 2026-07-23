from llm import llm
from prompts import PLANNER_PROMPT
def planner(query:str):
    prompt = PLANNER_PROMPT.invoke(
        {
            "query": query
        }
    )
    response=llm.invoke(prompt)
    return response.content