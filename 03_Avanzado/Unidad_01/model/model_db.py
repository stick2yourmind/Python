import mysql.connector
from peewee import *


def update_where_id_my_sql(my_sql_host, my_sql_user, my_sql_pass, my_sql_db, my_sql_table,
                           columns_name_list, columns_value_list):
    """
Update a register by matching its id.

Parameters
----------
my_sql_host : str
    MySQL's host.
my_sql_user : str
    User's name.
my_sql_pass : str
    User's password.
my_sql_db : str
    Database to update.
my_sql_table : str
    Table's name of the database to update.
columns_name_list : str
    List of strings. Each element of the list contains the name of the columns to update.
    First element contains id of register to update.
    columns_name_list = [id column's name, second column's name, third column's name, ...]
    Example:
    ``columns_name_list = ["id", "titulo", "ruta", "descripcion"]``
columns_value_list : str
    List of strings. Each element of the list contains the value of the columns to update.
    First element contains id of register to update.
    columns_value_list = [id column's value, second column's value, third column's value, ...]
    Example:
    ``columns_value_list = ["12", "titulo a actualizar", "ruta a actualizar",`` \n
    ``"descripcion a actualizar"]``

Returns
-------
int
    ``-1`` if columns_name_list's length does not match with columns_value_list's length
int
    ``0`` if new register if identical to older
int
    Number of registers have been updated

"""
    print(46 * "-" + "update_where_id_my_sql method" + 46 * "-")
    my_db = mysql.connector.connect(
        host=my_sql_host,
        user=my_sql_user,
        passwd=my_sql_pass,
        database=my_sql_db
    )
    my_cursor = my_db.cursor()
    # UPDATE se aplica si y solo si el registro ya existe previamente
    if len(columns_name_list) == len(columns_value_list):
        sql = "UPDATE " + my_sql_table + " SET "
        for i in range(1, len(columns_name_list)):
            sql += columns_name_list[i] + " = "
            sql += "'" + columns_value_list[i] + "' "
            if i < len(columns_name_list) - 1:
                sql += ", "
        sql += " WHERE "
        sql += columns_name_list[0] + " = " + columns_value_list[0]
        print(sql)
        my_cursor.execute(sql)
        my_db.commit()
        aux = my_cursor.rowcount
        my_cursor.close()
        my_db.close()
        print("return: \n")
        print(aux)
        print(120 * "-")
        return aux
    else:
        print("return: \n")
        print("-1")
        print(120 * "-")
        return -1


def create_db_my_sql(my_sql_host, my_sql_user, my_sql_pass, my_sql_db):
    """
Create a database. Its name will be my_sql_db.

Parameters
----------
my_sql_host : str
    MySQL's host.
my_sql_user : str
    User of host.
my_sql_pass : str
    User's password.
my_sql_db : str
    Database's name to create.

Returns
-------
None : None
    has no return

    """
    print(49 * "-" + "create_db_my_sql method" + 49 * "-")
    my_db = mysql.connector.connect(
        host=my_sql_host,
        user=my_sql_user,
        passwd=my_sql_pass)
    my_cursor = my_db.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS " + my_sql_db)
    my_db.commit()
    my_cursor.close()
    my_db.close()
    print("Has no return")
    print(120 * "-")


