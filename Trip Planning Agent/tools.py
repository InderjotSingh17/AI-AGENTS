from langchain_core.tools import tool
@tool
def get_weather(city:str)->str:
    """
    Returns weather information for a city.
    """
    return f"The weather in {city} is sunny with a temperature of 28°C."

@tool
def search_hotels(city:str,budget:int)->str:
    """
    Search hotels within a given budget.
    """
    return(
        f"Found several hotels in {city} under ₹{budget} per night."
    )

@tool
def search_transport(origin:str,destination:str)->str:
    """
    Search transportation options.
    """
    return (
        f"Flights, trains and buses are available from "
        f"{origin} to {destination}."
    )

@tool
def estimate_budget(days:int,people:int)->str:
    """
    Estimate total trip budget.
    """
    total=days*people*4500
    return f"Estimated trip budget: ₹{total}"
