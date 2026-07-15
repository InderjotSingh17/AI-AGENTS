from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage
from graphs.agent import agent
config={
    "configurable":{
        "thread_id":"user1"
    }
}
while True:
    user_input=input("\nYou: ")
    if user_input.lower() in ["exit","quit"]:
        break
    response = agent.invoke(
        {
            "messages": [
                HumanMessage(content=user_input)
            ]
        },
        config=config
    )
    print("\nAgent:", response["messages"][-1].content)