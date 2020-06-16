from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import sys
sys.path.append('..')
from controller.controller_main import *
from .view_extras import *

"""
           1º column                  2º column                     3º column           4º column
+---------------------------+-------------------------+------------------------------+-------------+
|                                          Label"Ingrese sus datos"                                |--> 1º row
+---------------------------+-------------------------+------------------------------+-------------+
| Label"Titulo"             | Entry_Title             |           None               |     None    |--> 2º row
+---------------------------+-------------------------+------------------------------+-------------+
| Label"Descripción"        | Entry_Description       |           None               |     None    |--> 3º row
| --------------------------+-------------------------+------------------------------+-------------+
|                                           Button"Mostrar registros"                              |--> 4º row
| --------------------------+-------------------------+------------------------------+-------------+
| Treeview_Head"ID"         | Treeview_Head"Titulo"   | Treeview_Head"Descripción"   |             |
| Treeview_Item01"ID"       | Treeview_Item01"Titulo" | Treeview_Item01"Descripción" |  Scrollbar  |--> 5º row
| Treeview_Item02"ID"       | Treeview_Item02"Titulo" | Treeview_Item02"Descripción" |             |
| --------------------------+------------------------ | -----------------------------+-------------+
| Button"CreateDB"          | Button"Alta"            |           None               |     None    |--> 6º row
+---------------------------+-------------------------+------------------------------+-------------+
|                                           Widget selector de temas                               |--> 7º row
+---------------------------+-------------------------+------------------------------+-------------+
|                                           Widget selector de temas                               |--> 8º row
+---------------------------+-------------------------+------------------------------+-------------+
|                                           Widget selector de temas                               |--> 9º row
+---------------------------+-------------------------+------------------------------+-------------+
|                                           Widget selector de temas                               |--> 10º row
+---------------------------+-------------------------+------------------------------+-------------+
"""
ERROR_TITLE = "El título solo puede contener letras mayúsculas y/o minúsculas, espacios, \
guiones bajos y medios.Además el primer y último carácter deben ser letras. En caso \
de utilzar un espacio, un guion bajo o un guion medio, cualquiera de ellos debe ser \
seguido por una letra ya sea mayúscula, o minúscula."
ERROR_CONNECTION = "No se ha podido conectar a la base de datos."
ERROR_DELETE = "No se ha podido eliminar el registro debido a que no posee conexion a la base de datos o no se " \
               "encontro el id especificado."
ERROR_SELECT_ITEM = "No ha seleccionado un registro. Para seleccionar un registro debe hacer doble click sobre el " \
                    "registro deseado."

