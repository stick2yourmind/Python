import random
from peewee import *
import datetime
import mysql.connector


my_sql_host_default = "localhost"
my_sql_user_default = "root"
my_sql_pass_default = ""
my_sql_db_default = "catalogueDB"
my_sql_table_default = "producto"
columns_name_list = ["titulo", "fecha", "descripcion", "estado", "objeto"]
my_sql_db = my_sql_db_default
my_sql_port = 3306
my_sql_host = my_sql_host_default
my_sql_user = my_sql_user_default
my_sql_pass = my_sql_pass_default



def create_db_my_sql(my_sql_host, my_sql_user, my_sql_pass, my_sql_db):
    aux = -1
    try:
        my_db = mysql.connector.connect(
            host=my_sql_host,
            user=my_sql_user,
            passwd=my_sql_pass)
        my_cursor = my_db.cursor()
        my_cursor.execute("CREATE DATABASE IF NOT EXISTS " + my_sql_db)
        my_db.commit()
        my_cursor.close()
        my_db.close()
        aux = 1
        print("create_db_my_sql: DB has been created")
    except:
        print("create_db_my_sql: Error")
    return aux



def create_table_orm(my_sql_db, my_sql_host, my_sql_port, my_sql_user, my_sql_pass, columns_name_list):
    aux = -1
    try:
        db = MySQLDatabase(my_sql_db, host=my_sql_host, port=my_sql_port,
                           user=my_sql_user,
                           passwd=my_sql_pass)

        class Catalogue(Model):
            class Meta:
                database = db

        class RegItem3(Catalogue):
            # id column is not required due to peewee auto generates it and assign a AutoField class to it.
            # classAutoField:
            # Field class for storing auto-incrementing primary keys.
            locals()[columns_name_list[0]] = TextField()
            locals()[columns_name_list[1]]  = DateTimeField(default=datetime.datetime.now())
            locals()[columns_name_list[2]]  = TextField()
            locals()[columns_name_list[3]]  = BooleanField(default=True)
            locals()[columns_name_list[4]]  = TextField()

        db.connect()
        db.create_tables([RegItem3])
        db.close()
        aux = 1
        print("create_table_orm: Table has been created")
    except:
        print("create_table_orm: Error")
    return aux


create_db_my_sql(my_sql_host, my_sql_user, my_sql_pass, my_sql_db)
create_table_orm(my_sql_db, my_sql_host, my_sql_port, my_sql_user, my_sql_pass , columns_name_list)
db = MySQLDatabase(my_sql_db, host=my_sql_host, port=my_sql_port,
                   user=my_sql_user,
                   passwd=my_sql_pass)

class Catalogue(Model):
    class Meta:
        database = db

class RegItem3(Catalogue):
    # id column is not required due to peewee auto generates it and assign a AutoField class to it.
    # classAutoField:
    # Field class for storing auto-incrementing primary keys.
    locals()[columns_name_list[0]] = TextField()
    locals()[columns_name_list[1]]  = DateTimeField(default=datetime.datetime.now())
    locals()[columns_name_list[2]]  = TextField()
    locals()[columns_name_list[3]]  = BooleanField(default=True)
    locals()[columns_name_list[4]]  = TextField()


db.connect()
columns_value_list = ["5", "titulo", None, "descripcion", "estado", "objeto"]
RegItem3 = RegItem3()
RegItem3.titulo = columns_value_list[1]
RegItem3.fecha = datetime.datetime.now()
RegItem3.descripcion = columns_value_list[3]
RegItem3.estado = columns_value_list[4]
RegItem3.objeto = columns_value_list[5]
RegItem3.save()
db.close()
# There is another way to update registers, by using both update() and execute(). Check pdf at unit 1 to check how to
# implement that solution.