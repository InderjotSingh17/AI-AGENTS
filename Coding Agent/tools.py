from langchain_core.tools import tool
@tool
def explain_code(code:str)->str:
    """
    Explain what the given code does
    """
    return f"Explanation requested for:\n{code}"

@tool
def generate_test_cases(problem:str)->str:
    """
    generate test cases for a programming problem
    """
    return f"Test cases for: {problem}"

TOOLS=[
    explain_code,
    generate_test_cases,
]