def create_table_my_sql(my_sql_host, my_sql_user, my_sql_pass, my_sql_db, my_sql_table, my_sql_struct=""):
    """
Create a table. Its name will be my_sql_table.

Note
----
    Creates a table with the following structure by default:
    ``"CREATE TABLE IF NOT EXISTS " + my_sql_table + " ( id int(11) NOT NULL \`` \n
    ``PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, ruta \`` \n
    ``varchar(128) COLLATE utf8_spanish2_ci NOT NULL, descripcion text COLLATE \`` \n
    ``utf8_spanish2_ci NOT NULL )"``

Parameters
----------
my_sql_host : str
    MySQL's host.
my_sql_user : str
    User of host.
my_sql_pass : str
    User's password.
my_sql_db : str
    Database's name to update.
my_sql_table : str
    Table's name
my_sql_struct : str
    Estructure of the table if it is not specified, default structure will be applied

Returns
-------
None : None
    has no return

    """
    print(47 * "-" + "Create_Table_MySQL method" + 48 * "-")
    structure = "CREATE TABLE IF NOT EXISTS " + my_sql_table + " ( id int(11) NOT NULL \
PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, ruta \
varchar(128) COLLATE utf8_spanish2_ci NOT NULL, descripcion text COLLATE \
utf8_spanish2_ci NOT NULL )"
    my_db = mysql.connector.connect(
        host=my_sql_host,
        user=my_sql_user,
        passwd=my_sql_pass,
        database=my_sql_db)
    my_cursor = my_db.cursor()
    if not my_sql_struct:
        print("Default structure applied")
        print("structure: \n" + structure + "\n")
        my_cursor.execute(structure)
    else:
        print("structure specified applied")
        print("structure: \n" + my_sql_struct + "\n")
        my_cursor.execute(my_sql_struct)
    my_db.commit()
    my_cursor.close()
    my_db.close()
    print("Has no return")
    print(120 * "-")


def insert_register_my_sql(my_sql_host, my_sql_user, my_sql_pass, my_sql_db, my_sql_table,
                           columns_name_list, columns_value_list):
    """
Inserts a register to a table

Parameters
----------
my_sql_host : str
    MySQL's host.
my_sql_user : str
    User of host.
my_sql_pass : str
    User's password.
my_sql_db : str
    Database's name to update.
my_sql_table : str
    Table's name to update.
columns_name_list : list
    List of strings. Each element of the list contains the name of the columns to update.
    First element contains id of register to insert.
    columns_name_list = [id column's name, second column's name, third column's name, ...]
    Example:
    ``columns_name_list = ["id", "titulo", "ruta", "descripcion"]``
columns_value_list : list
    List of strings. Each element of the list contains the value of the columns to update.
    First element contains id of register to insert.
    columns_value_list = [id column's value, second column's value, third column's value, ...]
    Example:
    ``columns_value_list = ["12", "titulo a actualizar", "ruta a actualizar",`` \n
    ``"descripcion a actualizar"]``

Returns
-------
Aux : int
    it contains the number of registers inserted, this version only supports one
    register per method call.

    """
    print(46 * "-" + "insert_register_my_sql method" + 46 * "-")
    my_db = mysql.connector.connect(
        host=my_sql_host,
        user=my_sql_user,
        passwd=my_sql_pass,
        database=my_sql_db
    )
    my_cursor = my_db.cursor()
    if len(columns_name_list) == len(columns_value_list):
        sql = "INSERT INTO " + my_sql_table + " ("
        for i in range(0, len(columns_name_list)):
            sql += columns_name_list[i]
            if i < len(columns_name_list) - 1:
                sql += ", "
        sql += ") VALUES ("
        for i in range(0, len(columns_value_list)):
            sql += "%s"
            if i < len(columns_name_list) - 1:
                sql += ", "
        sql += ")"
        # Con .execute(ESTRUCTURA EN TIPO STRING, TUPLAS) puedo insertar tuplas en una tabla
        print(sql)
        print(columns_value_list)
        my_cursor.execute(sql, columns_value_list)
        my_db.commit()
        aux = my_cursor.rowcount
        my_cursor.close()
        my_db.close()
    else:
        aux = 0
    print("return: \n")
    print(aux)
    print(120 * "-")
    return aux


def delete_id_my_sql(my_sql_host, my_sql_user, my_sql_pass, my_sql_db, my_sql_table, my_sql_id):
    """
Deletes a register, it's selected by its id.

Parameters
----------
my_sql_host : str
    MySQL's host.
my_sql_user : str
    User of host.
my_sql_pass : str
    User's password.
my_sql_db : str
    Database to update.
my_sql_table : str
    Table's name to update.
my_sql_id : str
    id of register to delete.

Returns
-------
aux : int
    it contains the number of registers deleted, this version only supports one
    register per method call.

    """
    print(49 * "-" + "delete_id_my_sql method" + 49 * "-")
    my_db = mysql.connector.connect(
        host=my_sql_host,
        user=my_sql_user,
        passwd=my_sql_pass,
        database=my_sql_db
    )
    my_cursor = my_db.cursor()
    sql = "DELETE FROM " + my_sql_table + " WHERE id = " + my_sql_id
    print(sql)
    my_cursor.execute(sql)
    my_db.commit()
    aux = my_cursor.rowcount
    my_cursor.close()
    my_db.close()
    print("return: \n")
    print(aux)
    print(120 * "-")
    return aux


