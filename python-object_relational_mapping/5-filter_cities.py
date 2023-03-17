#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], database=argv[3])
    cur = conn.cursor()
    cur.execute(
        """SELECT cities.name
        FROM cities JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE BINARY %s
        ORDER BY cities.id""", (argv[4],))

    query_rows = cur.fetchall()
    st = 0
    for row in query_rows:
        for name in row:
            print(name, end="" if row ==
                  query_rows[-1] and name == row[-1] else ", ")
    print()

    cur.close()
    conn.close()