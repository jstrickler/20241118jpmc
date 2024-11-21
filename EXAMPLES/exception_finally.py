import sqlite3

conn = None
try:
    conn = sqlite3.connect("wombats.db")
except sqlite3.DatabaseError as err:
    print(err)
    exit(1)  # exit program
else:
    pass # use the db here
finally:
    if conn:
        conn.close()
