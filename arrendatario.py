from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter as tk
import clsArr as coneccionArrendatario

def botonArrendatario():
    Ventana_Arrendatario = Toplevel()
    Ventana_Arrendatario.title("Arrendatario")
    Ventana_Arrendatario.configure(background="#D5C2C1")
    Ventana_Arrendatario.resizable(1, 0)
    Ventana_Arrendatario.state("zoomed")  # Ventana en pantalla completa

    # cargar imagen de fondo
    imagen =  Image.open("fondo2.jpg")
    imagen = imagen.resize((1920, 1080), Image.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Imagen de fondo con label
    fondo_label = Label(Ventana_Arrendatario,image=imagen_tk)
    fondo_label.image = imagen_tk
    fondo_label.place(relwidth=1, relheight=1) 

    Label(Ventana_Arrendatario, text="Arrendatario:", foreground="#000000", font=("Verdana", 14)).pack(pady=20)
    Label(Ventana_Arrendatario, text="Lista de Arrendatarios:", foreground="#000000",font=("Verdana", 14)).place(x=900,y=190)

    boton_cerrar = ttk.Button(Ventana_Arrendatario, text="Atras", command=Ventana_Arrendatario.destroy)
    boton_cerrar.pack(pady=20)
    boton_cerrar.place(x=300,y=500,width=90,height=40)

    fuenteGen = ("Verdana", 12)

    Label(Ventana_Arrendatario, text="ID Arrendatario:", font=fuenteGen).place(x=20, y=200)
    Label(Ventana_Arrendatario, text="DNI Arrendatario:", font=fuenteGen).place(x=20, y=250)
    Label(Ventana_Arrendatario, text="Nombre Arrendatario:", font=fuenteGen).place(x=20, y=300)
    Label(Ventana_Arrendatario, text="Email:", font=fuenteGen).place(x=20, y=350)
    Label(Ventana_Arrendatario, text="Telefono:", font=fuenteGen).place(x=20, y=400)

    # Variables
    IDArrendatario = StringVar()
    DNIArrendatario = StringVar()
    NomArrendatario = StringVar()
    EmailArrendatario = StringVar()
    TelefonoArrendatario = StringVar()

    # Campos de entrada
    e_IDArrendatario = ttk.Entry(Ventana_Arrendatario, textvariable=IDArrendatario, width=35)
    e_DNIArrendatario = ttk.Entry(Ventana_Arrendatario, textvariable=DNIArrendatario, width=35)
    e_NomArrendatario = ttk.Entry(Ventana_Arrendatario, textvariable=NomArrendatario, width=35)
    e_EmailArrendatario = ttk.Entry(Ventana_Arrendatario, textvariable=EmailArrendatario, width=35)
    e_TelefonoArrendatario = ttk.Entry(Ventana_Arrendatario, textvariable=TelefonoArrendatario, width=35)

    e_IDArrendatario.place(x=300, y=200)
    e_DNIArrendatario.place(x=300, y=250)
    e_NomArrendatario.place(x=300, y=300)
    e_EmailArrendatario.place(x=300, y=350)
    e_TelefonoArrendatario.place(x=300, y=400)

    ############## ICONOS Y BOTONES ##################

    tabla = ttk.Treeview(Ventana_Arrendatario)
    tabla.place(x=800, y=270)

    tabla["columns"] = ("ID", "DNI", "Nombre Arrendatario", "Email", "Telefono")

    tabla.column("#0", width=0, stretch=NO)
    tabla.column("ID", width=50, anchor=CENTER)
    tabla.column("DNI", width=50, anchor=CENTER)
    tabla.column("Nombre Arrendatario", width=140, anchor=CENTER)
    tabla.column("Email", width=50, anchor=CENTER)
    tabla.column("Telefono", width=70, anchor=CENTER)

    tabla.column("ID", width=130, anchor=CENTER)

    tabla.heading("#0", text="")
    tabla.heading("ID", text="ID")
    tabla.heading("DNI", text="DNI")
    tabla.heading("Nombre Arrendatario", text="Nombre Arrendatario")
    tabla.heading("Email", text="Email")
    tabla.heading("Telefono", text="Telefono")

    #Funciones
    def ActualizarArrendatario():
        if DNIArrendatario.get():
            ViviendaA = {
            "ID":IDArrendatario.get(),
            "DNI Arrendatario":DNIArrendatario.get(),
            "Nombre Arrendatario":NomArrendatario.get(),
            "Email Arrendatario":EmailArrendatario.get(),
            "Telefono":TelefonoArrendatario.get(),
            }
            ID = IDArrendatario.get()
            Repuesta= coneccionArrendatario.ActualizarArrendatario(ViviendaA,ID)
            messagebox.showinfo("ACTUALIZACION DE VIVIENDA", Repuesta)
        else:
            messagebox.showwarning("Error en los campos", "Debe diligenciar todos los campos para el registro")
    def AgregarArrendatario():
        if DNIArrendatario.get() and NomArrendatario.get(): 
            Vivienda = {"DNIArrendatario":DNIArrendatario.get(),
                    "NombreArr":NomArrendatario.get(),
                    "CoreoElectronico":EmailArrendatario.get(),
                    "Telefono":TelefonoArrendatario.get()
            }
            Respuesta = coneccionArrendatario.AgregarArrendatario(Vivienda)
            messagebox.showinfo("REGISTRO DE VIVIENDA", Respuesta)
        else:
            messagebox.showwarning("Error en los campos","Debe diligenciar todos los campos para el registro")

    def EliminarArrendatario():
            if IDArrendatario.get():
                ID = IDArrendatario.get()
                Respuesta = coneccionArrendatario.EliminarVivienda(ID)

                messagebox.showinfo("Vivienda encontrada y eliminada", Respuesta)

    #Carga de imagen de los botones
    Guardarimg = PhotoImage(file="guardar.png").subsample(60)
    iconoEliminar = PhotoImage(file="ICONOE.png").subsample(14)
    iconoGuardarA = PhotoImage(file="ICONOA.png").subsample(8)

    btn_Actualizar = ttk.Button(Ventana_Arrendatario, text="ACTUALIZAR VIVIENDA", command=ActualizarArrendatario,width=20,image=iconoGuardarA)
    btn_Actualizar.place(x=80,y=490)

    btn_CrearGuardar = ttk.Button(Ventana_Arrendatario, text="CREAR/GUARDAR VIVIENDA", command=AgregarArrendatario,width=20,image=Guardarimg)
    btn_CrearGuardar.place(x=20, y=490)

    btn_Eliminar = ttk.Button(Ventana_Arrendatario, text="ELIMINAR VIVIENDA", command=EliminarArrendatario,width=20,image=iconoEliminar)
    btn_Eliminar.place(x=155, y=490)

    def Llenartabla():
        tabla.delete(*tabla.get_children())
        Respuesta = coneccionArrendatario.ListarArrendatario()
        print("Datos recibidos:", Respuesta)
        ArrendatarioTabla = Respuesta.get("Arrendatario")
        for fila in ArrendatarioTabla:
            row = list(fila)
            row = tuple(row)
            tabla.insert("", END, text=row[0], values=row)
    Llenartabla()

    Ventana_Arrendatario.mainloop()