# Test search_like_my_sql
def search_like_my_sql(my_sql_host, my_sql_user, my_sql_pass, my_sql_db, my_sql_table, columns_name_list,
                       columns_name_search, str_to_search):
    """
Searchs the string "Search" in a "Column_Name_Search". search_like_my_sql match if a string of
the column "Column_Name_Search" contains the string "Search"

Parameters
----------
my_sql_host : str
    MySQL's host.
my_sql_user : str
    User of host.
my_sql_pass : str
    User's password.
my_sql_db : str
    Database where string "str_to_search" will be search.
my_sql_table : str
    Table where string "str_to_search" will be search.
columns_name_list : str
    List of strings. Each element of the list contains the name of the columns to request.
    First element contains id of register to insert.
    columns_name_list = [id column's name, second column's name, third column's name, ...]
    Example:
    ``columns_name_list = ["id", "titulo", "ruta", "descripción"]``
columns_name_search : str
    Column's name where to search the string "str_to_search"
str_to_search : str
    String to search the string


Returns
-------
resultados : list
    List of tuples.Each element contains a tuple with all columns's values request.


Examples
--------
>>> my_sql_host = "localhost"
>>> my_sql_user = "root"
>>> my_sql_pass = ""
>>> my_sql_db = "baseprueba2"
>>> my_sql_table = "producto"
>>> columns_name_list = ["id", "titulo", "ruta", "descripcion"]
>>> Column_Name_Search = "titulo"
>>> Search = "5"
>>> Aux = search_like_my_sql(my_sql_host, my_sql_user, my_sql_pass, my_sql_db, my_sql_table,
>>> columns_name_list, Column_Name_Search, Search)
>>> print("resultados encontrados : {0} coincidentes con '{1}'".format(len(Aux), Search))
>>> print("(Resultado {0}, Resultado {1}, Resultado {2}, Resultado {3})".format(
>>> columns_name_list[0], columns_name_list[1], columns_name_list[2], columns_name_list[3]))
>>> for x in Aux: print(x)
>>>     print(x)

>>> #+----+-----------+---------+--------------+
>>> #| id |  titulo   |  ruta   | descripcion  |--> Columns of table called "producto"
>>> #+----+-----------+---------+--------------+
>>> #| 4  | titulod5  | ruta24  | descripcion7 |--> Items matched/fetched
>>> #| 5  | 5         | 5       | 5            |
>>> #+----+-----------+---------+--------------+

Will print all coincidences with '5' in the column's name "titulo" witch belongs to a table
called "producto". This table belongs to a database called "baseprueba2"

It will print: \n
``[(4, 'titulod5', 'ruta24', 'descripcion7'), (5, '5', '5', '5')]``

    """
    print(48 * "-" + "search_like_my_sql method" + 48 * "-")
    my_db = mysql.connector.connect(
        host=my_sql_host,
        user=my_sql_user,
        passwd=my_sql_pass,
        database=my_sql_db)
    my_cursor = my_db.cursor()
    # Interpretación: Retornar la columna titulo de la tabla producto e id de la tabla
    # producto, donde la columna titulo de la tabla producto
    # %String% : "%String" indica cualquier carácter anterior a "String".
    # "String%" indica cualquier carácter posterior a "String". Es decir, debe
    # contener "String" sin importar si esta al inicio de la trama o al final.
    sql = "SELECT "
    for i in range(0, len(columns_name_list)):
        sql += my_sql_table + "." + columns_name_list[i]
        if i < len(columns_name_list) - 1:
            sql += ", "
    sql += " FROM " + my_sql_table + " WHERE " + my_sql_table + "." + columns_name_search + \
           " LIKE '%" + str_to_search + "%'"
    print(sql)
    my_cursor.execute(sql)
    resultados = my_cursor.fetchall()
    my_cursor.close()
    my_db.close()
    print("return: \n")
    print(resultados)
    print(120 * "-")
    return resultados


