from langchain_core.prompts import ChatPromptTemplate
from prompts import PLANNER_PROMPT
from schemas import Plan
from llm import llm 

planner=(
    ChatPromptTemplate.from_messages(
        [
            ("system", PLANNER_PROMPT),
            ("human", "{goal}")
        ]
    )
    | llm.with_structured_output(Plan)
)

def create_plan(goal:str):
    return planner.invoke(
        {
            "goal":goal
        }
    )