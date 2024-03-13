#!/usr/bin/python3
"""takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT cities.name FROM states \
            INNER JOIN cities ON states.id = cities.state_id \
            WHERE BINARY states.name = %s ORDER BY cities.id ASC"
    state_name = sys.argv[4]
    cur.execute(query, (state_name,))
    cities = cur.fetchall()
    city_names = ", ".join(city[0] for city in cities)
    print(city_names)
    cur.close()
    db.close()
