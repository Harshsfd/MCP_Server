from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI(title="MCP Server", version="1.0")

# ✅ CORS Middleware Fix
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # production में यहां specific domain डाल सकते हैं
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "MCP Server is running!"}