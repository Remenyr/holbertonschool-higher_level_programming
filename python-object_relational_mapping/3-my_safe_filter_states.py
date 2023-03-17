#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], database=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name LIKE BINARY %s""", (argv[4],))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
