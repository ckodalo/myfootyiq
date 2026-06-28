import requests
import os
from fastapi import FastAPI

from routes.football_data import router as football_data_router
from routes.odds import router as odds_router

app = FastAPI()

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





    

    