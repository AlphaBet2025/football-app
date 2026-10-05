# Football Lineup & Fantasy Builder

A Python project that pulls real football data (squads, fixtures, odds) to:
1. Show predicted lineups with depth options and tactical tweaks for clubs
2. Power a fantasy-football-style planner with an odds-based fixture difficulty ticker

**Status:** early setup / learning project — starting with a single league (Premier League) before expanding.

## Tech Stack

- **Language:** Python
- **Data source:** [football-data.org](https://www.football-data.org/) API (squads, fixtures, competitions)
- **Backend:** FastAPI
- **Front-end:** Plain HTML/CSS + Jinja2 templates (no JS framework) — chosen deliberately to actually learn front-end fundamentals rather than relying on a Python-only UI tool like Streamlit
- **Database:** SQLite (local file, simple for a solo project)
- **Env management:** `python-dotenv` for API keys

## Setup Instructions

1. Clone this repo:
```
   git clone <your-repo-url>
   cd football-lineup-app
```

2. Install required packages:
```
   pip install requests python-dotenv fastapi uvicorn jinja2
```

3. Create a `.env` file in the project root (this file is git-ignored and never shared):
```
   FOOTBALL_API_KEY=your_actual_key_here
```
   Get your key by registering at [football-data.org](https://www.football-data.org/client/register).

4. Run the main script to fetch and store data:
```
   python main.py
```

5. Run the web app:
```
   python -m uvicorn app:app --reload
```
   Then visit `http://127.0.0.1:8000/squad/{club_id}` to view a club's squad (e.g. `/squad/65` for Manchester City).

**Never commit your `.env` file or share your API key.** The included `.gitignore` (Python template) already excludes it, along with `football.db` and `__pycache__`.

## Roadmap

- [x] Fetch one club's squad from the API and print it
- [x] Design `players` and `clubs` database schema
- [x] Store squad data in SQLite
- [x] Loop over all Premier League clubs
- [x] Build a basic FastAPI + Jinja2 page showing one club's squad as a list
- [ ] Lay players out positionally on an actual pitch graphic
- [ ] Add predicted lineup logic (based on minutes played / odds)
- [ ] Add tactical formation tweaks
- [ ] Add depth chart / bench alternates
- [ ] Build fixture difficulty ticker (odds-based)
- [ ] Build fantasy team planner (budget-based squad picking)
- [ ] Expand beyond one league

## Decisions Made

- Using SQLite, not Postgres, for now — simpler for a solo beginner project
- Starting with one league only to avoid API rate-limit/data-volume issues
- Commenting style: comment non-obvious concepts (e.g. what a cursor is, why a foreign key matters) rather than every single line — balances learning value against readability
- SQLite connection uses `check_same_thread=False` — needed because FastAPI runs request handlers in background threads, and SQLite otherwise locks a connection to the thread that created it. Fine for a solo local project; would need a different approach (e.g. a fresh connection per request) if this ever handled concurrent users.

## Open Questions

(none currently — resolved: API does represent position/formation per player via a `position` field; competition's `/teams` endpoint does include full squad data per club)

## Future Project Ideas (not started)

- Match outcome predictor (pandas, scikit-learn/XGBoost) — using historical PL data (possession, goals, defense, home advantage, matchups) to predict win/loss/draw
- Player value analyzer (pandas, scikit-learn/XGBoost) — estimate a player's "should-be" value from performance, age, position, contract to spot over/undervalued players
- AI player scout (pandas/scikit-learn + OpenAI API) — given a club's roster, weaknesses, and budget, suggest transfer targets; ML does the analysis, the API layer explains it in natural language
- Possibly combine all three into one PL analytics project later, once this project is more mature

## Session Log

Paste a short summary here at the end of each working session (what got done, what's next). If you ever start a fresh AI chat with no memory of this project, paste this whole README back to it first — that's enough context to pick up right where you left off.

**Sept 14 —** Project created. Repo set up, `.env` configured, planning done. Next: fetch first club's squad.

**Sept 16 —** First successful API call (Man City squad fetched, status 200). Decided against Streamlit in favor of FastAPI + plain HTML/CSS, specifically to learn real front-end skills for the pitch visual. Next: design SQLite schema for `players` and `clubs`.

**Sept 16 —** Created `database.py`, separate from `main.py`, to keep fetching and storage logic apart. Built `clubs` and `players` tables with a foreign key linking players to their club. Verified both tables exist in `football.db` with a temporary check query (since removed). Next: write insert logic so fetched squad data actually gets saved into these tables.

**Sept 22 —** Added `insert_club`, `insert_player`, and `get_all_players` functions to `database.py`, using `INSERT OR REPLACE` so re-running the script keeps data current instead of erroring on duplicates. Wired `main.py` to call these with the real Man City API response. Confirmed working — all 25 players saved to `football.db` with correct club linkage. Next: loop over all Premier League clubs instead of just one hardcoded team.

**Sept 22 —** Replaced the hardcoded single-team fetch with the `/v4/competitions/PL/teams` endpoint, which turned out to include full squad data per club already — no extra per-team requests needed. Looped over all 20 clubs and their squads, saving everything to the database in one run. Verified the club list against the actual current (2026-27) season lineup. Next: build a simple UI showing one club's squad on a pitch.

**Oct 4 —** Built the first FastAPI route (`/squad/{club_id}`) and Jinja2 template (`squad.html`) rendering a club's squad as a plain list. Added `get_players_by_club` and `get_club_name` to `database.py`. Fixed two bugs: SQLite's single-thread restriction (`check_same_thread=False`) and a library version mismatch in how `TemplateResponse` takes arguments. Confirmed working end-to-end at `/squad/65`. Next: lay players out positionally on an actual pitch graphic.