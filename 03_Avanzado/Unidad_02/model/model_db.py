import mysql.connector
from peewee import *

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


def delete_reg_orm(my_sql_db, my_sql_host, my_sql_port, my_sql_user, my_sql_pass, columns_name_list, id_reg):
    aux = -1
    print(id_reg)
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
        deleteReg = RegItem.get(RegItem.id == int(id_reg) )
        deleteReg.delete_instance()
        db.close()
        aux = 1
        print("delete_reg_orm: Register deleted")
    except:
        print("delete_reg_orm: Error")
    return aux



def update_register_orm(my_sql_db, my_sql_host, my_sql_port, my_sql_user, my_sql_pass, columns_name_list, reg_item):
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
        updateReg = RegItem.get(RegItem.id == int(reg_item[0]) )
        updateReg.titulo = reg_item[1]
        updateReg.descripcion = reg_item[2]
        updateReg.save()
        db.close()
        aux = 1
        print("update_register_orm: Register updated")
    except:
        print("update_register_orm: Error")
    return aux


