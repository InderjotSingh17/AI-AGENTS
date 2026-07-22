from agent import coding_agent 
def main():
    query=input("enter your coding question:")
    response=coding_agent(query)
    print("\nExplanation:\n")
    print(response.explanation)
    print("\nLanguage:\n")
    print(response.language)
    print("\nCode:\n")
    print(response.code)

if __name__=="__main__":
    main()