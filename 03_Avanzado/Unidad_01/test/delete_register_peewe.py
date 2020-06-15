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
id_reg = "10"
deleteReg = RegItem.get(RegItem.id == int(id_reg) )
deleteReg.delete_instance()
db.close()
# Error when RegItem.id does not exist or has been already deleted, example with id_reg=10:
# __main__.RegItemDoesNotExist: <Model: RegItem> instance matching query does not exist:
# SQL: SELECT `t1`.`id`, `t1`.`titulo`, `t1`.`descripcion` FROM `regitem` AS `t1` WHERE (`t1`.`id` = %s) LIMIT %s OFFSET %s
# Params: [10, 1, 0]