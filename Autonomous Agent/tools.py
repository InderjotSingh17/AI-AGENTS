from langchain_core.tools import tool
@tool
def add(a:int,b:int)->int:
    """
    add two numbers.
    """
    return a+b

@tool
def subtract(a:int,b:int)->int:
    """
    subtract two numbers.
    """
    return a-b

@tool
def multiply(a:int,b:int)->int:
    """
    multiply two numbers
    """
    return a*b

@tool
def divide(a:int,b:int)->int:
    """
    divide two numbers.
    """
    if b==0:
        return "cannot divide by zero"
    return a/b

TOOLS=[
    add,
    subtract,
    multiply,
    divide
]