#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities INNER JOIN states \
                ON states.id = cities.state_id ORDER BY cities.id ASC")
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()
