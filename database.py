import sqlite3  # built-in module for working with SQLite, no installation needed

conn = sqlite3.connect("football.db")  # creates football.db if it doesn't exist, or opens it if it does
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