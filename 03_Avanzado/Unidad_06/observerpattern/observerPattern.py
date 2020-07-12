def show_table_by_element(fetched, index):
    print("fetched: ", fetched, " index: ", index)

class Publicador:

    observadores = []
    
    def Agregar(self, obj):
        self.observadores.append(obj)
        
    def Quitar(self, obj):
        pass
        
    def Notificar(self):
        for observador in self.observadores:
            observador.Update()
            
class Publicacion(Publicador):
    def __init__(self):
        self.estado = None
        
    def SetEstado(self, value):
        self.estado = value
        self.Notificar()
        
    def GetEstado(self):
        return self.estado
        
class Observador:
    def Update(self):
        raise NotImplementedError("Delegación de actualización")
        
class ConcreteObserverID(Observador):
    def __init__(self, obj):
        self.observadorID = obj
        self.observadorID.Agregar(self)
            
    def Update(self):
        print("Actualización dentro de ConcreteObserverID")
        self.estado = self.observadorID.GetEstado().get("id")
        show_table_by_element(self.estado, "#1")

class ConcreteObserverTitulo(Observador):
    def __init__(self, obj):
        self.observadorB = obj
        self.observadorB.Agregar(self)

    def Update(self):
        print("Actualización dentro de ConcreteObserverTitulo")
        self.estado = self.observadorB.GetEstado().get("titulo")
        show_table_by_element(self.estado, "#2")

class ConcreteObserverFecha(Observador):
    def __init__(self, obj):
        self.observadorB = obj
        self.observadorB.Agregar(self)

    def Update(self):
        print("Actualización dentro de ConcreteObserverFecha")
        self.estado = self.observadorB.GetEstado().get("fecha")
        show_table_by_element(self.estado, "#3")

class ConcreteObserverDescripcion(Observador):
    def __init__(self, obj):
        self.observadorB = obj
        self.observadorB.Agregar(self)

    def Update(self):
        print("Actualización dentro de ConcreteObserverDescripcion")
        self.estado = self.observadorB.GetEstado().get("descripcion")
        show_table_by_element(self.estado, "#4")

class ConcreteObserverEstado(Observador):
    def __init__(self, obj):
        self.observadorB = obj
        self.observadorB.Agregar(self)

    def Update(self):
        print("Actualización dentro de ConcreteObserverEstado")
        self.estado = self.observadorB.GetEstado().get("estado")
        show_table_by_element(self.estado, "#5")

class ConcreteObserverObjeto(Observador):
    def __init__(self, obj):
        self.observadorB = obj
        self.observadorB.Agregar(self)

    def Update(self):
        print("Actualización dentro de ConcreteObserverObjeto")
        self.estado = self.observadorB.GetEstado().get("objeto")
        show_table_by_element(self.estado, "#6")


register = {"id": 1, "titulo":"titulo prueba", "descripcion": "descrip prueba", "fecha": "hoy", "estado": "est pr",
            "objeto": "obj test"}
tema1 = Publicacion()
observador_id = ConcreteObserverID(tema1)
observador_titulo = ConcreteObserverTitulo(tema1)
observador_fecha = ConcreteObserverFecha(tema1)
observador_descripcion = ConcreteObserverDescripcion(tema1)
observador_estado = ConcreteObserverEstado(tema1)
observador_objeto = ConcreteObserverObjeto(tema1)
tema1.SetEstado(register)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
