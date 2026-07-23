from langchain_core.prompts import ChatPromptTemplate
PLANNER_PROMPT=ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI planner.
Analyze the user's request and decide how to solve it.
If a tool is required, use it.
Think step by step before producing the final answer.
            """
        ),
        (
            "human",
            "{query}"
        )
    ]
)

REFLECTION_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI reviewer.
Review the previous answer.
If the answer is correct and complete, approve it.
If it contains mistakes or missing information, explain what should be improved.
            """
        ),
        (
            "human",
            """
User Question:
{query}
AI Answer:
{answer}
            """
        )
    ]
)