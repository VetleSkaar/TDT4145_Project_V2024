## Utility functions and variables

from operator import call
import sqlite3
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

# Clear terminal
def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')
DATABASE_LOCATION = "theater.db"


def open_db() -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    con = sqlite3.connect(DATABASE_LOCATION)
    cur = con.cursor()
    return con, cur