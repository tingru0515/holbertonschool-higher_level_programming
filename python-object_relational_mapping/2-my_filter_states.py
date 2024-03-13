#!/usr/bin/python3
"""takes in an argument and displays all values in the table
where name matches the argument"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = {} ORDER BY id ASC".format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
