import requests  # sends web requests, lets Python talk to APIs
from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env
api_key = os.getenv("FOOTBALL_API_KEY")

url = "https://api.football-data.org/v4/teams/65"  # 65 = Man City's ID in football-data.org's system
headers = {"X-Auth-Token": api_key}  # attaches your API key so the request is recognized

response = requests.get(url, headers=headers)

print(response.status_code)  # 200 = success, 401/403 = key problem, 404 = wrong URL
print(response.json())