# Python

Python proyects and snippets

Unit - 01:

    	Rev. 0.0:

    		Proyect to apply ORM module.

    	Rev. 1.0:
    	        ORM choose: peewee
    		Database: MySQL
           		Connector used to create db: pymysql, mysql-connector crash wit peewee.
    		Create table and add register has been implemented.
    		Know issues: query does not work but query example at test folder works. Next revision will implement queries
    	Rev. 1.1:
    		Added show_reg_orm model method, implemented as a query
    	Rev. 1.2:
    		Added delete_reg_orm model method
    	Rev. 1.3:
    		Added update_register_orm model method to complete CRUD application.

Unit - 02:

    	REV. 1.0:
    			View updated. Layout has been modified to have six columns at treeview.
    	REV. 2.0:
                Overloading __str__ in regItem class implemented. View, controller and model updated.

Unit - 03:

    	REV. 1.0:
    			Script to modify
    	REV. 2.0:
                Script modified
                
                
Unit - 04:

    	REV. 2.0:
                Añadidos decoradores print_add, print_delete y print_delete. En caso de resultar el proceso correctamente ejecutado se imprime en consola:
                    "print_add: One register has been added by using decorator", 
                    "print_delete: One register has been deleted by using decorator" y 
                    "print_update: One register has been updated by using decorator". 
                En caso erróneo se imprime en consola: 
                    "print_add: Register could not been added by using decorator", 
                    "print_delete: Register could not been deleted by using decorator" y 
                    "print_update: Register could not been updated by using decorator".

    	REV. 2.1:
    	        Añadido información adicional del registro impreso en cada decorador.
    	            print_add: informa título y descripción, únicos parametro recibidos por add_reg_orm.
    	            print_delete: informa id, único parametro recibido por delete_reg_orm.
    	            print_update: informa id, título y descripción. Únicos parametro recibido por update_register_orm.

Unit - 05: Ninguna

Unit - 06:

    	REV. 2.0:
                Añadido patron observador en la capa view. Modificación minima del código.
    	REV. 2.1:
                Corrección de columnas invertidas entre fecha y descripción.
    	REV. 2.2:
                Se mueven los módulos del patron observador a la carpeta observerpattern.