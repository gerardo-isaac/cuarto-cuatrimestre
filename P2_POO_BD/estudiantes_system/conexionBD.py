import mysql.connector
try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_estudiantes"
    )

    cursor = conexion.cursor(buffered=True)
except:
    print("... Por el momento no es posible conctarse con la base de datos. Intentelo más tarde ...")