def query_my_sql(my_sql_host, my_sql_user, my_sql_pass, my_sql_query):
    """
Method to execute a query in the server my_sql_host.

Parameters
----------
my_sql_host : str
    MySQL's host.
my_sql_user : str
    User of host.
my_sql_pass : str
    User's password.
my_sql_query : str
    Query to execute


Returns
-------
Resultados : list
    List of tuples.Each element contains a tuple with all data fetched.

Example
-------
>>> my_sql_host = "localhost"
>>> my_sql_user = "root"
>>> my_sql_pass = ""
>>> my_sql_query = "SHOW DATABASES"
>>> aux = query_my_sql(my_sql_host, my_sql_user, my_sql_pass, my_sql_query)
>>> print(aux)
>>> +--------------------+
>>> |     Database       |
>>> +--------------------+
>>> | baseprueba1        |
>>> | baseprueba2        |
>>> | baseprueba3        |
>>> | information_schema |
>>> | mysql              |
>>> | performance_schema |
>>> | phpmyadmin         |
>>> | test               |
>>> +--------------------+

It will print: \n
``[('baseprueba1',), ('baseprueba2',), ('baseprueba3',), ('information_schema',), \`` \n
``'mysql',), ('performance_schema',), ('phpmyadmin',), ('test',)]``

Example
-------
>>> def test_query2():
>>>         my_sql_host = "localhost"
>>>         my_sql_user = "root"
>>>         my_sql_pass = ""
>>>         my_sql_query = "SHOW TABLES FROM baseprueba2"
>>>         aux = []
>>>         aux = query_my_sql(my_sql_host, my_sql_user, my_sql_pass, my_sql_query)
>>>         print(aux)
>>>
>>>
>>> test_query2()
>>> #+------------------------+
>>> #| Tables_in_baseprueba2  |
>>> #+------------------------+
>>> #| producto               |
>>> #| productoww             |
>>> #+------------------------+

It will print: \n
``[('producto',), ('productoww',)]``

Example
-------
>>> def test_query4():
>>>         my_sql_host = "localhost"
>>>         my_sql_user = "root"
>>>         my_sql_pass = ""
>>>         my_sql_query = "SHOW FULL COLUMNS FROM baseprueba1.producto"
>>>         aux = []
>>>         aux = query_my_sql(my_sql_host, my_sql_user, my_sql_pass, my_sql_query)
>>>         print(aux)
>>>
>>>
>>> test_query4()
>>> #+-------------+--------------+------------------+------+-----+---------+----------------+---------------------------------+---------+
>>> #|    Field    |     Type     |    Collation     | Null | Key | Default |     Extra      |           Privileges            | Comment |
>>> #+-------------+--------------+------------------+------+-----+---------+----------------+---------------------------------+---------+
>>> #| id          | int(11)      | NULL             | NO   | PRI | NULL    | auto_increment | select,insert,update,references |         |
>>> #| titulo      | varchar(128) | utf8_spanish2_ci | NO   |     | NULL    |                | select,insert,update,references |         |
>>> #| ruta        | varchar(128) | utf8_spanish2_ci | NO   |     | NULL    |                | select,insert,update,references |         |
>>> #| descripcion | text         | utf8_spanish2_ci | NO   |     | NULL    |                | select,insert,update,references |         |
>>> #+-------------+--------------+------------------+------+-----+---------+----------------+---------------------------------+---------+

It will print: \n
``[('id', 'int(11)', None, 'NO', 'PRI', None, 'auto_increment', \`` \n
``'select,insert,update,references', ''), ('titulo', 'varchar(128)', \`` \n
``'utf8_spanish2_ci', 'NO', '', None, '', 'select,insert,update,references', ''), \`` \n
``('ruta', 'varchar(128)', 'utf8_spanish2_ci', 'NO', '', None, '', \`` \n
``'select,insert,update,references', ''), ('descripcion', 'text', 'utf8_spanish2_ci', \`` \n
``'NO', '', None, '', 'select,insert,update,references', '')]``

    """
    print(51 * "-" + "query_my_sql method" + 51 * "-")
    my_db = mysql.connector.connect(
        host=my_sql_host,
        user=my_sql_user,
        passwd=my_sql_pass)
    # Interpretación: Retornar la columna titulo de la tabla producto e id de la tabla
    # producto, donde la columna titulo de la tabla producto
    # %String% : "%String" indica cualquier carácter anterior a "String".
    # "String%" indica cualquier carácter posterior a "String". Es decir, debe
    # contener "String" sin importar si esta al inicio de la trama o al final.
    my_cursor = my_db.cursor()
    sql = my_sql_query
    print(sql)
    my_cursor.execute(sql)
    aux = my_cursor.fetchall()
    my_cursor.close()
    my_db.close()
    print("return: \n")
    print(aux)
    print(120 * "-")
    return aux


