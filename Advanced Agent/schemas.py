from pydantic import BaseModel,Field
class ReflectionResponse(BaseModel):
    is_correct: bool = Field(
        description="True if the answer is correct, otherwise False."
    )
    feedback: str = Field(
        description="Feedback explaining why the answer is correct or how it can be improved."
    )