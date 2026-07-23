from llm import llm
from prompts import REFLECTION_PROMPT
from schemas import ReflectionResponse
structured_llm=llm.with_structured_output(ReflectionResponse)
def reflection(query: str, answer: str):
    prompt = REFLECTION_PROMPT.invoke(
        {
            "query": query,
            "answer": answer
        }
    )
    response=structured_llm.invoke(prompt)
    return response