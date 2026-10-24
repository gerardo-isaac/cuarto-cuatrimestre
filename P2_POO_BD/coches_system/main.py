from coches import coches

class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        print("\033c")

    def esperarTecla(self):
        input("\t\t\t...Presiona una tecla para continuar...")

    def menu_acciones(self, tipo):
        print(f"\t\t\t...::: Menu de {tipo} :::...")
        print("\t\t1.- Agregar")
        print("\t\t2.- Borrar")
        print("\t\t3.- Modificar")
        print("\t\t4.- Mostrar")
        print("\t\t5.- Salir")
        opcion = input("\n\t\tElige una opcion: ").strip()
        return opcion

    def respuesta_sql(self, respuesta):
        if respuesta:
            input("\t\t\t...Accion realizada con exito...")
        else:
            input("\t\t\t...Esta accion no puede realizarse...")

    def datos_coches(self, tipo):
        self.borrarPantalla()
        print(f"\n\t\t...Ingresa los datos del {tipo}...")
        cochesitos={}
        cochesitos['marca'] = input("\t\tIngresa la marca del coche: ").upper().strip()
        cochesitos['color'] = input("\t\tIngresa el color del coche: ").upper().strip()
        cochesitos['modelo'] = input("\t\tIngresa el modelo del coche: ").upper().strip()
        cochesitos['velocidad'] = input("\t\tIngresa la velocidad: ").strip()
        cochesitos['potencia'] = input("\t\tIngresa la potencia: ").strip()
        cochesitos['asientos'] = input("\t\tIngresa el numero de asientos: ").strip()

        return cochesitos

    def menu_coche(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = self.menu_acciones("Coches")
            match opcion:
                case '1':
                    self.borrarPantalla()
                    cochesitos = self.datos_coches("Coche")
                    coche1 = coches.Coches(cochesitos['marca'], cochesitos['color'], cochesitos['modelo'], cochesitos['velocidad'], cochesitos['potencia'], cochesitos['asientos'])

                    respuesta = coche1.insertar()
                    self.respuesta_sql(respuesta)
                    del coche1

                case '2':
                    self.borrarPantalla()
                    try:
                        id = int(input("Ingresa el ID del coche a eliminar: ").strip())
                        respuesta = coches.Coches.eliminar(id)
                        self.respuesta_sql(respuesta)
                    except:
                        print("\t\tError: El ID debe ser un numero.")
                        self.esperarTecla()

                case '3':
                    self.borrarPantalla()
                    try:
                        id = int(input("Ingresa el ID del coche a actualizar: ").strip())
                        cochesitos = self.datos_coches("Coche")
                        coche1 = coches.Coches(cochesitos['marca'], cochesitos['color'], cochesitos['modelo'], cochesitos['velocidad'], cochesitos['potencia'], cochesitos['asientos'])

                        respuesta = coche1.actualizar(id)
                        self.respuesta_sql(respuesta)
                        del coche1

                    except:
                        print("\t\tError: El ID debe ser un numero.")
                        self.esperarTecla()

                case '4':
                    self.borrarPantalla()
                    registros = coches.Coches.consultar()

                    if registros and len(registros) > 0:
                        num_coches = 1
                        for fila in registros:
                            print(f"\n\t\t...::: Coche # {num_coches} :::...")
                            print(f"ID: {fila[0]}")
                            print(f"Marca: {fila[1]}")
                            print(f"Color: {fila[2]}")
                            print(f"Modelo: {fila[3]}")
                            print(f"Velocidad: {fila[4]}")
                            print(f"Potencia: {fila[5]}")
                            print(f"Asientos: {fila[6]}")
                            num_coches += 1
                        self.esperarTecla()
                    else:
                        print("\n\n\t NO existen datos que mostrar por el momento")
                        self.esperarTecla()

                case '5':
                    self.borrarPantalla()
                    print("\t\t...Regresando al menu principal...")
                    opcion = False

                case _:
                    input("\t\t\t...Opcion invalida...")

    def main(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            print("\n\t\t\t...::: Menu Principal :::...\n")
            print("1.- Coches")
            print("2.- Salir")
            opcion = input("Elige una opcion: ").strip()
            match opcion:
                case '1':
                    self.borrarPantalla()
                    self.menu_coche()
                case '2':
                    self.borrarPantalla()
                    print("...Salir del sistema...")
                    opcion = False
                case _:
                    input("\t\t\t...Opcion invalida...")

if __name__ == "__main__":
    app = App()
