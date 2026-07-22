import os 
from dotenv import load_dotenv 
from langchain_openai import ChatOpenAI
load_dotenv()
llm=ChatOpenAI(
    model="openai/gpt-4.1-mini",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0,
    max_tokens=512
)                         