from fastapi import FastAPI

app = FastAPI(
    title="HackRice 15 Starter Code",
    description="A solid foundation for your hackathon project.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the HackRice 15 Starter Backend!"}

# Add routers
from backend.api.v1.api import api_router as api_router_v1

app.include_router(api_router_v1, prefix="/api/v1")