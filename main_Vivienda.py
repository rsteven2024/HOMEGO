from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
import clsVIV as VIV
from PIL import Image,ImageTk
import tkinter as tk

def menuVivienda():
    ventana = Toplevel()
    ventana.title("Registro Vivienda")
    ventana.configure(background="#D5C2C1")
    ventana.resizable(1, 0)
    ventana.state("zoomed") 
    # COLOR DE LA VENTANA
    ventana.configure(background="#D5C2C1")
    # cargar imagen de fondo
    imagen =  Image.open("fondo2.jpg")
    imagen = imagen.resize((1920, 1080), Image.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Imagen de fondo con label
    fondo_label = Label(ventana,image=imagen_tk)
    fondo_label.image = imagen_tk
    fondo_label.place(relwidth=1, relheight=1) 


    #-------------------------------------------------------------
    fuente = ("Verdana", 22)
    fuentesub = ("Verdana", 18)
    Label(ventana,text="GESTION DE LAS VIVIENDAS",justify="center",font=fuente,foreground="#000000").place(x=570,y=42)
    Label(ventana,text="..TABLA DE REGISTRO DE LAS VIVIENDAS..",justify="center",font=fuentesub,foreground="#000000").place(x=530,y=102)
    #Label(ventana,text="ID (numero de identificacion): ",justify="center",font=fuentesub,foreground="#FFF0DC").place(x=100,y=200)

    fuenteGen = ("Verdana",12)
    Label(ventana,text="ID VIVIENDA: ",justify="left",font=fuenteGen,foreground="#000000").place(x=20,y=200)
    Label(ventana,text="DNI VIVIENDA: ",justify="left",font=fuenteGen,foreground="#000000").place(x=20,y=250)
    Label(ventana,text="CIUDAD: ",justify="left",font=fuenteGen,foreground="#000000").place(x=20,y=300)
    Label(ventana,text="DIRECCION VIVIENDA: ",justify="left",font=fuenteGen,foreground="#000000").place(x=20,y=350)
    Label(ventana,text="VALOR ALQUILER NOCHE: ",justify="left",font=fuenteGen,foreground="#000000").place(x=20,y=400)
    Label(ventana,text="ESPECIFICACIONES VIVIENDA: ",justify="left",font=fuenteGen,foreground="#000000").place(x=20,y=450)
    Label(ventana,text="ESTADO: ",justify="left",font=fuenteGen,foreground="#000000").place(x=20,y=500)
    Label(ventana,text="CANTIDAD DE PERSONAS: ",justify="left",font=fuenteGen,foreground="#000000").place(x=20,y=550)

    ### INPUT ####
    # SON LOS CAMPOS DONDE EL USUARIO INGRESA EL TEXTO
    idvivienda = StringVar()
    dnivivienda = StringVar()
    ciudad = StringVar()
    direccionvivienda = StringVar()
    valoralquilernoche = StringVar()
    especificacionesvivienda = StringVar()
    estado = StringVar()
    cantidadpersonas = StringVar()

    ### CONSTRUCCION DE LAS CAJAS ###
    e_idvivienda = ttk.Entry(ventana,textvariable=idvivienda,width=35)
    e_dnivivienda = ttk.Entry(ventana,textvariable=dnivivienda,width=35)
    e_ciudad = ttk.Entry(ventana,textvariable=ciudad,width=35)
    e_direccionvivienda = ttk.Entry(ventana,textvariable=direccionvivienda,width=35)
    e_valoralquilernoche = ttk.Entry(ventana,textvariable=valoralquilernoche,width=35)
    e_especificacionesvivienda = ttk.Entry(ventana,textvariable=especificacionesvivienda,width=35)
    e_estado = ttk.Combobox(ventana,textvariable=estado,values=["Disponible","No Disponible"],width=35)
    e_cantidadpersonas = ttk.Entry(ventana,textvariable=cantidadpersonas,width=35)

    e_idvivienda.place(x=300,y=200)
    e_dnivivienda.place(x=300,y=250)
    e_ciudad.place(x=300,y=300)
    e_direccionvivienda.place(x=300,y=350)
    e_valoralquilernoche.place(x=300,y=400)
    e_especificacionesvivienda.place(x=300,y=450)
    e_estado.place(x=300,y=500)
    e_cantidadpersonas.place(x=300,y=550)

    ############## ICONOS ##################
    iconoGuardarG = PhotoImage(file="ICONOG.png").subsample(2)
    iconoGuardarA = PhotoImage(file="ICONOA.png").subsample(8)
    iconoGuardarB = PhotoImage(file="ICONOB.png").subsample(20)
    iconoGuardarE = PhotoImage(file="ICONOE.png").subsample(16)
    ############ BUTTON ################

    def Limpiar():
        idvivienda.set("")
        dnivivienda.set("")
        ciudad.set("")
        direccionvivienda.set("")
        valoralquilernoche.set("")
        especificacionesvivienda.set("")
        estado.set("")
        cantidadpersonas.set("")

    def EliminarVivienda():
        if idvivienda.get():
            ID = idvivienda.get()
            Respuesta = VIV.EliminarVivienda(ID)

            messagebox.showinfo("Vivienda encontrada y eliminada", Respuesta)
            Limpiar()

    def ActualizarVivienda():
        if idvivienda.get() and dnivivienda.get() and direccionvivienda.get() and valoralquilernoche.get() and especificacionesvivienda.get() and estado.get():
            ViviendaA = {
            "DNIVivienda":dnivivienda.get(),
            "Ciudad":ciudad.get(),
            "Direccion":direccionvivienda.get(),
            "ValorAlquiler":valoralquilernoche.get(),
            "EspecificacionesDelAlquiler":especificacionesvivienda.get(),
            "Estado":estado.get(),
            "CantidadPersonas":cantidadpersonas.get()}
            ID = idvivienda.get()
            Repuesta= VIV.ActualizarVivienda(ViviendaA,ID)
            messagebox.showinfo("ACTUALIZACION DE VIVIENDA", Repuesta)
            Limpiar()
        else:
            messagebox.showwarning("Error en los campos", "Debe diligenciar todos los campos para el registro")
            Limpiar()

    def AgregarVivienda():
        if dnivivienda.get() and direccionvivienda.get() and valoralquilernoche.get(): # get = trae el valor que tiene ese objeto que en este caso es lo que tiene dnicliente
            Vivienda = {"DNIVivienda":dnivivienda.get(),
                    "CIUDAD":ciudad.get(),
                    "Direccion":direccionvivienda.get(),
                    "ValorAlquiler":valoralquilernoche.get(),
                    "EspecificacionDelAlquiler":especificacionesvivienda.get(),
                    "Estado":estado.get(),
                    "CantidadPersonas":cantidadpersonas.get()
            }
            Respuesta = VIV.AgregarVivienda(Vivienda)
            messagebox.showinfo("REGISTRO DE VIVIENDA", Respuesta)
            Limpiar()
        else:
            messagebox.showwarning("Error en los campos","Debe diligenciar todos los campos para el registro")
            Limpiar()
        
    def BuscarViviendaID():
        
        if idvivienda.get():
            IDViv = idvivienda.get()

            Respuesta = VIV.BuscarViviendaID(IDViv)

            
            if Respuesta.get("Respuesta"):
                Vivienda = Respuesta.get("Vivienda")
                Mensaje = Respuesta.get("Mensaje")
                idvivienda.set(Vivienda.get("IDVivienda"))
                dnivivienda.set(Vivienda.get("DNIVivienda"))
                ciudad.set(Vivienda.get("Ciudad"))
                direccionvivienda.set(Vivienda.get("Direccion"))
                valoralquilernoche.set(Vivienda.get("ValorAlquiler"))
                especificacionesvivienda.set(Vivienda.get("EspecificacionDelAlquiler"))
                estado.set(Vivienda.get("Estado"))
                cantidadpersonas.set(Vivienda.get("CantidadPersonas"))

                messagebox.showinfo("Dato encontrado", Mensaje)
                Limpiar()
        else:
            Limpiar()
            messagebox.showwarning("Error en los campos","* Debe diligenciar el ID de la vivienda que desea buscar")
        
    btn_CrearGuardar = ttk.Button(ventana, text="CREAR/GUARDAR VIVIENDA", command=AgregarVivienda,width=20,image=iconoGuardarG)
    btn_Actualizar = ttk.Button(ventana, text="ACTUALIZAR VIVIENDA", command=ActualizarVivienda,width=20,image=iconoGuardarA)
    btn_Buscar = ttk.Button(ventana, text="BUSCAR VIVIENDA", command=BuscarViviendaID,width=20,image=iconoGuardarB)
    btn_Eliminar = ttk.Button(ventana, text="ELIMINAR VIVIENDA", command=EliminarVivienda,width=20,image=iconoGuardarE)
    boton_cerrar = ttk.Button(ventana, text="Atras", command=ventana.destroy).place(x=20,y=650,height=42,width=75)

    btn_CrearGuardar.place(x=20, y=590)
    btn_Actualizar.place(x=80, y=590)
    btn_Buscar.place(x=516, y=190)
    btn_Eliminar.place(x=135, y=590)

    ############### LISTA DE CLIENTES ###########
    fuenteLIS = ("Verdana",17)
    Label(ventana,text="LISTADO DE VIVIENDAS REGISTRADAS", justify="center",font=fuenteLIS,foreground="#000000").place(x=770,y=190)

    tabla = ttk.Treeview(ventana)
    tabla.place(x=600,y=250,width=900,height=230)

    tabla["columns"] = ("ID","DNI","CIUDAD","DIRECCION","VALOR","ESPECIFICACIONES","ESTADO","CANTIDAD PERSONAS")

    tabla.column("#0",width=0,stretch=NO)
    tabla.column("ID",width=50,anchor=CENTER)
    tabla.column("DNI",width=50,anchor=CENTER)
    tabla.column("CIUDAD",width=70,anchor=CENTER)
    tabla.column("DIRECCION",width=100,anchor=CENTER)
    tabla.column("VALOR",width=70,anchor=CENTER)
    tabla.column("ESPECIFICACIONES",width=200,anchor=CENTER)
    tabla.column("ESTADO",width=90,anchor=CENTER)
    tabla.column("CANTIDAD PERSONAS",width=105,anchor=CENTER)

    tabla.heading("#0",text="")
    tabla.heading("ID",text="ID")
    tabla.heading("DNI",text="DNI")
    tabla.heading("CIUDAD",text="CIUDAD")
    tabla.heading("DIRECCION",text="DIRECCION")
    tabla.heading("VALOR",text="VALOR")
    tabla.heading("ESPECIFICACIONES",text="ESPECIFICACIONES")
    tabla.heading("ESTADO",text="ESTADO")
    tabla.heading("CANTIDAD PERSONAS",text="CANTIDAD PERSONAS")

    def Llenartabla():
        tabla.delete(*tabla.get_children())
        Respuesta = VIV.ListarVivienda()
        
        Vivienda = Respuesta.get("Viviendas")
        for fila in Vivienda:
            row = list(fila)
            row = tuple(row)
            tabla.insert("",END,text=id,values=row)
    Llenartabla()
    # Siempre tiene que ir al final del codigo de la ventana 
    ventana.mainloop()