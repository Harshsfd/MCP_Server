from fastapi import FastAPI
from .routes import router

app = FastAPI(title="MCP Server - Local Tools")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "MCP Server is running 🚀"}
