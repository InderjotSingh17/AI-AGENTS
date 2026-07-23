from agent import advanced_agent
def main():
    while True:
        query=input("\nYou: ")
        if query.lower() in ["exit", "quit"]:
            print("\nGoodbye!")
            break
        response=advanced_agent(query)
        print(f"\nAI: {response}")

if __name__=="__main__":
    main()