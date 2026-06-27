import requests
import os
from fastapi import FastAPI

fdata_matches = 'https://api.football-data.org/v4/matches'
fdata_areas = 'https://api.football-data.org/v4/areas'
fdata_competitions = 'https://api.football-data.org/v4/competitions'
fdata_teams = 'https://api.football-data.org/v4/teams'
fdata_trends = 'https://api.football-data.org/v4/trends'
fdata_persons = 'https://api.football-data.org/v4/persons'

fdata_key = os.getenv("FK", "")

app = FastAPI()

@app.get('/matches')
def fetch_matches():

    headers = {
        "X-Auth-Token": "8aec8f2dc27743fe8e5240f112c89dc3"
    }

    response = requests.get(fdata_matches, headers=headers)

    if response.status_code == 200:
        data = response.json()

        return data
        
        # for match in data['matches']:
        #     print(match) 

@app.get('/areas')
def fetch_areas():

    headers = {
        "X-Auth-Token": "8aec8f2dc27743fe8e5240f112c89dc3"
    }  

    response = requests.get(fdata_areas, headers=headers)

    if response.status_code == 200:
        data = response.json()

        return data


@app.get('/competitions')
def fetch_competitions():
    
    headers = {
        "X-Auth-Token": "8aec8f2dc27743fe8e5240f112c89dc3"
    } 

    response = requests.get(fdata_competitions, headers = headers) 

    if response. status_code  == 200: 
        data = response.json()

        return data

@app.get('/teams')
def fetch_teams():
    headers = {
        "X-Auth-Token": "8aec8f2dc27743fe8e5240f112c89dc3"
    } 

    response = requests.get(fdata_teams, headers = headers) 

    if response.status_code  == 200: 
        data = response.json()

        return data["teams"]

@app.get('/teams/{id}')
def fetch_teams(id: int):
    headers = {
        "X-Auth-Token": "8aec8f2dc27743fe8e5240f112c89dc3"
    } 

    
    #response = requests.get(f"{fdata_teams}/{id}", headers=headers)

    response = requests.get(fdata_teams, headers = headers)

    if response.status_code == 200: 
        data = response.json()

        for team in data["teams"]:
            if team["id"] == id:
                return team
    
        return {"Error": f"Team with id {id} not found"}


@app.get('/trends')
def fetch_teams():
    headers = {
        "X-Auth-Token": "8aec8f2dc27743fe8e5240f112c89dc3"
    } 

    response = requests.get(fdata_trends, headers = headers) 

    if response. status_code  == 200: 
        data = response.json()

        return data
    
@app.get('/persons')
def fetch_teams():
    headers = {
        "X-Auth-Token": "8aec8f2dc27743fe8e5240f112c89dc3"
    } 

    response = requests.get(fdata_persons, headers = headers) 

    if response. status_code  == 200: 
        data = response.json()

        return data



    

    