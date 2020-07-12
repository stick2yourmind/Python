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
        self.observadorA = obj
        self.observadorA.Agregar(self)
            
    def Update(self):
        print("Actualización dentro de ConcreteObserverID")
        self.estado1 = self.observadorA.GetEstado().get("id")
        print("ID = ", self.estado1)

class ConcreteObserverTitulo(Observador):
    def __init__(self, obj):
        self.observadorB = obj
        self.observadorB.Agregar(self)

    def Update(self):
        print("Actualización dentro de ConcreteObserverTitulo")
        self.estado = self.observadorB.GetEstado().get("titulo")
        print("titulo = ", self.estado)


class ConcreteObserverTitulo(Observador):
    def __init__(self, obj):
        self.observadorB = obj
        self.observadorB.Agregar(self)

    def Update(self):
        print("Actualización dentro de ConcreteObserverTitulo")
        self.estado = self.observadorB.GetEstado().get("titulo")
        print("titulo = ", self.estado)



register = {"id": 1, "titulo":"titulo de prueba", "descripcion": "descripcion de prueba"}
tema1 = Publicacion()
observadorA = ConcreteObserverID(tema1)
observadorB = ConcreteObserverTitulo(tema1)
tema1.SetEstado(register)
print(observadorA.__dict__)
print(observadorB.__dict__)
print('---'*25)
print(Publicador.__dict__)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
