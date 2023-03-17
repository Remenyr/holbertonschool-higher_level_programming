#!/usr/bin/python3
"""
script that takes in an argument and displays all values
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], database=argv[3])
    cur = conn.cursor()
    cur.execute(
        """SELECT * FROM states
        WHERE name LIKE BINARY '{}'
        ORDER BY id ASC""".format(argv[4]))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
