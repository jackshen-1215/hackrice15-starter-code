from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="HackRice 15 Starter Code",
    description="A solid foundation for your hackathon project.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health():
    return {"status": "ok"}

# Add routers
from backend.api.v1.api import api_router as api_router_v1

app.include_router(api_router_v1, prefix="/api/v1")

# Serve frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

from backend.db.session import engine
from backend.db.base_class import Base
import backend.models.user  # ensure model is registered
import backend.models.task  # ensure model is registered

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)