class WindowView:
    def __init__(self, tab):
        self.item_selected=None
        self.title_selected=None
        self.description_selected=None
        self.var_entry = [-1, -1]
        self.window = Tk()
        self.window.title("Tarea POO")
        self.frame_mw = Frame(self.window)
        self.frame_mw.pack()
        self.frame_mw.Label_head = ""
        self.title = 0
        self.var_entry[self.title] = StringVar()
        self.frame_mw.Label_title = ""
        self.frame_mw.Entry_title = ""
        self.description = 1
        self.var_entry[self.description] = StringVar()
        self.frame_mw.Label_description = ""
        self.frame_mw.Entry_description = ""
        self.frame_mw.Button_showReg = ""
        self.frame_mw.Table = ""
        self.frame_mw.Scrollbar = ""
        self.frame_mw.createDB = ""
        self.frame_mw.addRegister = ""
        self.frame_mw.updateRegister = ""
        self.frame_mw.deleteRegister = ""
        self.frame_mw.Radio_theme_default = ""
        self.frame_mw.Radio_theme_1 = ""
        self.frame_mw.Radio_theme_2 = ""
        self.frame_mw.Radio_theme_3 = ""
        self.radio_var = StringVar()
        self.layout_make(tab)
        center(self.window)

    def layout_make(self, tab="default"):
        if tab=="default":
            self.frame_mw.pack()
            # First row
            self.frame_mw.Label_head = Label(self.frame_mw)
            # Second row
            self.frame_mw.Label_title = Label(self.frame_mw)
            self.frame_mw.Entry_title = Entry(self.frame_mw)
            # Third row
            self.frame_mw.Label_description = Label(self.frame_mw)
            self.frame_mw.Entry_description  = Entry(self.frame_mw)
            # Fourth row
            self.frame_mw.Button_showReg = Button(self.frame_mw)
            # Fifth row - Treeview
            self.frame_mw.Table = ttk.Treeview(self.frame_mw)
            # Adding scrollbar to treeview
            self.frame_mw.Scrollbar = ttk.Scrollbar(self.frame_mw)
            # Sixth row
            self.frame_mw.createDB = Button(self.frame_mw)
            self.frame_mw.addRegister = Button(self.frame_mw)
            self.frame_mw.updateRegister = Button(self.frame_mw)
            self.frame_mw.deleteRegister = Button(self.frame_mw)
            # Seventh row
            self.frame_mw.Radio_theme_default = Radiobutton(self.frame_mw)
            self.frame_mw.Radio_theme_1 = Radiobutton(self.frame_mw)
            self.frame_mw.Radio_theme_2 = Radiobutton(self.frame_mw)
            self.frame_mw.Radio_theme_3 = Radiobutton(self.frame_mw)
        self.layout_config(tab)

    def layout_config(self, tab="default"):
        if tab=="default":
            # First row
            self.frame_mw.Label_head.configure(text="Ingrese sus datos", bg="#b92041", fg="white",
                                               font=('Helvetica', 16, "bold"))
            self.frame_mw.Label_head.grid(row=0, columnspan=5, sticky="nsew")
            # Second row
            self.frame_mw.Label_title.configure(text = "Título", width = 22, anchor = W)
            self.frame_mw.Label_title.grid(row=1, column=0, columnspan=2)
            self.frame_mw.Entry_title.configure(textvariable = self.var_entry[self.title], width = 120)
            self.frame_mw.Entry_title.grid(row=1, column=1, columnspan=4)
            # Third row
            self.frame_mw.Label_description.configure(text="Descripción", width=22, anchor=W)
            self.frame_mw.Label_description.grid(row=2, column=0, columnspan=2)
            self.frame_mw.Entry_description.configure(textvariable=self.var_entry[self.description], width=120)
            self.frame_mw.Entry_description.grid(row=2, column=1, columnspan=4)
            # Fourth row
            #self.frame_mw.Button_showReg.configure(text="Mostrar registros", state="disable")
            self.frame_mw.Button_showReg.configure(text="Mostrar registros", command= self.click_show_reg)
            self.frame_mw.Button_showReg.grid(row=3, column=0, columnspan=5)
            # Fifth row
            self.frame_mw.Table.grid(row=4, column=0, columnspan=4, sticky="nsew")
            # Adding headings
            self.frame_mw.Table["columns"] = ("1", "2", "3", "4", "5", "6")
            self.frame_mw.Table['show'] = 'headings'
            self.frame_mw.Table.heading("1", text="id")
            self.frame_mw.Table.heading("2", text="Titulo")
            self.frame_mw.Table.heading("3", text="Fecha")
            self.frame_mw.Table.heading("4", text="Descripción")
            self.frame_mw.Table.heading("5", text="Estado")
            self.frame_mw.Table.heading("6", text="Objeto")
            # Binding double click to table´s item
            self.frame_mw.Table.bind("<Double-1>", lambda x: self.table_double_click())
            # Config. scrollbar row
            self.frame_mw.Scrollbar.configure(orient='vertical', command=self.frame_mw.Table.yview)
            self.frame_mw.Scrollbar.grid(row=4, column=4, sticky="nsew")
            self.frame_mw.Table.configure(yscrollcommand=self.frame_mw.Scrollbar.set)
            # Sixth row
            self.frame_mw.createDB.configure(text="Crear base de datos y tabla", command=self.click_create_d_b)
            self.frame_mw.createDB.grid(row=5, column=0)
            self.frame_mw.addRegister.configure(text="Alta", command= lambda : [self.click_add_reg(
                self.var_entry[self.title].get(), self.var_entry[self.description].get())])
            self.frame_mw.addRegister.grid(row=5, column=1)
            self.frame_mw.updateRegister.configure(text="Actualizar", command= lambda : [self.click_update_reg()])
            self.frame_mw.updateRegister.grid(row=5, column=2)
            self.frame_mw.deleteRegister.configure(text="Eliminar", command= lambda : [self.click_delete_reg()])
            self.frame_mw.deleteRegister.grid(row=5, column=3)
            # Seventh row . theme default
            self.frame_mw.Radio_theme_default.configure(text="Default", variable=self.radio_var,
                                                        background="SystemButtonFace", value="SystemButtonFace",
                        command= lambda : self.ch_color("default"))
            self.frame_mw.Radio_theme_default.grid(row=6, columnspan=5, sticky="nsew")
            # Seventh row . theme 1
            self.frame_mw.Radio_theme_1.configure(text="Naranja", variable=self.radio_var, background="#eb6434",
                                                  value="#eb6434", command= lambda : self.ch_color("tema_1"),
                                                  foreground = "white")
            self.frame_mw.Radio_theme_1.grid(row=7, columnspan=5, sticky="nsew")
            # Seventh row . theme 2
            self.frame_mw.Radio_theme_2.configure(text="Azul", variable=self.radio_var, background="#264653",
                                                       value="#264653", command= lambda : self.ch_color("tema_2"),
                                                  foreground = "white")
            self.frame_mw.Radio_theme_2.grid(row=8, columnspan=5, sticky="nsew")
            # Seventh row . theme 3
            self.frame_mw.Radio_theme_3.configure(text="Verdeazulado", variable=self.radio_var, background="#119296",
                                                  value="#119296", command= lambda : self.ch_color("tema_3"),
                                                  foreground = "white")
            self.frame_mw.Radio_theme_3.grid(row=9, columnspan=5, sticky="nsew")
            # Unselect radio buttons
            self.radio_var.set(0)
            self.clean_entry()
            controller_theme("default", "SystemButtonFace", act="save")
            controller_theme("tema_1", "#eb6434", act="save")
            controller_theme("tema_2", "#264653", act="save")
            controller_theme("tema_3", "#119296", act="save")

    def clean_entry(self):
        self.var_entry[self.title].set("")
        self.var_entry[self.description].set("")

    def clean_table(self):
        for i in self.frame_mw.Table.get_children():
            self.frame_mw.Table.delete(i)

    def show_table(self, fetched):
        for x in range(len(fetched)):
            item = fetched[x]
            self.frame_mw.Table.insert("", 'end', values=(item[0], item[1], item[2]))

    def click_show_reg(self):
        fetched = controller_show_reg()
        if fetched == -1:
            showerror("¡Error de conexión!", ERROR_CONNECTION)
        else:
            self.clean_table()
            self.show_table(fetched)

    def click_add_reg(self, input_title, input_description):
        aux = controller_add_reg(input_title, input_description)
        if aux == 0:
            showerror("¡Título no válido!", ERROR_TITLE)
        elif aux == -1:
            showerror("¡Error de conexión!", ERROR_CONNECTION)
        elif aux > 0:
            self.clean_entry()
            self.click_show_reg()

    def click_update_reg(self):
        if None != self.item_selected:
            self.title_selected = self.var_entry[self.title].get()
            self.description_selected = self.var_entry[self.description].get()
            aux = controller_update_reg(self.item_selected, self.title_selected, self.description_selected)
            print("click_update_reg aux :" + str(aux))
            if aux == -1:
                showerror("¡Error de conexión!", ERROR_CONNECTION)
            if aux == 0:
                showerror("¡Registro no requiere ser modificado!", "No ha realizado cambios en el registro.")
            else:
                self.item_selected = None
                self.title_selected = None
                self.description_selected = None
                self.clean_entry()
                self.click_show_reg()
                showinfo("Actualizado", "Actualización del registro finalizado con exito.")
        else:
            showerror("¡Registro no seleccionado!", ERROR_SELECT_ITEM)

    def click_delete_reg(self):
        if None != self.item_selected:
            aux = controller_delete_reg(self.item_selected)
            if aux == -1 or aux == 0:
                showerror("¡Error durante la eliminación del registro!", ERROR_DELETE)
            else:
                self.item_selected = None
                self.title_selected = None
                self.description_selected = None
                self.clean_entry()
                self.click_show_reg()
        else:
            showerror("¡Registro no seleccionado!", ERROR_SELECT_ITEM)


    def ch_color(self, theme_name):
        r = controller_theme(theme_name, act="choose")
        self.window.configure(background=r)
        self.frame_mw.configure(background=r)

    def table_double_click(self):
        self.item_selected=self.frame_mw.Table.item(self.frame_mw.Table.focus())
        print(self.item_selected)
        # Load focus item into entry's
        self.var_entry[self.description].set(str(self.item_selected["values"][2]))
        self.var_entry[self.title].set(str(self.item_selected["values"][1]))
        # Save item's ID into self.item_selected
        self.description_selected=str(self.item_selected["values"][2])
        self.title_selected=str(self.item_selected["values"][1])
        self.item_selected = str(self.item_selected["values"][0])
        print("ID: " + self.item_selected)

    @staticmethod
    def click_create_d_b():
        aux = controller_create_d_b()
        if aux == -1:
            showerror("¡Error de conexión!", ERROR_CONNECTION)



# Testing src
# a = WindowView()
# a.layout_make(tab="default")
# mainloop()