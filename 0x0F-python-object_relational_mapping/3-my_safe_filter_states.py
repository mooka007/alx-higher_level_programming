#!/usr/bin/python3
""" script that takes in arguments and displays all values """

import MySQLdb
from sys import argv

if __name__ = '__main__':

    HOST = 'localhost'
    PORT = '3306'
    MY_USER = argv[1]
    MY_PSWD = argv[2]
    MY_DB = argv[3]
    NAME = argv[4]
    db = MySQLdb.connect(host=HOST, user=MY_USER, password=MY_PSWD,
                         db=MY_DB, port=PORT)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id", (NAME,))
    row_query = cur.fetchall()
    for r_pritn in row_query:
        print(r_pritn)
    cur.close()
    db.close()
