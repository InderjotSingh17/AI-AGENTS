from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from tools.calculator import multiply
from memory.checkpoint import memory
import os 
from dotenv import load_dotenv
from tools.clock import current_time
from tools.weather import get_weather
load_dotenv()
llm = ChatOpenAI(
    model="deepseek/deepseek-chat",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0
)
agent = create_react_agent(
    model=llm,
    tools=[
        multiply,
        current_time,
        get_weather
    ],
    checkpointer=memory
)