class Paridad:
    def __set_name__(self, owner, nombre):
        self.nombre = nombre
    def __get__(self, instancia, type=None) -> object:
        return instancia.__dict__.get(self.nombre) or 0
    def __set__(self, instancia, valores) -> None:
        aux = [0]*len(valores)
        for index in range(len(valores)):
            aux[index] = valores[index] if valores[index] % 2 == 0 else 0
        instancia.__dict__[self.nombre] = aux
    
class Evaluar:
    evaluar_paridad = Paridad()
  

el_valor = Evaluar()
el_valor.evaluar_paridad = [1,2,3,4,5,6,7,8,9]
print(el_valor.evaluar_paridad)
