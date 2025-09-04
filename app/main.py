from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router

app = FastAPI(title="MCP Server - Local Tools")

# ---- CORS setup ----
origins = [
    "http://localhost:3000",  # React frontend
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # allow frontend origin
    allow_credentials=True,
    allow_methods=["*"],         # allow GET, POST, PUT, DELETE
    allow_headers=["*"],
)

# ---- Include API routes ----
app.include_router(router)

@app.get("/")
def home():
    return {"message": "MCP Server is running 🚀 With Frontend"}
