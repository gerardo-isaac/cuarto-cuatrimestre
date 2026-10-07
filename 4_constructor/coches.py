print("\033c")

class Coches:
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self.__marca = marca
        self.__color = color
        self.__modelo = modelo
        self.__velocidad = velocidad
        self.__caballaje = caballaje
        self.__plazas = plazas

    def acelerar(self):
        self.__velocidad += 1   

    def frenar(self):
        self.__velocidad -= 1


