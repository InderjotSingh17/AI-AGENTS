from pydantic import BaseModel,Field
class RouteResponse(BaseModel):
    """
    Schema used by the Supervisor Agent to decide
    which specialist agent should handle the request.
    """
    agent:str=Field(
        description="The selected agent.Must be one of: Coding Agent, Research Agent, Math Agent."
    
    )