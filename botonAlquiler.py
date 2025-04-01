from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
import clsALQ as ALQ
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter as tk


def Ventana_Alquiler():
    Ventana_Alquiler = Toplevel()
    Ventana_Alquiler.title("LISTADO DE ALQUILER")
    Ventana_Alquiler.configure(background="#D5C2C1")
    Ventana_Alquiler.resizable(1, 0)
    Ventana_Alquiler.state("zoomed")

    # cargar imagen de fondo
    imagen =  Image.open("fondo2.jpg")
    imagen = imagen.resize((1920, 1080), Image.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Imagen de fondo con label
    fondo_label = Label(Ventana_Alquiler,image=imagen_tk)
    fondo_label.image = imagen_tk
    fondo_label.place(relwidth=1, relheight=1) 


    Label(Ventana_Alquiler, text="LISTADO DE ALQUILER:", foreground="#000000", font=("Verdana", 14)).pack(pady=20)
    
    boton_cerrar = ttk.Button(Ventana_Alquiler, text="Atras", command=Ventana_Alquiler.destroy)
    boton_cerrar.pack(pady=20)
    boton_cerrar.place(x=300,y=550,height=42,width=90)

    fuenteGen = ("Verdana", 12)

    Label(Ventana_Alquiler, text="ID ALQUILER:", font=fuenteGen).place(x=20, y=200)
    Label(Ventana_Alquiler, text="ID VIVIENDA:", font=fuenteGen).place(x=20, y=250)
    Label(Ventana_Alquiler, text="FECHA INICIO ALQUILER:", font=fuenteGen).place(x=20, y=300)
    Label(Ventana_Alquiler, text="FECHA FIN ALQUILER:", font=fuenteGen).place(x=20, y=350)
    Label(Ventana_Alquiler, text="MONTO ALQUILER:", font=fuenteGen).place(x=20, y=400)
    Label(Ventana_Alquiler, text="ESTADO ALQUILER:", font=fuenteGen).place(x=20, y=450)
    Label(Ventana_Alquiler, text="CANTIDAD PERSONAS:", font=fuenteGen).place(x=20, y=500)

    # Variables
    IDAlquiler = StringVar()
    IDVivienda = StringVar()
    FechaInicioAlquiler = StringVar()
    FechaFinAlquiler = StringVar()
    MontoAlquiler = StringVar()
    EstadoAlquiler = StringVar()
    CantidadPersonas = StringVar()

    # Campos de entrada
    e_IDAlquiler = ttk.Entry(Ventana_Alquiler, textvariable=IDAlquiler, width=35)
    e_IDVivienda = ttk.Entry(Ventana_Alquiler, textvariable=IDVivienda, width=35)
    e_FechaInicioAlquiler = ttk.Entry(Ventana_Alquiler, textvariable=FechaInicioAlquiler, width=35)
    e_FechaFinAlquiler = ttk.Entry(Ventana_Alquiler, textvariable=FechaFinAlquiler, width=35)
    e_MontoAlquiler = ttk.Entry(Ventana_Alquiler, textvariable=MontoAlquiler, width=35)
    e_EstadoAlquiler = ttk.Combobox(Ventana_Alquiler, textvariable=EstadoAlquiler,values=["Disponible","No Disponible"], width=35)
    e_CantidadPersonas = ttk.Entry(Ventana_Alquiler, textvariable=CantidadPersonas, width=35)

    e_IDAlquiler.place(x=300, y=200)
    e_IDVivienda.place(x=300, y=250)
    e_FechaInicioAlquiler.place(x=300, y=300)
    e_FechaFinAlquiler.place(x=300, y=350)
    e_MontoAlquiler.place(x=300, y=400)
    e_EstadoAlquiler.place(x=300, y=450)
    e_CantidadPersonas.place(x=300, y=500)

    iconoGuardarG = PhotoImage(file="ICONOG.png").subsample(2)
    iconoGuardarA = PhotoImage(file="ICONOA.png").subsample(8)
    iconoGuardarB = PhotoImage(file="ICONOB.png").subsample(20)
    iconoGuardarE = PhotoImage(file="ICONOE.png").subsample(16)


    def Limpiar():
        IDAlquiler.set("")
        IDVivienda.set("")
        FechaInicioAlquiler.set("")
        FechaFinAlquiler.set("")
        MontoAlquiler.set("")
        EstadoAlquiler.set("")
        CantidadPersonas.set("")

    def AgregarAlquiler():
        if IDVivienda.get() and FechaInicioAlquiler.get() and FechaFinAlquiler.get():
            Alquiler = {"IDVivienda":IDVivienda.get(),
                    "FechaInicioAlquiler":FechaInicioAlquiler.get(),
                    "FechaFinAlquiler":FechaFinAlquiler.get(),
                    "MontoAlquiler":MontoAlquiler.get(),
                    "EstadoAlquiler":EstadoAlquiler.get(),
                    "CantidadPersonas":CantidadPersonas.get()
            }
            Respuesta = ALQ.AgregarAlquiler(Alquiler)
            messagebox.showinfo("REGISTRO DE ALQUILER", Respuesta)
            Limpiar()
        else:
            messagebox.showwarning("Error en los campos","Debe diligenciar todos los campos para el registro")
            Limpiar()

    def BuscarAlquilerID():
        
        if IDAlquiler.get():
            IDAlq = IDAlquiler.get()

            Respuesta = ALQ.BuscarAlquilerID(IDAlq)

            
            if Respuesta.get("Respuesta"):
                Alquiler = Respuesta.get("Alquiler")
                Mensaje = Respuesta.get("Mensaje")
                IDAlquiler.set(Alquiler.get("IDAlquiler"))
                IDVivienda.set(Alquiler.get("IDVivienda"))
                FechaInicioAlquiler.set(Alquiler.get("FechaInicioAlquler"))
                FechaFinAlquiler.set(Alquiler.get("FechaFinAlquiler"))
                MontoAlquiler.set(Alquiler.get("MontoAlquiler"))
                EstadoAlquiler.set(Alquiler.get("EstadoAlquiler"))
                CantidadPersonas.set(Alquiler.get("CantidadPersonas"))

                messagebox.showinfo("Dato encontrado", Mensaje)
                Limpiar()
        else:
            Limpiar()
            messagebox.showwarning("Error en los campos","* Debe diligenciar el ID del Alquiler que desea buscar")

    def ActualizarAlquiler():

        if IDAlquiler.get() and IDVivienda.get() and FechaInicioAlquiler.get() and FechaFinAlquiler.get() and MontoAlquiler.get() and EstadoAlquiler.get():
            AlquilerA = {
            "IDVivienda":IDVivienda.get(),
            "FechaInicioAlquiler":FechaInicioAlquiler.get(),
            "FechaFinAlquiler":FechaFinAlquiler.get(),
            "MontoAlquiler":MontoAlquiler.get(),
            "EstadoAlquiler":EstadoAlquiler.get(),
            "CantidadPersonas":CantidadPersonas.get()}
            ID = IDAlquiler.get()
            Repuesta= ALQ.ActualizarAlquiler(AlquilerA,ID)
            messagebox.showinfo("ACTUALIZACION DE ALQUILER", Repuesta)
            Limpiar()
        else:
            messagebox.showwarning("Error en los campos", "Debe diligenciar todos los campos para el registro")
            Limpiar()

    def EliminarAlquiler():

        if IDAlquiler.get():
            ID = IDAlquiler.get()
            Respuesta = ALQ.EliminarAlquiler(ID)

            messagebox.showinfo("Alquiler encontrado y eliminado", Respuesta)
            Limpiar()


    btn_CrearGuardar = ttk.Button(Ventana_Alquiler, text="CREAR/GUARDAR ALQUILER", command=AgregarAlquiler,width=20,image=iconoGuardarG)
    btn_Actualizar = ttk.Button(Ventana_Alquiler, text="ACTUALIZAR ALQUILER", command=ActualizarAlquiler,width=20,image=iconoGuardarA)
    btn_Buscar = ttk.Button(Ventana_Alquiler, text="BUSCAR ALQUILER", command=BuscarAlquilerID,width=20,image=iconoGuardarB)
    btn_Eliminar = ttk.Button(Ventana_Alquiler, text="ELIMINAR ALQUILER", command=EliminarAlquiler,width=20,image=iconoGuardarE)

    btn_CrearGuardar.place(x=20, y=540)
    btn_Actualizar.place(x=80, y=540)
    btn_Buscar.place(x=516, y=190)
    btn_Eliminar.place(x=135, y=540)


    fuenteLIS = ("Verdana",17)
    Label(Ventana_Alquiler,text="LISTADO DE ALQUILERES REGISTRADOS", justify="center",font=fuenteLIS,foreground="#000000").place(x=770,y=190)

    tabla = ttk.Treeview(Ventana_Alquiler)
    tabla.place(x=630,y=250,width=800)

    tabla["columns"] = ("IDALQUILER","IDVIVIENDA","FECHA-INICIO-ALQUILER","FECHA-FIN-ALQUILER","MONTO-ALQUILER","ESTADO-ALQUILER")

    tabla.column("#0",width=0,stretch=NO)
    tabla.column("IDALQUILER",width=35,anchor=CENTER)
    tabla.column("IDVIVIENDA",width=35,anchor=CENTER)
    tabla.column("FECHA-INICIO-ALQUILER",width=90,anchor=CENTER)
    tabla.column("FECHA-FIN-ALQUILER",width=90,anchor=CENTER)
    tabla.column("MONTO-ALQUILER",width=70,anchor=CENTER)
    tabla.column("ESTADO-ALQUILER",width=70,anchor=CENTER)

    tabla.heading("#0",text="")
    tabla.heading("IDALQUILER",text="IDALQUILER")
    tabla.heading("IDVIVIENDA",text="IDVIVIENDA")
    tabla.heading("FECHA-INICIO-ALQUILER",text="FECHA-INICIO-ALQUILER")
    tabla.heading("FECHA-FIN-ALQUILER",text="FECHA-FIN-ALQUILER")
    tabla.heading("MONTO-ALQUILER",text="MONTO-ALQUILER")
    tabla.heading("ESTADO-ALQUILER",text="ESTADO-ALQUILER")

    def Llenartabla():
        tabla.delete(*tabla.get_children())
        Respuesta = ALQ.ListarAlquiler()
        
        Alquiler = Respuesta.get("Alquiler")
        for fila in Alquiler:
            row = list(fila)
            row = tuple(row)
            tabla.insert("",END,text=id,values=row)
    Llenartabla()
    Ventana_Alquiler.mainloop()