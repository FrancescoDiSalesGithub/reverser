import sqlite3
import base64

class reverseshell_data:

    def __init__(self) -> None:
        self.__connection=sqlite3.connect("enviroments.db")
                
    def get_all_applications(self):
        
        cursor = self.__connection.cursor()
        for line in cursor.execute("select program from program"):
            print(line[0])


    def execute(self,program):

        try:
            cursor = self.__connection.cursor()
            for row in cursor.execute("SELECT s.command from program p,shell s where p.program = ? and p.id_program=s.id_program",[program]):
                print(base64.b64decode(row[0]).decode("utf-8","ignore"))
        except:
            
            self.create_table_setup("tableprogram")
            self.create_table_setup("tableshell")
    
            self.insert_setup("programs")
            self.insert_setup("shell")

            self.finish_creation()
            print("During the research the tables did not exist. Try to run the program again")


    def create_table_setup(self,name_table):

        tables_file = open("sql/{}.sql".format(str(name_table)),"r")
        table_lines = tables_file.readlines()
        tables_file.close()

        table_string = ""
        for line in table_lines:
            table_string = table_string + line

        self.__connection.execute(table_string)

    def insert_setup(self,name_insert):

        programs_file = open("sql/{}.sql".format(str(name_insert)),"r")
        programs_line = programs_file.readlines()
        programs_file.close()

        for line in programs_line:
            self.__connection.execute(line)

    def finish_creation(self):
        self.__connection.commit()

    def close_connection(self):
        self.__connection.close()

    