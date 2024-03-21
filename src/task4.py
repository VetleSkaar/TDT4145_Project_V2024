## Take in date
## Find all performances on this date and how many tickets are sold to each performance

from datetime import datetime
from util import TIME_FORMAT, DATABASE_LOCATION
import sqlite3

con = sqlite3.connect(DATABASE_LOCATION)
cur = con.cursor()

print("Skriv inn dato \n")
raw_date = "2024-02-01" # input("Dato (YYYY-MM-DD): ")
print(raw_date)
input_date = datetime.strptime(raw_date, "%Y-%m-%d").strftime("%Y-%m-%d")

performance_query = '''
SELECT PerformanceID, COUNT(ALL Available)
    FROM Seat 
WHERE
    PerformanceID IN (SELECT ID FROM Performance WHERE PerformanceDate LIKE ?)
    AND Available = false
GROUP BY PerformanceID
'''
raw_performances = cur.execute(performance_query, (input_date + "%", )).fetchall()

print(raw_performances)