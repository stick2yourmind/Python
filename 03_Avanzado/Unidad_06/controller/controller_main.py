import sys
sys.path.append("..")
import re
from model.model_db import create_db_my_sql, create_table_orm, show_reg_orm, add_reg_orm, delete_reg_orm, update_register_orm
from model.model_shelve import *

Pattern = "^[A-Za-z]+(?:[ _-][A-Za-z]+)*$"
columns_name_list = ["titulo", "fecha", "descripcion", "estado", "objeto"]
title = 0
description = 1


def validate(pattern, to_validate):
    r_aux = re.compile(pattern)
    return r_aux.search(to_validate)

def create_db():
    print("\tcreate_db: starting")
    aux = create_db_my_sql()
    print("\tcreate_db: finished")
    return aux

def create_table():
    print("\tcreate_table: starting")
    aux = create_table_orm()
    print("\tcreate_table: finished")
    return aux

def controller_add_reg(input_title, input_description):
    print("\tcontroller_add_reg: starting")
    aux = -1
    columns_value_list = [input_title, input_description]
    # Clean entry title and entry description
    if validate(Pattern, columns_value_list[title]):
        try:
            aux = add_reg_orm(columns_value_list[0], columns_value_list[1])
            print("\tcontroller_add_reg: Model method has been executed")
        except:
            print("\tcontroller_add_reg: Model method could not been executed")
    print("\tcontroller_add_reg: finished")
    return aux

def controller_update_reg(id_reg, input_title, input_description):
    print("\tcontroller_update_reg: starting")
    aux = -1
    reg_item = [id_reg, input_title, input_description]
    try:
        aux = update_register_orm(reg_item)
        print("\tcontroller_update_reg: Model method has been executed")
    except:
        print("\tcontroller_update_reg: Model method could not been executed")
    print("\tcontroller_update_reg: finished")
    return aux

def controller_delete_reg(id_reg):
    print("\tcontroller_delete_reg: starting")
    aux = -1
    try:
        aux = delete_reg_orm(id_reg)
        print("\tcontroller_delete_reg: Model method has been executed")
    except:
        print("\tcontroller_delete_reg: Model method could not been executed")
    print("\tcontroller_delete_reg: finished")
    return aux

def controller_create_d_b():
    print("\tcontroller_create_d_b: starting")
    error = -1
    aux = create_db()
    if aux == error:
        print("\tcontroller_create_d_b: finished")
        return aux
    else:
        aux = create_table()
    print("\tcontroller_create_d_b: finished")
    return aux

def controller_show_reg():
    print("\tcontroller_show_reg: starting")
    fetched = -1
    try:
        fetched = show_reg_orm()
        print("\tcontroller_show_reg:  Model method has been executed")
    except:
        print("\tcontroller_show_reg: Model method could not been executed")
    print("\tcontroller_show_reg: finished")
    return fetched

def controller_theme(theme_name, color="default", act="choose"):
    print("\tcontroller_theme: starting")
    if act=="choose":
        print("\tcontroller_theme: finished")
        return choose_theme(theme_name)
    else:
        save_theme(theme_name, color)
        print("\tcontroller_theme: finished")

