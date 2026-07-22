from pydantic import BaseModel,Field
class CodeResponse(BaseModel):
    explanation:str=Field(description="brief explanation of the solution")
    code:str=Field(description="generated source code")
    language:str=Field(description="programming language used")