def show_databases_my_sql(my_sql_host, my_sql_user, my_sql_pass):
    """
Method to show all databases in the server my_sql_host.

Parameters
----------
my_sql_host : str
    MySQL's host.
my_sql_user : str
    User of host.
my_sql_pass : str
    User's password.

Returns
-------
Resultados : list
    List of tuples.Each element contains a tuple with all databases fetched.

Example
-------
>>> my_sql_host = "localhost"
>>> my_sql_user = "root"
>>> my_sql_pass = ""
>>> aux = show_databases_my_sql(my_sql_host, my_sql_user, my_sql_pass)
>>> print(aux)
>>> #+--------------------+
>>> #|     Database       |
>>> #+--------------------+
>>> #| baseprueba1        |
>>> #| baseprueba2        |
>>> #| baseprueba3        |
>>> #| information_schema |
>>> #| mysql              |
>>> #| performance_schema |
>>> #| phpmyadmin         |
>>> #| test               |
>>> #+--------------------+

It will print: \n
``[('baseprueba1',), ('baseprueba2',), ('baseprueba3',), ('information_schema',), \`` \n
``'mysql',), ('performance_schema',), ('phpmyadmin',), ('test',)]``


    """
    print(46 * "-" + "show_databases_my_sql method" + 46 * "-")
    my_db = mysql.connector.connect(
        host=my_sql_host,
        user=my_sql_user,
        passwd=my_sql_pass)
    # Interpretación: Retornar la columna titulo de la tabla producto e id de la tabla
    # producto, donde la columna titulo de la tabla producto
    # %String% : "%String" indica cualquier carácter anterior a "String".
    # "String%" indica cualquier carácter posterior a "String". Es decir, debe
    # contener "String" sin importar si esta al inicio de la trama o al final.
    my_cursor = my_db.cursor()
    sql = "SHOW DATABASES"
    print(sql)
    my_cursor.execute(sql)
    aux = my_cursor.fetchall()
    my_cursor.close()
    my_db.close()
    print("return: \n")
    print(aux)
    print(120 * "-")
    return aux

