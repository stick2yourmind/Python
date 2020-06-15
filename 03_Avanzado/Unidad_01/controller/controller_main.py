import sys
sys.path.append("..")
import re
import sys
sys.path.append('..')
from model.model_db import *
from model.model_shelve import *

Pattern = "^[A-Za-z]+(?:[ _-][A-Za-z]+)*$"

my_sql_host_default = "localhost"
my_sql_user_default = "root"
my_sql_pass_default = ""
my_sql_db_default = "baseprueba4"
my_sql_table_default = "producto"
my_sql_struct_default = "CREATE TABLE IF NOT EXISTS producto( id int(11) NOT NULL PRIMARY KEY \
AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, descripcion text COLLATE \
utf8_spanish2_ci NOT NULL )"
columns_name_list = ["titulo", "descripcion"]
title = 0
description = 1

reg = MySQL(my_sql_host=my_sql_host_default, my_sql_user=my_sql_user_default, my_sql_pass=my_sql_pass_default,
                 my_sql_db=my_sql_db_default, my_sql_table=my_sql_table_default, my_sql_struct=my_sql_struct_default)

def validate(pattern, to_validate):
    r_aux = re.compile(pattern)
    return r_aux.search(to_validate)

def create_db():
    global reg
    aux = reg.create_db()
    return aux

def create_table():
    global columns_name_list
    my_sql_db = my_sql_db_default
    my_sql_port = 3306
    my_sql_host = my_sql_host_default
    my_sql_user = my_sql_user_default
    my_sql_pass = my_sql_pass_default
    aux = create_table_orm(my_sql_db, my_sql_host, my_sql_port, my_sql_user, my_sql_pass, columns_name_list)
    return aux

def controller_add_reg(input_title, input_description):
    global columns_name_list
    aux = -1
    my_sql_db = my_sql_db_default
    my_sql_port = 3306
    my_sql_host = my_sql_host_default
    my_sql_user = my_sql_user_default
    my_sql_pass = my_sql_pass_default
    columns_value_list = [input_title, input_description]
    # Clean entry title and entry description
    if validate(Pattern, columns_value_list[title]):
        try:
            dictItem = {}
            dictItem[str(columns_name_list[0])] = str(columns_value_list[0])
            dictItem[str(columns_name_list[1])] = str(columns_value_list[1])
            aux = add_reg_orm(my_sql_db, my_sql_host, my_sql_port, my_sql_user, my_sql_pass, columns_name_list,
                                  **dictItem)
            print("controller_add_reg: register added")
        except:
            print("controller_add_reg: error")
    return aux

def controller_update_reg(id_reg, input_title, input_description):
    a = ["id", "titulo", "descripcion"]
    b = [id_reg, input_title, input_description]
    aux = reg.update_register(a,b)
    return aux

def controller_delete_reg(id_reg):
    aux = reg.delete_register(id_reg)
    return aux

def controller_create_d_b():
    error = -1
    aux = create_db()
    if aux == error:
        return aux
    else:
        aux = create_table()
    return aux


def controller_show_reg():
    global columns_name_list
    fetched = -1
    my_sql_db = my_sql_db_default
    my_sql_port = 3306
    my_sql_host = my_sql_host_default
    my_sql_user = my_sql_user_default
    my_sql_pass = my_sql_pass_default
    try:
        fetched = show_reg_orm(my_sql_db, my_sql_host, my_sql_port, my_sql_user, my_sql_pass, columns_name_list)
        print("controller_show_reg: Executed succesfully")
    except:
        print("controller_show_reg: Error")
    return fetched

def controller_theme(theme_name, color="default", act="choose"):
    if act=="choose":
        return choose_theme(theme_name)
    else:
        save_theme(theme_name, color)

