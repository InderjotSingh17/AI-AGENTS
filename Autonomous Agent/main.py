from agent import autonomous_agent 
def main():
    while True:
        query=input("\nYou:")
        if query.lower() in ["exit","quit"]:
            print("\nGoodBye")
            break
        response=autonomous_agent(query)
        print(f"\nAI: {response}")

if __name__=="__main__":
    main()