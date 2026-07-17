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
def fact_checker(state:ResearchState):
    print("Fact checker agent started")
    prompt=f"""
    You are a professional fact checker.
    verify the following research for accuracy and reliability.
    research:
    ({state['research']})
    Your tasks:
    1. Correct any factual mistakes.
    2. Remove misleading statements.
    3. Keep only reliable information.
    4. Return the corrected research only.

    Do not explain your reasoning.
    """
    response=llm.invoke(prompt)
    state["verified_research"]=response.content
    print("fact checking completed")
    return state