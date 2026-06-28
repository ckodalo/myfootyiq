import requests
import os
from fastapi import APIRouter

from dotenv import load_dotenv

load_dotenv()

FOOTBALL_DATA_KEY = os.getenv("FOOTBALL_DATA_KEY", "")
ODDS_API_KEY = os.getenv("ODDS_API_KEY", "")

FOOTBALL_DATA_BASE = "https://api.football-data.org/v4"
ODDS_API_BASE = "https://api.the-odds-api.com/v4"

router = APIRouter()

@router.get("/odds")
def GetAllOdds():

    #params
    sport = "soccer_fifa_world_cup"
    regions = "uk"
    markets = "outright"

    response = requests.get(f"{ODDS_API_BASE}/sports/{sport}/odds", params={"apiKey":ODDS_API_KEY, "regions":regions, "market":markets})

    if response.status_code == 200:
        return response.json()
    
    return {"Error": f"Unsuccessful response"}

@router.get("/sports")    
def GetAllSports():
    
    response = requests.get(f"{ODDS_API_BASE}/sports", params={"apiKey":ODDS_API_KEY})

    if response.status_code == 200:
        return response.json()
    
