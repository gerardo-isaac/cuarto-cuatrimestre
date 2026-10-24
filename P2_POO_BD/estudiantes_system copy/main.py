from estudiantes import estudiantesBD

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

    def datos_estudiantes(self, tipo):
        self.borrarPantalla()
        print(f"\n\t\t...Ingresa los datos del {tipo}...")

        estudiantitos = {}

        estudiantitos['nombre'] = input(
            "\t\tIngresa el nombre del estudiante: "
        ).strip().upper()

        try:
            estudiantitos['nota'] = float(
                input("\t\tIngresa la nota del estudiante: ").strip()
            )
        except ValueError:
            print("\t\tError: La nota debe ser un numero.")
            self.esperarTecla()
            return None

        return estudiantitos

    def menu_estudiantes(self):
        opcion = True

        while opcion:
            self.borrarPantalla()
            opcion = self.menu_acciones("Estudiantes")

            match opcion:
                case '1':
                    self.borrarPantalla()
                    estudiantitos = self.datos_estudiantes("estudiante")

                    if estudiantitos is not None:
                        estudiante1 = estudiantesBD.EstudiantesBD(
                            estudiantitos['nombre'],
                            estudiantitos['nota']
                        )

                        respuesta = estudiante1.insertar()
                        self.respuesta_sql(respuesta)
                        del estudiante1

                case '2':
                    self.borrarPantalla()

                    try:
                        id_estudiante = int(
                            input("Ingresa el ID del estudiante a eliminar: ").strip()
                        )

                        respuesta = estudiantesBD.EstudiantesBD.eliminar(
                            id_estudiante
                        )
                        self.respuesta_sql(respuesta)

                    except ValueError:
                        print("\t\tError: El ID debe ser un numero.")
                        self.esperarTecla()

                case '3':
                    self.borrarPantalla()
                    id_estudiante = int(input("Ingresa el ID del estudiante a actualizar: ").strip())
                    estudiantitos = self.datos_estudiantes("estudiante")

                    estudiante1 = estudiantesBD.EstudiantesBD
                    respuesta = estudiante1.actualizar(id_estudiante)
                    self.respuesta_sql(respuesta)
                    del estudiante1

                case '4':
                    self.borrarPantalla()
                    registros = estudiantesBD.EstudiantesBD.consultar()

                    if registros and len(registros) > 0:
                        num_estudiante = 1

                        for fila in registros:
                            print(
                                f"\n\t\t...::: Estudiante # {num_estudiante} :::..."
                            )
                            print(f"ID: {fila[0]}")
                            print(f"Nombre: {fila[1]}")
                            print(f"Nota: {fila[2]}")
                            num_estudiante += 1

                        self.esperarTecla()

                    else:
                        print("\n\n\t\tNo existen datos que mostrar por el momento.")
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
            print("1.- Estudiantes")
            print("2.- Salir")

            opcion = input("Elige una opcion: ").strip()

            match opcion:
                case '1':
                    self.borrarPantalla()
                    self.menu_estudiantes()

                case '2':
                    self.borrarPantalla()
                    print("...Salir del sistema...")
                    opcion = False

                case _:
                    input("\t\t\t...Opcion invalida...")


if __name__ == "__main__":
    app = App()