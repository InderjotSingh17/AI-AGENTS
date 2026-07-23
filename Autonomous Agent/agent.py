from llm import llm
from prompts import AGENT_PROMPT
from tools import TOOLS
from langchain_core.messages import ToolMessage
llm_with_tools=llm.bind_tools(TOOLS)
def autonomous_agent(query:str):
    prompt=AGENT_PROMPT.invoke(
        {
            "query":query
        }
    )
    messages=prompt.to_messages()
    while True:
        response=llm_with_tools.invoke(messages)
        if not response.tool_calls:
            return response.content
        messages.append(response)
        for tool_call in response.tool_calls:
            selected_tool=next(
                tool for tool in TOOLS
                if tool.name==tool_call["name"]
            )
            tool_result=selected_tool.invoke(tool_call["args"])
            messages.append(
                ToolMessage(
                    content=str(tool_result),
                    tool_call_id=tool_call["id"]
                )
            )