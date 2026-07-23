from llm import llm
from prompts import RESEARCH_PROMPT
def research_agent(query:str):
    prompt=RESEARCH_PROMPT.invoke(
        {
            "query":query
        }
    )
    response=llm.invoke(prompt)
    return response.content