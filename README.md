# Football Lineup & Fantasy Builder

A Python project that pulls real football data (squads, fixtures, odds) to:
1. Show predicted lineups with depth options and tactical tweaks for clubs
2. Power a fantasy-football-style planner with an odds-based fixture difficulty ticker

**Status:** early setup / learning project — starting with a single league (Premier League) before expanding.

## Tech Stack

- **Language:** Python
- **Data source:** [football-data.org](https://www.football-data.org/) API (squads, fixtures, competitions)
- **Backend/UI:** FastAPI and/or Streamlit (TBD as the project grows)
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
   pip install requests python-dotenv
   ```

3. Create a `.env` file in the project root (this file is git-ignored and never shared):
   ```
   FOOTBALL_API_KEY=your_actual_key_here
   ```
   Get your key by registering at [football-data.org](https://www.football-data.org/client/register).

4. Run the main script:
   ```
   python main.py
   ```

**Never commit your `.env` file or share your API key.** The included `.gitignore` (Python template) already excludes it.

## Roadmap

- [ ] Fetch one club's squad from the API and print it
- [ ] Design `players` and `clubs` database schema
- [ ] Store squad data in SQLite
- [ ] Loop over all Premier League clubs
- [ ] Build a simple UI showing one club's squad on a pitch
- [ ] Add predicted lineup logic (based on minutes played / odds)
- [ ] Add tactical formation tweaks
- [ ] Add depth chart / bench alternates
- [ ] Build fixture difficulty ticker (odds-based)
- [ ] Build fantasy team planner (budget-based squad picking)
- [ ] Expand beyond one league

## Decisions Made

- Using SQLite, not Postgres, for now — simpler for a solo beginner project
- Starting with one league only to avoid API rate-limit/data-volume issues

## Open Questions

- How does the API represent formation/position in the squad response? (check once we fetch real data)

## Session Log

Paste a short summary here at the end of each working session (what got done, what's next). If you ever start a fresh AI chat with no memory of this project, paste this whole README back to it first — that's enough context to pick up right where you left off.

**[Date] —** Project created. Repo set up, `.env` configured, planning done. Next: fetch first club's squad.