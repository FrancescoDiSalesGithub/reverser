import sqlite3


class reverseshell_data:

    def __init__(self) -> None:
            try:
                self.__connection=sqlite3.connect("enviroments.db")
            except:
                
                newdb = open("enviroments.db","w")
                newdb.close()

                self.__connection=sqlite3.connect("enviroments.db")

                tables_file = open("sql/tables.sql","r")
                table_lines = tables_file.readlines()
                tables_file.close()
                
                cursor = self.__connection.cursor()
                
       

    def execute(self,program):
        cursor = self.__connection.cursor()
        for row in cursor.execute("SELECT * from shell where program=%s",(program)):
            print(row)
    
    def close_connection(self):
        self.__connection.close()

    