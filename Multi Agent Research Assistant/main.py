from graph.builder import app
initial_state={
    "query": "Research the impact of Artificial Intelligence in Healthcare.",
    "research": "",
    "verified_research": "",
    "summary": ""
}
result=app.invoke(initial_state)
print("\n" + "=" * 60)
print("FINAL SUMMARY")
print("=" * 60)

print(result["summary"])