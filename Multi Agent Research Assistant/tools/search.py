from duckduckgo_search import DDGS
def search_web(query: str) -> str:
    print("Searching the Web")
    results = DDGS().text(query, max_results=5)
    output = ""
    for result in results:
        output += (
            f"Title: {result['title']}\n"
            f"Body: {result['body']}\n"
            f"Link: {result['href']}\n\n"
        )
    return output