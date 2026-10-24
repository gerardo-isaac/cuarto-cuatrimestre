from conexionBD import conexion, cursor
from coches import coches

class Camiones(coches.Coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos, eje, capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, potencia, asientos)
        self.__eje = eje
        self.__capacidadCarga = capacidadCarga

    def acelerar(self):
        self._velocidad += 2

    def frenar(self):
        self._velocidad -= 2

    def cargar(self, tipo_carga):
        print(f"El tipo de carga del camion es: {tipo_carga}")


    @property
    def eje(self):
        return self.__eje

    @property
    def capacidadCarga(self):
        return self.__capacidadCarga


    @eje.setter
    def eje(self, eje):
        self.__eje = eje

    @capacidadCarga.setter
    def capacidadCarga(self, capacidadCarga):
        self.__capacidadCarga = capacidadCarga


    def insertar(self):
        try:
            cursor.execute("insert into camiones values (null, %s, %s, %s, %s, %s, %s, %s, %s)", (self._marca, self._color, self._modelo, self._velocidad, self._potencia, self._asientos, self.__eje, self.__capacidadCarga))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from camiones")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from camiones where id=%s", (id,))
            conexion.commit()
            return True
        except:
            return False

    def actualizar(self, id):
        try:
            cursor.execute("update camiones set marca=%s, color=%s, modelo=%s, velocidad=%s, potencia=%s, asientos=%s, eje=%s, capacidadCarga=%s where id=%s", (self._marca, self._color, self._modelo, self._velocidad, self._potencia, self._asientos, self.__eje, self.__capacidadCarga, id))
            conexion.commit()
            return True
        except:
            return False