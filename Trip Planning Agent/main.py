from planner import create_plan
from executor import execute
def main():
    goal=input("enter your travel goal:")
    plan=create_plan(goal)
    print("\nGenerated Plan\n")
    for i, step in enumerate(plan.steps, start=1):
        print(f"{i}. {step}")
    print("\nExecuting Plan...\n")
    result = execute(plan)
    print("\nFinal Travel Plan\n")
    print(result)
if __name__=="__main__":
    main()
