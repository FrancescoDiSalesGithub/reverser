import sqlite3
import dbhandler
import sys

if __name__ == "__main__":

    try:

        handler = dbhandler.reverseshell_data()
        handler.execute()
        handler.close_connection()

    except:
        raise Exception("Something bad happened")

    pass