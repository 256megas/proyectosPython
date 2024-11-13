import mysql.connector
from mysql.connector import errorcode


class mySQLCon:
    __TABLES = {}
    __TABLES['usuarios'] = (
        "CREATE TABLE usuarios ( user_num int(11) NOT NULL AUTO_INCREMENT, nombre varchar(14) NOT NULL, apellido varchar(16) NOT NULL, PRIMARY KEY (user_num));")

    def __init__(self):
        self.__conector = mysql.connector.connect(user='root', password='',
                                                  host='127.0.0.1',
                                                  database='testPython')
        self.__cur = self.__conector.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__conector.connection.close()

    def createTables(self):
        for eachTable in self.__TABLES:
            table_description = self.__TABLES[eachTable]
            try:
                print("CREANDO TABLA {}: ".format(eachTable), end='')
                self.__cur.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("YA EXISTE.")
                else:
                    print(err.msg)
            else:
                print("OK")

    def createUser(self, nombre, apellido):
        __createUser = "INSERT INTO usuarios (nombre, apellido) VALUES ('" + \
            nombre+"','" + apellido+"');"
        try:
            print(f"CREANDO USUARIO {nombre}")
            self.__cur.execute(__createUser)
            self.__conector.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("YA EXISTE.")
            else:
                print(err.msg)
