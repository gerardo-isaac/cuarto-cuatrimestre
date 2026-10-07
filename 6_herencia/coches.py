print("\033c")

class Coches:
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencina = potencia
        self._asientos = asientos

    def acelerar(self):
        self._velocidad += 1   

    def frenar(self):
        self._velocidad -= 1

#Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
# En teoria se deberia de crear un metodo Getters y Setters por   cada atributo que contenga la clase
#   Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
#Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    def getVelocidad(self):
        return self._velocidad 

    def setVelocidad(self,velocidad):
        self._velocidad=velocidad

    def getMarca(self):
        return self._marca 

    def setMarca(self,marca):
        self._marca=marca

    def getColor(self):
        return self._color 

    def setColor(self,color):
        self._color=color

    def getModelo(self):
        return self._modelo 

    def setModelo(self,modelo):
        self._modelo=modelo

    def getCaballaje(self):
        return self._potencia 

    def setCaballaje(self,potencia):
        self._potencia=potencia

    def getPlazas(self):
        return self._asientos

    def setPlazas(self,asientos):
        self._plazas=asientos



class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos, eje, capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, potencia, asientos)
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga

    def cargar(self,tipo_carga):
        print(f"el tipo de carga del camion es: {tipo_carga}")

    def acelerar(self):
        self._velocidad += 1    
        print("estoy acelerando como un camion...")

    def frenar(self):
        self._velocidad -= 1
        print("estoy frenando como un camion...")

    def geteje(self):
        return self.__eje
    
    def seteje(self,eje):
        self.__eje=eje 

    def getcapacidadCarga(self):
        return self.__capacidadCarga
    
    def setcapacidadCagarga(self, capacidadCarga):
        self.__capacidadCarga=capacidadCarga


class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos, traccion, cerrada):
        super().__init__(marca, color, modelo, velocidad, potencia, asientos)
        self.__traccion=traccion
        self.__cerrada=cerrada

        def transportar(self,num_pasajeros):
            print(f"el numero de pasajeros en la camioneta es: {num_pasajeros}")

        def acelerar(self):
            self._velocidad += 1    
            print("estoy acelerando como una camioneta...")

        def frenar(self):
            self._velocidad -= 1
            print("estoy frenando como una camioneta...")

        def setTraccion(self,traccion):
            self.__traccion=traccion

        def getTreaccion(self):
            return self.__traccion


        def setCerrada(self,cerrada):
            self.__cerrada=cerrada

        def getcerrada(self):
            return self.__cerrada