from llm import llm
from tools import TOOLS
from memory import memory
from planner import planner
from reflection import reflection
llm_with_tools = llm.bind_tools(TOOLS)
def advanced_agent(query: str):
    messages = memory.load_memory_variables({}).get("history", [])
    plan = planner(query)
    messages.append(
        {
            "role": "system",
            "content": f"Plan:\n{plan}"
        }
    )
    messages.append(
        {
            "role": "user",
            "content": query
        }
    )
    while True:
        response = llm_with_tools.invoke(messages)
        if response.tool_calls:
            messages.append(response)
            for tool_call in response.tool_calls:
                selected_tool = next(
                    tool for tool in TOOLS
                    if tool.name == tool_call["name"]
                )
                tool_result = selected_tool.invoke(tool_call["args"])
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call["id"],
                        "content": str(tool_result)
                    }
                )
            continue
        answer = response.content
        review = reflection(query, answer)
        print("\n===== REFLECTION =====")
        print(review)
        print("======================\n")
        if review.is_correct:
            memory.save_context(
                {"input": query},
                {"output": answer}
            )
            return answer
        messages.append(
            {
                "role": "system",
                "content": f"""
The previous answer was not satisfactory.
Feedback:
{review.feedback}
Generate a better answer.
"""
            }
        )