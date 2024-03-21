from datetime import datetime
from util import TIME_FORMAT, DATABASE_LOCATION
import sqlite3
from pathlib import Path


# Resets Database if run
Path(DATABASE_LOCATION).unlink(True)
con = sqlite3.connect(DATABASE_LOCATION)
cur = con.cursor()

cur.executescript(Path("sql/schema.sql").read_text())
con.commit()

# Insert Plays
cur.execute('''INSERT INTO Play (Title, Acts) 
                VALUES ("Kongsemnene", 5)''')

cur.execute('''INSERT INTO Play (Title, Acts) 
                VALUES ("Størst av alt er kjærligheten", 1)''')

con.commit()


# Insert Performances of plays

time_1 = datetime(2024, 2, 1, 19).strftime(TIME_FORMAT)
time_2 = datetime(2024, 2, 3, 18, 30).strftime(TIME_FORMAT)

performance_query = '''INSERT INTO Performance (PlayID, TheaterHall, PerformanceDate) 
                VALUES (?,?,?)'''

performance_data = [
    (0, "Hovedscenen", time_1),
    (1, "Gamle Scene", time_2)
]

cur.executemany(performance_query, performance_data)

con.commit()


# Insert Seats for each performance
invalid_seats = (467, 468, 469, 470, 495, 496, 497, 498)
seat_query = '''INSERT INTO Seat (PerformanceID, SeatNumber, SeatRow, Area, Available) 
                VALUES (?,?,?,?, true)'''

# Hovedscenen Seats
queries = []
for performance_id,  in cur.execute("SELECT ID from Performance WHERE TheaterHall = 'Hovedscenen'").fetchall():
    print(performance_id)
    for i in range(1, 524):
        if i in invalid_seats:
            continue

        queries.append((performance_id, i, (i//28)+1, "Hovedscenen"))

cur.executemany(seat_query, queries)
con.commit()

# Gamle Scenen Seats
gamlescene_seats = {"Parkett": [18, 16, 17, 18, 18, 17, 18, 17, 17, 14],
                    "Balkong": [28, 27, 22, 17],
                    "Galleri": [33, 18, 17]}

queries = []
for performance_id, in cur.execute("SELECT ID from Performance WHERE TheaterHall = 'Gamle Scene'").fetchall():
    for area, seats in gamlescene_seats.items():
        for row, seat_amount in enumerate(seats):
            for i in range(1, seat_amount):
                queries.append((performance_id, i, row+1, area))

cur.executemany(seat_query, queries)
con.commit()

# Adds Roles and acts to TheaterRole and PresentIn Tables
with open("files needed/roller.txt", "r") as fh:
    roles_raw = fh.read().split("\n\n")

roles = []
for raw in roles_raw:
    name, acts = raw.split("\n")

    acts = {int(act) for act in acts.split(",")}
    roles.append((name, acts))

role_query = """INSERT INTO TheaterRole (RoleName, PlayID) VALUES (?, ?) RETURNING ID"""
apperance_query = """INSERT INTO PresentIn (RoleID, Act) VALUES (?, ?)"""
for name, acts in roles:
    role_id, = cur.execute(role_query, (name, 0)).fetchone()

    cur.executemany(apperance_query, [(role_id, act) for act in acts])

con.commit()


# Andre medvirkende

# CONTRIBUTORS

