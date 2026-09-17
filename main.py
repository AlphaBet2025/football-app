import requests
from dotenv import load_dotenv
import os 

load_dotenv()
api_key = os.getenv("FOOTBALL_API_KEY")

url = "https://api.football-data.org/v4/teams/65"
headers = {"X-Auth-Token": api_key}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())