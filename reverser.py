import dbhandler
import sys

if __name__ == "__main__":

    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("insert the program you want to generate the reverse shell")
        sys.exit(-1)

    if sys.argv[1] == "help" or sys.argv[1] == "--help":
        print("usage: python3 reverser [application]")
        print("")
        print("possible applications: ")

        handler = dbhandler.reverseshell_data()
        handler.get_all_applications()
        handler.close_connection()
        
        sys.exit(0)

    try:

        handler = dbhandler.reverseshell_data()
        handler.execute(sys.argv[1])
        handler.close_connection()

    except:
        raise Exception("Something bad happened")
