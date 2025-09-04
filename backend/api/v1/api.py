from fastapi import APIRouter

from backend.api.v1.endpoints import auth, llm, tasks

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(llm.router, prefix="/llm", tags=["llm"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])