from pydantic import BaseModel,Field 
class Plan(BaseModel):
    goal:str=Field(description="Overall Goal")
    steps:list[str]=Field(description="Ordered list of steps")