from .base_class import Base
from .session import engine

# Import all the models, so that Base has them before being
# imported by Alembic
# from ..models.user import User  # noqa

def init_db():
    # Tables are created with Alembic, this is for development only
    Base.metadata.create_all(bind=engine)