from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from database import get_players_by_club, get_club_name

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/squad/{club_id}") # {club_id} is a path parameter — whatever number is in the URL gets passed into the function below
def show_squad(request: Request, club_id: int):
    club_name = get_club_name(club_id)
    players = get_players_by_club(club_id)
    return templates.TemplateResponse(request, "squad.html", {  # request must be passed positionally in this Starlette version, not as a dict key
        "club_name": club_name,
        "players": players
    })