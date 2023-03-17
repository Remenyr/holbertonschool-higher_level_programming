#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], database=argv[3])
    cur = conn.cursor()
    cur.execute(
        """SELECT cities.id, cities.name, states.name
        FROM states JOIN cities ON states.id = cities.state_id
        ORDER BY cities.id""")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
