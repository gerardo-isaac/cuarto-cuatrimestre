"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches

class Coches:
    def __init__(self, color, marca, velocidad):
        self.__color=color
        self.__marca=marca
        self.__velocidad=velocidad

    def acelerar (self):
        pass    
    def renar (self):
        pass
    def tocas_claxon (self):
        pass 


print(f"el color del coche1 es: {coche1.__color}")
#Instanciar o crear objetos de la clase Coches

coche1=Coches("rojo", "VW", 220)
coche2=Coches("azul", "nissan", 180)






