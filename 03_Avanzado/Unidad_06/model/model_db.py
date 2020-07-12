import mysql.connector
from peewee import *
import datetime

# global variables connection to db
my_sql_db = "catalogueDB"
my_sql_host = "localhost"
my_sql_port = 3306
my_sql_user = "root"
my_sql_pass = ""
my_sql_table = "RegItem"
my_sql_struct = "CREATE TABLE IF NOT EXISTS producto( id int(11) NOT NULL PRIMARY KEY \
AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, descripcion text COLLATE \
utf8_spanish2_ci NOT NULL )"

# Creating a db connection
db = MySQLDatabase(my_sql_db, host=my_sql_host, port=my_sql_port,
                   user=my_sql_user,
                   passwd=my_sql_pass)


# Access to db


class Catalogue(Model):
    class Meta:
        database = db


# Access to table


class RegItem(Catalogue):
    titulo = TextField()
    fecha = DateTimeField(default=datetime.datetime.now())
    descripcion = TextField()
    estado = BooleanField(default=True)
    objeto = TextField()

    def __str__(self):
        return "El título es: " + self.titulo


def create_db_my_sql():
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
    print("\t\tcreate_db_my_sql: starting")
    global my_sql_db
    global my_sql_host
    global my_sql_user
    global my_sql_pass
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
        print("\t\tcreate_db_my_sql: DB has been created")
    except:
        print("\t\tcreate_db_my_sql: Error")
    print("\t\tcreate_db_my_sql: finished")
    return aux


def create_table_orm():
    print("\t\tcreate_table_orm: starting")
    global db
    global RegItem
    aux = -1
    try:
        db.connect()
        db.create_tables([RegItem])
        db.close()
        aux = 1
        print("\t\tcreate_table_orm: Table has been created")
    except:
        print("\t\tcreate_table_orm: Error")
    print("\t\tcreate_table_orm: finished")
    return aux


def print_add(fn):
    def console_printer(*args):
        print("\t\t\tprint_add: título = ", args[0])    # args[0] primer parámetro de add_reg_orm
        print("\t\t\tprint_add: descripción = ", args[1]) # args[1] segundo parámetro de add_reg_orm
        aux = fn(*args) # fn(*args) add_reg_orm's return
        if aux != -1:
            print("\t\t\tprint_add: One register has been added by using decorator")
        else:
            print("\t\t\tprint_add: Register could not been added by using decorator")
        return aux
    return console_printer


@print_add
def add_reg_orm(titulo, descripcion):
    print("\t\tadd_reg_orm: starting")
    global db
    global RegItem
    aux = -1
    try:
        db.connect()
        obj = RegItem(titulo=titulo, descripcion=descripcion)
        print("\t\t", obj)
        obj = RegItem(titulo=titulo, descripcion=descripcion, objeto=str(obj))
        obj.save()
        db.close()
        aux = 1
        print("\t\tadd_reg_orm: Register has been added")
    except:
        print("\t\tadd_reg_orm: Error")
    print("\t\tadd_reg_orm: finished")
    return aux


def show_reg_orm():
    print("\t\tshow_reg_orm: starting")
    global db
    global RegItem
    aux = -1
    try:
        db.connect()
        fetched = []
        query = RegItem.select(RegItem.id, RegItem.titulo, RegItem.fecha, RegItem.descripcion, RegItem.estado,
                               RegItem.objeto)
        for item in query:
            fetched.append((item.id, item.titulo, item.fecha,
                            item.descripcion, item.estado, item.objeto))
        db.close()
        print("\t\tshow_reg_orm: Data fetched returned")
        aux = 1
    except:
        print("\t\tshow_reg_orm: Error")
    print("\t\tshow_reg_orm: finished")
    if aux == -1:
        return aux
    else:
        return fetched

def print_delete(fn):
    def console_printer(*args):
        print("\t\t\tprint_delete: id = ", args[0])    # args[0] primer parámetro de delete_reg_orm
        aux = fn(*args)
        if aux != -1:
            print("\t\t\tprint_delete: One register has been deleted by using decorator")
        else:
            print("\t\t\tprint_delete: Register could not been deleted by using decorator")
        return aux
    return console_printer


@print_delete
def delete_reg_orm(id_reg):
    print("\t\tdelete_reg_orm: starting")
    global db
    global RegItem
    aux = -1
    try:
        db.connect()
        deleteReg = RegItem.get(RegItem.id == int(id_reg))
        deleteReg.delete_instance()
        db.close()
        aux = 1
        print("\t\tdelete_reg_orm: Register deleted")
    except:
        print("\t\tdelete_reg_orm: Error")
    print("\t\tdelete_reg_orm: finished")
    return aux

def print_update(fn):
    def console_printer(*args):
        print("\t\t\tprint_update: id = ", args[0][0])  # args[0][0] primer elemento del parámetro de update_register_orm
        print("\t\t\tprint_update: título = ", args[0][1])  # args[0][1] segundo elemento del primer parámetro de update_register_orm
        print("\t\t\tprint_update: descripción = ", args[0][2])  # args[0][2] tercer elemento del primer parámetro de update_register_orm
        aux = fn(*args)
        if aux != -1:
            print("\t\t\tprint_update: One register has been updated by using decorator")
        else:
            print("\t\t\tprint_update: Register could not been updated by using decorator")
        return aux
    return console_printer


@print_update
def update_register_orm(reg_item):
    print("\t\tupdate_register_orm: starting")
    global db
    global RegItem
    aux = -1
    try:
        db.connect()
        updateReg = RegItem(titulo=reg_item[1], descripcion=reg_item[2])
        updateReg = RegItem.update(titulo=reg_item[1], descripcion=reg_item[2], objeto=str(updateReg)).where(
            RegItem.id == reg_item[0])
        updateReg.execute()
        db.close()
        aux = 1
        print("\t\tupdate_register_orm: Register updated")
    except:
        print("\t\tupdate_register_orm: Error")
    print("\t\tupdate_register_orm: finished")
    return aux
