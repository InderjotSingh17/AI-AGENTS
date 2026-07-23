from langchain_core.prompts import ChatPromptTemplate 
AGENT_PROMPT=ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a helpful AI assistant.
Answer the user's questions accurately.
If a suitable tool is available, use it whenever necessary instead of guessing.
After using the tool, provide a clear and concise final answer.
            """
        ),
        (
            "human",
            "{query}"
        )
    ]
)