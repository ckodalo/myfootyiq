import requests
import os
from fastapi import FastAPI

fdata_url = 'https://api.football-data.org/v4/matches'
fdata_key = os.getenv("FK", "")

app = FastAPI()

@app.get('/matches')
def fetch_matches():

    headers = {
        "X-Auth-Token": "8aec8f2dc27743fe8e5240f112c89dc3"
    }

    response = requests.get(fdata_url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        return data
        
        # for match in data['matches']:
        #     print(match) 
            