import requests
import os
from fastapi import FastAPI

from routes.football_data import router as football_data_router
from routes.odds import router as odds_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten for production
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(football_data_router)
app.include_router(odds_router)


@app.get("/")
def root():
    return {"app": "footy iq mvp",
            
            "docs": "/docs"
            }

@app.get("/health")
def health():
    return {"status": "ok"}





    

    