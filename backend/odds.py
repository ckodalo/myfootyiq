import requests
import os
from fastapi import FastAPI


from dotenv import load_dotenv

load_dotenv()

FOOTBALL_DATA_KEY = os.getenv("FOOTBALL_DATA_KEY", "")
ODDS_API_KEY = os.getenv("ODDS_API_KEY", "")

FOOTBALL_DATA_BASE = "https://api.football-data.org/v4"
ODDS_API_BASE = "https://api.the-odds-api.com/v4"