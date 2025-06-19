from fastapi import APIRouter

from backend.track_specific.entrepreneurship.api.endpoints import market_research

api_router = APIRouter()
api_router.include_router(market_research.router, prefix="/market_research", tags=["market_research"])