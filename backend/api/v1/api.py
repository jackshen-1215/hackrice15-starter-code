from fastapi import APIRouter

from backend.api.v1.endpoints import auth, llm

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(llm.router, prefix="/llm", tags=["llm"])