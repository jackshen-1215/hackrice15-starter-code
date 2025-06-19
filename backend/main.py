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
from api.v1.endpoints import auth, llm

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(llm.router, prefix="/api/v1/llm", tags=["llm"])