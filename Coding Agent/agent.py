from llm import llm 
from prompts import CODING_PROMPT 
from schemas import CodeResponse
from tools import TOOLS 
llm_with_tools=llm.bind_tools(TOOLS)
structured_llm=llm_with_tools.with_structured_output(CodeResponse)
def coding_agent(query:str):
    prompt=CODING_PROMPT.invoke(
        {
            "query":query
        }
    )
    response=structured_llm.invoke(prompt)
    return response 