def show_tables_my_sql(my_sql_host, my_sql_user, my_sql_pass, my_sql_db):
    """
Method to show all table in the database my_sql_db.

Parameters
----------
my_sql_host : str
    MySQL's host.
my_sql_user : str
    User of host.
my_sql_pass : str
    User's password.
my_sql_db : str
    User's password.

Returns
-------
Resultados : list
    List of tuples.Each element contains a tuple with all databases fetched.

Example
-------
>>> def test_show_table():
>>>         my_sql_host = "localhost"
>>>         my_sql_user = "root"
>>>         my_sql_pass = ""
>>>         my_sql_db = "baseprueba2"
>>>         aux = []
>>>         aux = show_tables_my_sql(my_sql_host, my_sql_user, my_sql_pass, my_sql_db)
>>>         print(aux)
>>>
>>>
>>> test_show_table()
>>> #+------------------------+
>>> #| Tables_in_baseprueba2  |
>>> #+------------------------+
>>> #| producto               |
>>> #| productoww             |
>>> #+------------------------+

It will print: \n
``[('producto',), ('productoww',)]``

    """
    print(48 * "-" + "show_tables_my_sql method" + 48 * "-")
    my_db = mysql.connector.connect(
        host=my_sql_host,
        user=my_sql_user,
        passwd=my_sql_pass)
    # Interpretación: Retornar la columna titulo de la tabla producto e id de la tabla
    # producto, donde la columna titulo de la tabla producto
    # %String% : "%String" indica cualquier carácter anterior a "String".
    # "String%" indica cualquier carácter posterior a "String". Es decir, debe
    # contener "String" sin importar si esta al inicio de la trama o al final.
    my_cursor = my_db.cursor()
    sql = "SHOW TABLES FROM " + my_sql_db
    print(sql)
    my_cursor.execute(sql)
    aux = my_cursor.fetchall()
    print(aux)
    if not aux:
        print("Sin tablas")
    my_cursor.close()
    my_db.close()
    print("return: \n")
    print(aux)
    print(120 * "-")
    return aux


class MySQL:
    def __init__(self, my_sql_host, my_sql_user, my_sql_pass,
                 my_sql_db, my_sql_table, my_sql_struct):
        self.my_sql_host = my_sql_host
        self.my_sql_user = my_sql_user
        self.my_sql_pass = my_sql_pass
        self.my_sql_db = my_sql_db
        self.my_sql_table = my_sql_table
        self.my_sql_struct = my_sql_struct

    def create_db(self):
        try:
            create_db_my_sql(self.my_sql_host, self.my_sql_user, self.my_sql_pass, self.my_sql_db)
            print("Database has been created or has already exists")
            return 0
        except:
            print("Database has not been created")
            return -1

    def create_table(self):
            try:
                create_table_my_sql(self.my_sql_host, self.my_sql_user, self.my_sql_pass, self.my_sql_db,
                                   self.my_sql_table, self.my_sql_struct)
                print("Table has been created or has already exists")
                return 0
            except:
                print("Table has not been created")
                return -1

    def add_register(self, columns_name_list, columns_value_list):
        try:
            aux = insert_register_my_sql(self.my_sql_host, self.my_sql_user, self.my_sql_pass, self.my_sql_db,
                                         self.my_sql_table, columns_name_list, columns_value_list)
            print(str(aux) + " register has been added")
            return aux
        except:
            print("Register could not been added")
            return -1

    def update_register(self, columns_name_list, columns_value_list):
        try:
            aux = str(update_where_id_my_sql(self.my_sql_host, self.my_sql_user, self.my_sql_pass, self.my_sql_db,
            self.my_sql_table, columns_name_list, columns_value_list))
            if aux == '-1':
                print("columns_name_list's lenght does not match with columns_value_list's lenght")
            elif aux == '0':
                print("New register is identical to older")
            else:
                print(aux, "register updated")
        except:
            print("Database has not been updated")
        return int(aux)

    def delete_register(self, my_sql_id):
        aux = -1
        try:
            aux = str(delete_id_my_sql(self.my_sql_host, self.my_sql_user, self.my_sql_pass, self.my_sql_db,
                                       self.my_sql_table, my_sql_id))
            if aux == '0':
                print("Register to delete does not exist")
            else:
                print(aux + " register has been deleted")
        except:
            print("Error while trying to delete register")
        return aux

    def show_databases(self):
        aux = show_databases_my_sql(self.my_sql_host, self.my_sql_user, self.my_sql_pass)
        print(aux)
        return aux

    def show_tables(self, my_sql_db):
        aux = show_tables_my_sql(self.my_sql_host, self.my_sql_user, self.my_sql_pass, my_sql_db)
        print(aux)
        return aux

    def search_str(self, columns_name_list, column_name_search, str_to_search):
        aux = search_like_my_sql(self.my_sql_host, self.my_sql_user, self.my_sql_pass, self.my_sql_db,
                                 self.my_sql_table, columns_name_list, column_name_search, str_to_search)
        print("Resultados encontrados : {0} coindidentes con '{1}'".format(len(aux), str_to_search))
        print("(Resultado {0}, Resultado {1}, Resultado {2}, Resultado {3})".format(
            columns_name_list[0], columns_name_list[1], columns_name_list[2], columns_name_list[3]))
        print(aux)
        for x in aux:
            print(x)
        return aux

    def query(self, my_sql_query):
        try:
            aux = query_my_sql(self.my_sql_host, self.my_sql_user, self.my_sql_pass, my_sql_query)
        except:
            aux = -1
        print(aux)
        return aux

    def get_my_sql_host(self):
        return self.my_sql_host

    def get_my_sql_user(self):
        return self.my_sql_user

    def get_my_sql_pass(self):
        return self.my_sql_pass

    def get_my_sql_db(self):
        return self.my_sql_db

    def get_my_sql_table(self):
        return self.my_sql_table

    def get_my_sql_struct(self):
        return self.my_sql_struct


