from peewee import *

aux = -1
my_sql_host_default = "localhost"
my_sql_user_default = "root"
my_sql_pass_default = ""
my_sql_db_default = "baseprueba4"
my_sql_table_default = "producto"
columns_name_list = ["titulo", "descripcion"]
my_sql_db = my_sql_db_default
my_sql_port = 3306
my_sql_host = my_sql_host_default
my_sql_user = my_sql_user_default
my_sql_pass = my_sql_pass_default
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
    locals()[columns_name_list[1]] = TextField()


db.connect()

query = RegItem.select(RegItem.id, RegItem.titulo, RegItem.descripcion)
print(query)
for aux in query:
    print(aux.id)
    print(aux.titulo)
    print(aux.descripcion)

db.close()
aux = 1