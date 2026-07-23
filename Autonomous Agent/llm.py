import os 
from dotenv import load_dotenv 
load_dotenv()
from langchain_openai import ChatOpenAI
llm=ChatOpenAI(
    model="openai/gpt-4.1-mini",
    base_url="https://openrouter.ai/api/v1",
    temperature=0,
    api_key=os.getenv("OPENROUTER_API_KEY"),
    max_tokens=512,
)