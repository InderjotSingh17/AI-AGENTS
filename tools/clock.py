from langchain_core.tools import tool
from datetime import datetime
@tool
def current_time()->str:
    """
    returns the current local time
    """
    return datetime.now().strftime("%I:%M %p")