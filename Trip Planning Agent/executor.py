from langchain_core.messages import HumanMessage,ToolMessage 
from llm import llm
from tools import (
    get_weather,
    search_hotels,
    search_transport,
    estimate_budget,
)
tools = [
    get_weather,
    search_hotels,
    search_transport,
    estimate_budget,
]
llm_with_tools=llm.bind_tools(tools)
def execute(plan):
    messages=[
        HumanMessage(
            content=plan.goal
        )
    ]
    for step in plan.steps:
        print(f"\nSTEP : {step}")
        response=llm_with_tools.invoke(messages)
        messages.append(response)
        if response.tool_calls:
            for tool_call in response.tool_calls:
                selected_tool={
                    tool.name:tool
                    for tool in tools
                }[tool_call["name"]]
                tool_result=selected_tool.invoke(
                    tool_call["args"]
                )
                print(tool_result)
                messages.append(
                    ToolMessage(
                        content=tool_result,
                        tool_call_id=tool_call["id"]
                    )
                )
        final_response=llm.invoke(messages)
        return final_response.content