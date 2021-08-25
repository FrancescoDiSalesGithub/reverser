import sqlite3
import dbhandler
import sys

if __name__ == "__main__":

    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("insert the program you want to generate the reverse shell")
        sys.exit(-1)

    try:

        handler = dbhandler.reverseshell_data()
        handler.execute(sys.argv[1])
        handler.close_connection()

    except:
        raise Exception("Something bad happened")

    pass