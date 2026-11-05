from coches import coches
from tkinter import Tk,Label,Entry,Button,messagebox


class App:
    def __init__ (self, ventana):
        self.ventana=ventana
        self.ventana.title("Gestión de Coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0)
        self.main()

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def main(self):
        self.borrarPantalla()
        Label(self.ventana,text=" ::: MENU PRINCIPAL :::").pack(pady=20)
        Button(self.ventana,text="1.- Coches",command=self.menu_acciones).pack(pady=10)
        Button(self.ventana,text="2.- Salir",command=self.ventana.quit).pack(pady=10)

    def menu_acciones(self):
        self.borrarPantalla()
        tipo="Coche"
        Label(self.ventana,text=f" ::: Menú de {tipo} :::").pack(pady=10)
        Button(self.ventana,text="1.- Agregar",command=self.insertar_coche_view).pack(pady=10)
        Button(self.ventana,text="2.- Borrar",command=self.eliminar_coche_view).pack(pady=10)
        Button(self.ventana,text="3.- Modificar",command=self.modificar_coche_view).pack(pady=10)
        Button(self.ventana,text="4.- Mostrar",command=self.consultar_coche_view).pack(pady=10)
        Button(self.ventana,text="5.- Salir",command=self.main).pack(pady=10)

    def insertar_coche_view (self):
        self.borrarPantalla()
        Label(self.ventana,text="... Ingresar los datos del coche").pack(pady=10)

        Label(self.ventana,text="Marca").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)

        Label(self.ventana,text="Color").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana,text="Modelo").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)
        
        Label(self.ventana,text="Velocidad").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana,text="Potencia").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana,text="# de Asientos").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(self.ventana,text=":: Agregar ::",command=self.insertar_coche_controller).pack(pady=5)

        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)

    def insertar_coche_controller(self):
        coches1=coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coches1.insertar()
        self.respuesta_sql(respuesta)
        del coches1

    def eliminar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="... Ingrese el ID del coche a eliminar").pack(pady=10)
        
        Label(self.ventana,text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Button(self.ventana,text=":: Eliminar ::",command=self.eliminar_coche_controller).pack(pady=5)

        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)

    def eliminar_coche_controller(self):
        respuesta=coches.Coches.eliminar(self.id.get())
        self.respuesta_sql(respuesta)

    def consultar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="..::Consultar Coches::..").pack(pady=10)
        filas=""
        filas=self.consultar_coche_controller(filas)
        Label(self.ventana,text=f"{filas}").pack(pady=5)
        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)

    def consultar_coche_controller(self,filas):
        registros=coches.Coches.consultar()
        num_coche=1
        if len(registros) > 0:
            for fila in registros:
                filas=filas+(f"\n\t Coche #: {num_coche}\n\t ID: {fila[0]} \n\t Marca: {fila[1]} \n\t Color: {fila[2]} \n\t Modelo: {fila[3]}\n\t Velocidad: {fila[4]} \n\t Potencia: {fila[5]} \n\t Asientos: {fila[0]}")
                num_coche+=1
        else:
            filas="¡No se encontró información en la BD!..."
        return filas

    def modificar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="... Ingrese el ID del coche a modificar").pack(pady=10)
                
        Label(self.ventana,text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Label(self.ventana,text="... Datos del coche").pack(pady=10)
        
        Label(self.ventana,text="Marca").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.pack(pady=5)

        Label(self.ventana,text="Color").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana,text="Modelo").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)
        
        Label(self.ventana,text="Velocidad").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana,text="Potencia").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana,text="# de Asientos").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(self.ventana,text=":: Modificar ::",command=self.modificar_coche_controller).pack(pady=5)

        Button(self.ventana,text=":: Regresar ::",command=self.menu_acciones).pack(pady=5)

    def modificar_coche_controller(self):
        id=self.id.get()
        coches1=coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coches1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coches1
    
    # def terminarSistema(self):
    #     input("....:::: GRACIAS POR UTILIZAR NUESTRO SISTEMA, \n  vuelve pronto ::::...")

    # def menu_acciones(self,tipo):
    #     print(f"\t\t....:::: MENU DE {tipo} ::::...\n")
    #     opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Salir\n\t\tEscribe una opción: ").strip()
    #     return opcion

    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(title=":: Exitoso ::",message="¡Acción realizada con éxito!...")
        else:
            input("\n\t\t.... ¡Acción no realizada, vuelve a intentarlo!.... ")
            messagebox.showerror(title=":: Verifique por favor",message="¡Esta acción no pudo realizarse en este momento!...")

    # def datos_coche(self,tipo):
    #     self.borrarPantalla()
    #     print(f"\n\t ...Ingresar los datos del {tipo}")
    #     cochesito={}
    #     cochesito["marca"]=input("Marca: ").upper().strip()
    #     cochesito["color"]=input("Color: ").upper().strip()
    #     cochesito["modelo"]=input("Modelo: ").upper().strip()
    #     cochesito["velocidad"]=int(input("Velocidad (Km/h): ").strip())
    #     cochesito["potencia"]=int(input("Potencia (Hp): ").strip())
    #     cochesito["asientos"]=int(input("# de Asientos: ").strip())
    #     return cochesito
    
    # def menu_coches(self):
    #     opc=True
    #     while opc:
    #         self.borrarPantalla()
    #         opc=self.menu_acciones("Coches")
    #         match opc:
    #             case '1':
    #                 #Solicitar datos y crear objetos de coche
    #                 cochesito=self.datos_coche("Coche")
    #                 coches1=coches.Coches(cochesito["marca"],cochesito["color"],cochesito["modelo"],cochesito["velocidad"],cochesito["potencia"],cochesito["asientos"])
    #                 #Crear objetos de CochesBD y luego insertar a la BD
    #                 coches1=coches.Coches(cochesito["marca"],cochesito["color"],cochesito["modelo"],cochesito["velocidad"],cochesito["potencia"],cochesito["asientos"])
    #                 respuesta=coches1.insertar()
    #                 self.respuesta_sql(respuesta)
    #                 del coches1

    #             case '2':
    #                 self.borrarPantalla()
    #                 id=input("Ingrese el ID del coche a eliminar: ").strip()
    #                 respuesta=coches.Coches.eliminar(id)
    #                 self.respuesta_sql(respuesta)

    #             case '3':
    #                 self.borrarPantalla()
    #                 id=input("Ingrese el ID del coche a actualizar: ").strip()
    #                 cochesito=self.datos_coche("Coche")
    #                 coches1=coches.Coches(cochesito["marca"],cochesito["color"],cochesito["modelo"],cochesito["velocidad"],cochesito["potencia"],cochesito["asientos"])
    #                 respuesta=coches1.actualizar(id)
    #                 self.respuesta_sql(respuesta)
    #                 del coches1
    #             case '4':
    #                 self.borrarPantalla()
    #                 registros=coches.Coches.consultar()
    #                 num_coche=1
    #                 if len(registros) > 0:
    #                     for fila in registros:
    #                         print(f"\n\t Coche #: {num_coche}\n\t\t ID: {fila[0]} \n\t\t Marca: {fila[1]} \n\t\t Color: {fila[2]} \n\t\t Modelo: {fila[3]}\n\t\t Velocidad: {fila[4]} \n\t\t Potencia: {fila[5]} \n\t\t Asientos: {fila[0]}")
    #                         num_coche+=1
    #                         self.espereTecla()
    #                     else:
    #                         print("...No se encontró información en la base de datos!...")
    #                         self.espereTecla()
    #             case '5':
    #                 pass
    #             case _:
    #                 self.opcionInvalida()

    # def main(self):
    #     opcion = True
    #     while opcion:
    #         self.borrarPantalla()
    #         opcion=input("\n\t\t ::: MENÚ PRINCIPAL ::: \n\t 1. Coches\n\t 2. Salir\n\n\t\t Elige una opción: ").lower().strip()
    #         match opcion:
    #             case "1":
    #                 self.borrarPantalla()
    #                 self.menu_acciones("Coches")
    #                 self.espereTecla()
    #             case "2":
    #                 self.borrarPantalla()
    #                 self.terminarSistema()
    #                 opcion=False
    #             case _:
    #                 self.opcionInvalida()


if __name__ == "__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()