def create_table_orm(my_sql_db, my_sql_host, my_sql_port, my_sql_user, my_sql_pass, columns_name_list):
    aux = -1
    try:
        db = MySQLDatabase(my_sql_db, host=my_sql_host, port=my_sql_port,
                           user=my_sql_user,
                           passwd=my_sql_pass)

        class Catalogue(Model):
            class Meta:
                database = db

        class RegItem(Catalogue):
            # id column is not required due to peewee auto generates it and assign a AutoField class to it.
            # classAutoField:
            # Field class for storing auto-incrementing primary keys.
            locals()[columns_name_list[0]] = TextField()
            locals()[columns_name_list[1]]  = TextField()

        db.connect()
        db.create_tables([RegItem])
        db.close()
        aux = 1
        print("create_table_orm: Table has been created")
    except:
        print("create_table_orm: Error")
    return aux

def add_reg_orm(my_sql_db, my_sql_host, my_sql_port, my_sql_user, my_sql_pass, columns_name_list,**dictItem):
    aux = -1
    try:
        db = MySQLDatabase(my_sql_db, host=my_sql_host, port=my_sql_port,
                           user=my_sql_user,
                           passwd=my_sql_pass)

        class Catalogue(Model):
            class Meta:
                database = db

        class RegItem(Catalogue):
            # id column is not required due to peewee auto generates it and assign a AutoField class to it.
            # classAutoField:
            # Field class for storing auto-incrementing primary keys.
            locals()[columns_name_list[0]] = TextField()
            locals()[columns_name_list[1]]  = TextField()

        db.connect()
        print(dictItem)
        aux = RegItem(**dictItem)
        aux.save()
        db.close()
        aux = 1
        print("add_reg_orm: Register has been added")
    except:
        print("add_reg_orm: Error")
    return aux



def show_reg_orm(my_sql_db, my_sql_host, my_sql_port, my_sql_user, my_sql_pass, columns_name_list):
    aux = -1
    try:
        db = MySQLDatabase(my_sql_db, host=my_sql_host, port=my_sql_port,
                           user=my_sql_user,
                           passwd=my_sql_pass)

        class Catalogue(Model):
            class Meta:
                database = db

        class RegItem(Catalogue):
            # id column is not required due to peewee auto generates it and assign a AutoField class to it.
            # classAutoField:
            # Field class for storing auto-incrementing primary keys.
            locals()[columns_name_list[0]] = TextField()
            locals()[columns_name_list[1]]  = TextField()

        db.connect()
        fetched = []
        query = RegItem.select(RegItem.id, RegItem.titulo, RegItem.descripcion)
        for item in query:
            fetched.append((item.id, item.titulo, item.descripcion))
            print(item.id)
            print(item.titulo)
            print(item.descripcion)
        print(fetched)
        db.close()
        print("show_reg_orm: Data fetched returned")
        return fetched
    except:
        print("show_reg_orm: Error")
        return aux



