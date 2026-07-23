from langchain_core.tools import tool
@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@tool
def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

@tool
def divide(a: int, b: int):
    """Divide two numbers."""
    if b == 0:
        return "Cannot divide by zero."
    return a / b

TOOLS = [
    add,
    subtract,
    multiply,
    divide
]