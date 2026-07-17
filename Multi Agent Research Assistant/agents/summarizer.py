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
def summarizer(state:ResearchState):
    print("Summarizer agent started")
    prompt = f"""
    You are an expert technical writer.
    Create a clear, concise, and well-structured summary
    from the verified research below.
    Verified Research:
    {state["verified_research"]}
    Write the response in simple language using
    headings and bullet points wherever appropriate.
    """
    response=llm.invoke(prompt)
    state["summary"]=response.content
    print("summarization completed")
    return state