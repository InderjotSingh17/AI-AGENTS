from langgraph.graph import StateGraph,START,END
from graph.state import ResearchState
from agents.researcher import researcher
from agents.fact_checker import fact_checker
from agents.summarizer import summarizer
graph=StateGraph(ResearchState)
graph.add_node("researcher",researcher)
graph.add_node("fact_checker",fact_checker)
graph.add_node("summarizer",summarizer)
graph.add_edge(START,"researcher")
graph.add_edge("researcher","fact_checker")
graph.add_edge("fact_checker","summarizer")
graph.add_edge("summarizer",END)
app=graph.compile()