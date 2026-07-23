from llm import llm
from prompts import MATH_PROMPT 
def math_agent(query:str):
    prompt=MATH_PROMPT.invoke(
        {
            "query":query
        }
    )
    response=llm.invoke(prompt)
    return response.content