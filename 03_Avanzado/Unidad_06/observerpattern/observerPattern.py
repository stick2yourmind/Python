class Publicador:
    observadores = []

    def Agregar(self, obj):
        self.observadores.append(obj)

    def Quitar(self, obj):
        pass

    def Notificar(self, F):
        for observador in self.observadores:
            observador.Update(F)


class Publicacion(Publicador):
    def __init__(self):
        self.estado = None

    def SetEstado(self, value, F):
        self.estado = value
        self.Notificar(F)

    def GetEstado(self):
        return self.estado


class Observador:
    def Update(self, F):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverID(Observador):
    def __init__(self, obj):
        self.observadorID = obj
        self.observadorID.Agregar(self)

    def Update(self, F):
        print("Actualización dentro de ConcreteObserverID")
        self.estado = self.observadorID.GetEstado().get("id")
        F(self.estado, "#1")


class ConcreteObserverTitulo(Observador):
    def __init__(self, obj):
        self.observadorB = obj
        self.observadorB.Agregar(self)

    def Update(self, F):
        print("Actualización dentro de ConcreteObserverTitulo")
        self.estado = self.observadorB.GetEstado().get("titulo")
        F(self.estado, "#2")


class ConcreteObserverDescripcion(Observador):
    def __init__(self, obj):
        self.observadorB = obj
        self.observadorB.Agregar(self)

    def Update(self, F):
        print("Actualización dentro de ConcreteObserverDescripcion")
        self.estado = self.observadorB.GetEstado().get("descripcion")
        F(self.estado, "#3")


class ConcreteObserverFecha(Observador):
    def __init__(self, obj):
        self.observadorB = obj
        self.observadorB.Agregar(self)

    def Update(self, F):
        print("Actualización dentro de ConcreteObserverFecha")
        self.estado = self.observadorB.GetEstado().get("fecha")
        F(self.estado, "#4")


class ConcreteObserverEstado(Observador):
    def __init__(self, obj):
        self.observadorB = obj
        self.observadorB.Agregar(self)

    def Update(self, F):
        print("Actualización dentro de ConcreteObserverEstado")
        self.estado = self.observadorB.GetEstado().get("estado")
        F(self.estado, "#5")


class ConcreteObserverObjeto(Observador):
    def __init__(self, obj):
        self.observadorB = obj
        self.observadorB.Agregar(self)

    def Update(self, F):
        print("Actualización dentro de ConcreteObserverObjeto")
        self.estado = self.observadorB.GetEstado().get("objeto")
        F(self.estado, "#6")