from langchain_core.tools import tool
@tool
def get_weather(city:str)->str:
    """
    Returns the current weather of a city.
    This is a dummy tool for learning purpose.
    """
    weather_data={
        "delhi": "38°C, Sunny",
        "mumbai": "30°C, Humid",
        "bangalore": "27°C, Cloudy",
        "chandigarh": "35°C, Sunny"
    }
    return weather_data.get(
        city.lower(),
        "Weather not available."
    )