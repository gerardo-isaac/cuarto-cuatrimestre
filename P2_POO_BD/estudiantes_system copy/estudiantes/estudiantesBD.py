from conexionBD import cursor, conexion

class EstudiantesBD:
    def insertar(self, nombre, nota):
        try:
            cursor.execute("insert into estudiante values (null, %s, %s)", (nombre, nota))
            conexion.commit()
            return True
        except:
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from estudiante")
            return cursor.fetchall()
        except:
            return []

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from estudiante where id=%s",(id,))
            conexion.commit()
            return True
        except:
            return False

    def actualizar(self, nombre, nota, id):
        try:
            cursor.execute("update estudiante set nombre=%s, nota=%s where id=%s",(nombre, nota, id))
            conexion.commit()
            return True
        except: 
            return False