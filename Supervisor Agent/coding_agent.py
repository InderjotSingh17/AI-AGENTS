from llm import llm
from prompts import CODING_PROMPT
def coding_agent(query:str):
    prompt=CODING_PROMPT.invoke(
        {
            "query":query
        }
    )
    response=llm.invoke(prompt)
    return response.content