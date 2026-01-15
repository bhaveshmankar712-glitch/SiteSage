from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.audit_api import router as audit_router
from app.api.health_api import router as health_router
import os

app = FastAPI(title="SiteSage ApI", version="0.1.0")


origins = os.getenv("CORS_ORIGINS", "").split(",")
origins.append("https://site-sage-delta.vercel.app")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in origins if o],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(health_router)
app.include_router(audit_router)


@app.get("/")
async def greetings():
    return "Welcome to SiteSage"
