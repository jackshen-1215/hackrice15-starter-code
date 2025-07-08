from fastapi import APIRouter, Depends
from pydantic import BaseModel

from backend.ai.factory import get_llm_provider
from backend.api import deps

router = APIRouter()

class LLMRequest(BaseModel):
    provider: str
    prompt: str

@router.post("/chat")
def chat(
    request: LLMRequest,
    # current_user: models.User = Depends(deps.get_current_user) # Uncomment to require auth
):
    """
    Get a response from a specified LLM provider.
    """
    try:
        llm_provider = get_llm_provider(request.provider)
        response = llm_provider.get_response(request.prompt)
        return {"response": response}
    except ValueError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}