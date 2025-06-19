from sqlalchemy.orm import Session
from .base import CRUDBase
from backend.track_specific.entrepreneurship.models.market_research import MarketResearch
from backend.track_specific.entrepreneurship.schemas.market_research import MarketResearchCreate, MarketResearchUpdate

class CRUDMarketResearch(CRUDBase[MarketResearch, MarketResearchCreate, MarketResearchUpdate]):
    def get_by_user(self, db: Session, *, user_id: int) -> list[MarketResearch]:
        return db.query(MarketResearch).filter(MarketResearch.user_id == user_id).all()

market_research = CRUDMarketResearch(MarketResearch)