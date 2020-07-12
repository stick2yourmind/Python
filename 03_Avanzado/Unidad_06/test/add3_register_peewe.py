import mysql.connector
from peewee import *
import datetime

my_sql_host_default = "localhost"
my_sql_port_default = 3306
my_sql_user_default = "root"
my_sql_pass_default = ""
my_sql_db_default = "catalogueDB"
my_sql_table_default = "producto"
my_sql_struct_default = "CREATE TABLE IF NOT EXISTS producto( id int(11) NOT NULL PRIMARY KEY \
AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, fecha text COLLATE utf8_spanish2_ci " \
                        "NOT NULL, descripcion text COLLATE utf8_spanish2_ci NOT NULL,  estado text COLLATE " \
                        "utf8_spanish2_ci NOT NULL,  objeto text COLLATE utf8_spanish2_ci NOT NULL, )"
my_sql_host = my_sql_host_default
my_sql_port = my_sql_port_default
my_sql_user = my_sql_user_default
my_sql_pass = my_sql_pass_default
my_sql_db = my_sql_db_default
my_sql_table = my_sql_table_default





def add_reg_orm(titulo , descripcion , estado , objeto):
    print("\t\tadd_reg_orm: starting")
    aux = -1
    try:
        db = MySQLDatabase(my_sql_db, host=my_sql_host, port=my_sql_port,
                           user=my_sql_user,
                           passwd=my_sql_pass)

        class Catalogue(Model):
            class Meta:
                database = db

        class RegItem(Catalogue):
            titulo = TextField()
            fecha = DateTimeField(default=datetime.datetime.now())
            descripcion = TextField()
            estado = TextField()
            objeto = TextField()
            class Meta:
                database = db
            def __str__(self):
                return "El título es: " + self.titulo

        db.connect()
        obj = RegItem(titulo = titulo, descripcion = descripcion, estado = estado)
        print(obj)
        obj = RegItem(titulo = titulo, descripcion = descripcion, estado = estado, objeto = str(obj))
        obj.save()
        db.close()
        aux = 1
        print("\t\tadd_reg_orm: Register has been added")
    except:
        print("\t\tadd_reg_orm: Error")
    print("\t\tadd_reg_orm: finished")
    return aux

def create_table_orm():
    print("\t\tcreate_table_orm: starting")
    aux = -1
    try:
        # db.connect()
        db.create_tables([RegItem])
        # db.close()
        aux = 1
        print("\t\tcreate_table_orm: Table has been created")
    except:
        print("\t\tcreate_table_orm: Error")
    print("\t\tcreate_table_orm: finished")
    return aux

create_table_orm()
add_reg_orm(titulo="ddsddd", descripcion="ooo", estado = "estado1", objeto = "ooo")