import requests  # sends web requests, lets Python talk to APIs
from dotenv import load_dotenv
import os
from database import insert_club, insert_player, get_all_players

load_dotenv()  # loads variables from .env
api_key = os.getenv("FOOTBALL_API_KEY")

url = "https://api.football-data.org/v4/teams/65"  # 65 = Man City's ID in football-data.org's system
headers = {"X-Auth-Token": api_key}  # attaches your API key so the request is recognized

response = requests.get(url, headers=headers)

data = response.json()  # converts the JSON response into a Python dictionary

insert_club(data["id"], data["name"], data["venue"])

for player in data["squad"]:
    insert_player(
        player["id"],
        player["name"],
        player["position"],
        player["dateOfBirth"],  
        player["nationality"],
        data["id"]  # club_id, linking the player to their club
    )

print("Data saved to database.")

teams_url = "https://api.football-data.org/v4/competitions/PL/teams"
teams_response = requests.get(teams_url, headers=headers)
teams_data = teams_response.json()

for team in teams_data["teams"]:
    insert_club(team["id"], team["name"], team["venue"])

    for player in team["squad"]:
        insert_player(
            player["id"],
            player["name"],
            player["position"],
            player["dateOfBirth"],
            player["nationality"],
            team["id"]
        )

    print(f"Saved {team['name']} ({len(team['squad'])} players)")

print("All Premier League clubs saved.")