import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from graph.state import ResearchState
load_dotenv()
llm=ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="openai/gpt-4.1-mini",
    max_tokens=512
)
def researcher(state:ResearchState):
    print("Research agent started")
    prompt=f"""
    You are a professional research assistant.
    research the following topic to detail.
    topic:
    ({state['query']})
    return only the research.
    """
    response=llm.invoke(prompt)
    state["research"]=response.content
    print("research completed")
    return state 