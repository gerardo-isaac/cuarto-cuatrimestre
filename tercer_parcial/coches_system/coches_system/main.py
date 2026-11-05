from coches import cochesBD
from tkinter import Tk, Label, ttk, Entry, Button
from tkinter import messagebox

class App():
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Gestion de Coches")
        self.ventana.geometry("600x600+380+80")
        self.ventana.resizable(0,0)
        self.main() 

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text="::: MENU PRINCIPAL :::").pack(pady=20)
        Button(self.ventana, text="1.- Coches", command=self.menu_acciones).pack(pady=10)
        Button(self.ventana, text="2.- Salir", command=self.ventana.destroy).pack(pady=10)

    def terminarSistema(self):
        input("... ::: ! Gracias por usar nuestro sistema ¡ ::: ...")

    def opcionInvalida(self):
        input("... Opcion invalida oprima cualquier tecla para continuar...")

    def menu_acciones(self):
        self.borrarPantalla()
        tipo="Coches"
        Label(self.ventana,text=f"...::: Menu De {tipo} :::...").pack(pady=10)
        Button(self.ventana, text="1.- Agregar", command=self.insertar_coche_view).pack(pady=10)
        Button(self.ventana, text="2.- Borrar", command=self.eliminar_coche_view).pack(pady=10)
        Button(self.ventana, text="3.- Modificar", command=self.modificar_coche_view).pack(pady=10)
        Button(self.ventana, text="4.- Mostrar", command=self.mostrar_coche_view).pack(pady=10)
        Button(self.ventana, text="5.- Regresar", command=self.main).pack(pady=10)

    def insertar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingrese los datos del Coche").pack(pady=10)

        Label(self.ventana,text="Marca: ").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)

        Label(self.ventana,text="Color: ").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana,text="Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana,text="Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana,text="Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana,text="Asientos: ").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(self.ventana,text=":: Agregar ::", command=self.insertar_coche_controller).pack(pady=5)     
        Button(self.ventana,text=":: Regresar ::", command=self.menu_acciones).pack(pady=5)

    def eliminar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingrese el ID del Coche a Eliminar...").pack(pady=10)

        Label(self.ventana,text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Button(self.ventana,text=":: Eliminar ::", command=self.eliminar_coche_controller).pack(pady=5)     
        Button(self.ventana,text=":: Regresar ::", command=self.menu_acciones).pack(pady=5)

    def modificar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingrese el ID del coche a Modificar...").pack(pady=10)

        Label(self.ventana, text="ID del Coche: ").pack(pady=5)
        self.id = Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Label(self.ventana, text="Nueva Marca: ").pack(pady=5)
        self.marca = Entry(self.ventana)
        self.marca.pack(pady=5)

        Label(self.ventana, text="Nuevo Color: ").pack(pady=5)
        self.color = Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana, text="Nuevo Modelo: ").pack(pady=5)
        self.modelo = Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana, text="Nueva Velocidad: ").pack(pady=5)
        self.velocidad = Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana, text="Nueva Potencia: ").pack(pady=5)
        self.potencia = Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana, text="Nuevos Asientos: ").pack(pady=5)
        self.asientos = Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(self.ventana, text=":: Modificar ::", command=self.modificar_coche_controller).pack(pady=5)     
        Button(self.ventana, text=":: Regresar ::", command=self.menu_acciones).pack(pady=5)

    def mostrar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...::: Listado de Coches :::...").pack(pady=10)
        registros=cochesBD.CochesBD.consultar()

        if len(registros) > 0:
            columnas = ("id", "marca", "color", "modelo", "velocidad", "potencia", "asientos")
            tabla = ttk.Treeview(self.ventana, columns=columnas, show="headings", height=12)

            tabla.heading("id", text="ID")
            tabla.heading("marca", text="Marca")
            tabla.heading("color", text="Color")
            tabla.heading("modelo", text="Modelo")
            tabla.heading("velocidad", text="Velocidad")
            tabla.heading("potencia", text="Potencia")
            tabla.heading("asientos", text="Asientos")

            tabla.column("id", width=40, anchor="center")
            tabla.column("marca", width=80, anchor="center")
            tabla.column("color", width=80, anchor="center")
            tabla.column("modelo", width=80, anchor="center")
            tabla.column("velocidad", width=70, anchor="center")
            tabla.column("potencia", width=70, anchor="center")
            tabla.column("asientos", width=60, anchor="center")

            for fila in registros:
                tabla.insert("", "end", values=fila)
            tabla.pack(pady=10, fill="both", expand=True)
        else:
            Label(self.ventana, text="... No se encontró información en la BD ...").pack(pady=20)

        Button(self.ventana, text=":: Regresar ::", command=self.menu_acciones).pack(pady=10)



    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(title=":: Exitoso ::", message="... ! Accion realizada con exito ¡ ...")
        else:
            messagebox.showerror(title=":: Verifique Porfavor ::", message="... ! Esta accion no pudo realizarse en este momento ¡ ...")

    def insertar_coche_controller(self):
        coches1=cochesBD.CochesBD(self.marca.get(), self.color.get(), self.modelo.get(),
        self.velocidad.get(), self.potencia.get(), self.asientos.get())
        respuesta=coches1.insertar()
        self.respuesta_sql(respuesta)
        del coches1

    def eliminar_coche_controller(self):
        respuesta=cochesBD.CochesBD.eliminar(self.id.get())
        self.respuesta_sql(respuesta)

    def modificar_coche_controller(self):
        coches1 = cochesBD.CochesBD(self.marca.get(), self.color.get(), self.modelo.get(),
        self.velocidad.get(), self.potencia.get(), self.asientos.get())
        respuesta = coches1.actualizar(self.id.get())
        self.respuesta_sql(respuesta)
        del coches1

    def mostrar_coche_controller(self):
        registros = cochesBD.CochesBD.consultar()
        self.mostrar_coche_view(registros)

    # def consultar_coche_view(self):
    #     self.borrarPantalla()
    #     Label(self.ventana,text="..:: Consultar Coches ::..").pack(pady=10)
    #     filas=""
    #     # filas=self.consular_coche_controller(filas)
    #     Label(self.ventana,text=f"{filas}").pack(pady=5)
    #     Button(self.ventana,text=":: Regresar ::", command=self.menu_acciones).pack(pady=5)


if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
