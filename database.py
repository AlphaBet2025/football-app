import sqlite3  # built-in module for working with SQLite, no installation needed

conn = sqlite3.connect("football.db", check_same_thread=False)  # creates football.db if it doesn't exist, or opens it if it does
# check_same_thread=False allows FastAPI's background threads to reuse this same connection
cursor = conn.cursor()  # the tool used to run SQL commands through this connection

cursor.execute("""
CREATE TABLE IF NOT EXISTS clubs (
    id INTEGER PRIMARY KEY,
    name TEXT,
    venue TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY,
    name TEXT,
    position TEXT,
    date_of_birth TEXT,
    nationality TEXT,
    club_id INTEGER,
    FOREIGN KEY (club_id) REFERENCES clubs(id) -- ties club_id to clubs.id, linking each player to their club
)
""")

conn.commit() # saves changes to the database

def insert_club(club_id, name, venue):
    cursor.execute("INSERT OR REPLACE INTO clubs (id, name, venue) VALUES (?, ?, ?)", (club_id, name, venue))
    conn.commit()

def insert_player(player_id, name, position, date_of_birth, nationality, club_id):
    cursor.execute("INSERT OR REPLACE INTO players (id, name, position, date_of_birth, nationality, club_id) VALUES (?, ?, ?, ?, ?, ?)", (player_id, name, position, date_of_birth, nationality, club_id))
    conn.commit()

def get_all_players():
    cursor.execute("SELECT * FROM players")
    return cursor.fetchall()  # returns a list of tuples, each tuple is a row in the players table

def get_players_by_club(club_id):
    cursor.execute("SELECT * FROM players WHERE club_id = ?", (club_id,))
    return cursor.fetchall()  # returns a list of tuples, each tuple is a row in the players table for the specified club

def get_club_name(club_id):
    cursor.execute("SELECT name FROM clubs WHERE id = ?", (club_id,))
    result = cursor.fetchone()
    return result[0] if result else None  # returns the club name if found, otherwise None