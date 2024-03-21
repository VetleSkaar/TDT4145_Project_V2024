from datetime import datetime
from util import open_db
with open("files needed/hovedscenen.txt") as fh:
    data = fh.readlines()

date = datetime.strptime(data.pop(0).strip(), "Dato %Y-%m-%d").strftime("%Y-%m-%d")
print(date)

data.pop(0)
gallery = list(map(str.strip, data[:4]))
data = data[4:]
print(gallery)

data.pop(0)
parkett = list(map(str.strip, data))
print(parkett)


gallery = list(enumerate(reversed(gallery), 1))
parkett = list(enumerate(reversed(parkett), 1))
print(parkett)
con, cur = open_db()

for row, seats in parkett:
    print(seats)
    for seat, _ in filter(lambda s: s[1] == "1", enumerate(seats, 1)):
        print(row, seat)
        cur.execute("UPDATE Seat SET Available = false WHERE SeatNumber = ? AND SeatRow = ? AND PerformanceID = (SELECT ID FROM Performance WHERE PerformanceDate LIKE ? AND TheaterHall = 'Hovedscenen')", (seat, row, date + "%"))

print(cur.execute("SELECT SeatRow, SeatNumber FROM SEAT WHERE Available = false").fetchall())

con.rollback()