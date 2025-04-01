from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import clsFAC as FAC

def Ventana_Factura():
    ventana_factura = Toplevel()  # Cambia el nombre aquí
    ventana_factura.title("Facturación")
    ventana_factura.configure(background="#D5C2C1")
    ventana_factura.resizable(1, 0)
    ventana_factura.state("zoomed")

    # cargar imagen de fondo
    imagen = Image.open("fondo2.jpg")
    imagen = imagen.resize((1920, 1080), Image.LANCZOS)
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Imagen de fondo con label
    fondo_label = Label(ventana_factura, image=imagen_tk)  # Usa la variable correcta
    fondo_label.image = imagen_tk
    fondo_label.place(relwidth=1, relheight=1)

    # Fuentes
    fuenteGen = ("Verdana", 12)
    fuentesub = ("Verdana", 16)

    # Títulos
    Label(ventana_factura, text="GESTIÓN DE LAS FACTURAS:", foreground="#000000", font=fuenteGen).pack(pady=20)
    Label(ventana_factura, text="..TABLA DE REGISTRO DE LAS FACTURAS..", justify="center", font=fuentesub, foreground="#000000").place(x=830, y=102)

    # Botón Cerrar
    boton_cerrar = ttk.Button(ventana_factura, text="Atras", command=ventana_factura.destroy)
    boton_cerrar.pack(pady=20)
    boton_cerrar.place(x=250, y=650, width=90, height=40)

    # Variables
    IDFactura = StringVar()
    IDAlquiler = StringVar()
    MontoTotal = StringVar()
    CantidadPersonas = StringVar()
    FechaEmision = StringVar()
    FechaVencimiento = StringVar()
    EstadoPago = StringVar()
    MetodoPago = StringVar()
    FechaPago = StringVar()

    # Campos de entrada
    e_IDFactura = ttk.Entry(ventana_factura, textvariable=IDFactura, width=35)
    e_IDAlquiler = ttk.Entry(ventana_factura, textvariable=IDAlquiler, width=35)
    e_MontoTotal = ttk.Entry(ventana_factura, textvariable=MontoTotal, width=35)
    e_CantidadPersonas = ttk.Entry(ventana_factura, textvariable=CantidadPersonas, width=35)
    e_FechaEmision = ttk.Entry(ventana_factura, textvariable=FechaEmision, width=35)
    e_FechaVencimiento = ttk.Entry(ventana_factura, textvariable=FechaVencimiento, width=35)
    e_EstadoPago = ttk.Entry(ventana_factura, textvariable=EstadoPago, width=35)
    e_MetodoPago = ttk.Entry(ventana_factura, textvariable=MetodoPago, width=35)
    e_FechaPago = ttk.Entry(ventana_factura, textvariable=FechaPago, width=35)

    # Posicionamiento de los campos
    e_IDFactura.place(x=250, y=200)
    e_IDAlquiler.place(x=250, y=250)
    e_MontoTotal.place(x=250, y=300)
    e_CantidadPersonas.place(x=250, y=350)
    e_FechaEmision.place(x=250, y=400)
    e_FechaVencimiento.place(x=250, y=450)
    e_EstadoPago.place(x=250, y=500)
    e_MetodoPago.place(x=250, y=550)
    e_FechaPago.place(x=250, y=600)

    # Etiquetas para acompañar los campos de entrada
    Label(ventana_factura, text="ID Factura:", font=fuenteGen).place(x=60, y=200)
    Label(ventana_factura, text="ID Alquiler:", font=fuenteGen).place(x=60, y=250)
    Label(ventana_factura, text="Monto Total:", font=fuenteGen).place(x=60, y=300)
    Label(ventana_factura, text="Cantidad Personas:", font=fuenteGen).place(x=60, y=350)
    Label(ventana_factura, text="Fecha Emisión:", font=fuenteGen).place(x=60, y=400)
    Label(ventana_factura, text="Fecha Vencimiento:", font=fuenteGen).place(x=60, y=450)
    Label(ventana_factura, text="Estado de pago:", font=fuenteGen).place(x=60, y=500)
    Label(ventana_factura, text="Método de pago:", font=fuenteGen).place(x=60, y=550)
    Label(ventana_factura, text="Fecha de pago:", font=fuenteGen).place(x=60, y=600)

    # Funciones
    def Limpiar():
        IDFactura.set("")
        IDAlquiler.set("")
        MontoTotal.set("")
        CantidadPersonas.set("")
        FechaEmision.set("")
        FechaVencimiento.set("")
        EstadoPago.set("")
        MetodoPago.set("")
        FechaPago.set("")

    def AgregarFactura():
        if IDAlquiler.get() and EstadoPago.get():
            Factura = {
                "IDAlquiler": IDAlquiler.get(),
                "MontoTotal": MontoTotal.get(),
                "CantidadPersonas": CantidadPersonas.get(),
                "FechaEmision": FechaEmision.get(),
                "FechaVencimiento": FechaVencimiento.get(),
                "EstadoPago": EstadoPago.get(),
                "MetodoPago": MetodoPago.get(),
                "FechaPago": FechaPago.get()
            }
            Respuesta = FAC.AgregarFactura(Factura)
            messagebox.showinfo("REGISTRO DE FACTURA", Respuesta)
            Limpiar()
        else:
            messagebox.showwarning("Error en los campos", "Debe diligenciar todos los campos para el registro")
            Limpiar()

    def BuscarFacturaID():
        if IDFactura.get():
            IDfact = IDFactura.get()
            Respuesta = FAC.BuscarFacturaID(IDfact)

            if Respuesta.get("Respuesta"):
                Factura = Respuesta.get("Factura")
                Mensaje = Respuesta.get("Mensaje")
                IDFactura.set(Factura.get("IDFactura"))
                IDAlquiler.set(Factura.get("IDAlquiler"))
                MontoTotal.set(Factura.get("MontoTotal"))
                CantidadPersonas.set(Factura.get("CantidadPersonas"))
                FechaEmision.set(Factura.get("FechaEmision"))
                FechaVencimiento.set(Factura.get("FechaVencimiento"))
                EstadoPago.set(Factura.get("EstadoPago"))
                MetodoPago.set(Factura.get("MetodoPago"))
                FechaPago.set(Factura.get("FechaPago"))

                messagebox.showinfo("Dato encontrado", Mensaje)
            else:
                messagebox.showwarning("Error", Respuesta.get("Mensaje"))
        else:
            messagebox.showwarning("Error en los campos", "* Debe diligenciar el ID de la Factura que desea buscar")

    def ActualizarFactura():
        if IDFactura.get() and IDAlquiler.get() and MontoTotal.get() and CantidadPersonas.get() and FechaEmision.get() and FechaVencimiento.get():
            FacturaA = {
                "IDAlquiler": IDAlquiler.get(),
                "MontoTotal": MontoTotal.get(),
                "CantidadPersonas": CantidadPersonas.get(),
                "FechaEmision": FechaEmision.get(),
                "FechaVencimiento": FechaVencimiento.get(),
                "EstadoPago": EstadoPago.get(),
                "MetodoPago": MetodoPago.get(),
                "FechaPago": FechaPago.get()
            }
            ID = IDFactura.get()
            Respuesta = FAC.ActualizarFactura(FacturaA, ID)
            messagebox.showinfo("ACTUALIZACIÓN DE FACTURA", Respuesta)
            Limpiar()
        else:
            messagebox.showwarning("Error en los campos", "Debe diligenciar todos los campos para el registro")
            Limpiar()

    def EliminarFactura():
        if IDFactura.get():
            ID = IDFactura.get()
            Respuesta = FAC.EliminarFactura(ID)
            messagebox.showinfo("Factura encontrada y eliminada", Respuesta)

    # Botones
    iconoGuardarG = PhotoImage(file="ICONOG.png").subsample(2)
    iconoGuardarA = PhotoImage(file="ICONOA.png").subsample(8)
    iconoGuardarB = PhotoImage(file="ICONOB.png").subsample(20)
    iconoGuardarE = PhotoImage(file="ICONOE.png").subsample(16)

    btn_CrearGuardar = ttk.Button(ventana_factura, text="CREAR/GUARDAR FACTURA", command=AgregarFactura, width=20, image=iconoGuardarG)
    btn_Actualizar = ttk.Button(ventana_factura, text="ACTUALIZAR FACTURA", command=ActualizarFactura, width=20, image=iconoGuardarA)
    btn_Buscar = ttk.Button(ventana_factura, text="BUSCAR FACTURA", command=BuscarFacturaID, width=20, image=iconoGuardarB)
    btn_Eliminar = ttk.Button(ventana_factura, text="ELIMINAR FACTURA", command=EliminarFactura, width=20, image=iconoGuardarE)

    btn_CrearGuardar.place(x=20, y=660)
    btn_Actualizar.place(x=80, y=660)
    btn_Buscar.place(x=436, y=189)
    btn_Eliminar.place(x=135, y=660)

    # Tabla de Facturas
    tabla = ttk.Treeview(ventana_factura)
    tabla.place(x=660, y=250)

    tabla["columns"] = ("IDFACTURA", "IDALQUILER", "MONTO-TOTAL", "CANTIDAD-PERSONAS", "FECHA-EMISION", "FECHA-VENCIMIENTO", "ESTADO-PAGO", "METODO-PAGO", "FECHA-PAGO")

    tabla.column("#0", width=0, stretch=NO)
    tabla.column("IDFACTURA", width=50, anchor=CENTER)
    tabla.column("IDALQUILER", width=50, anchor=CENTER)
    tabla.column("MONTO-TOTAL", width=60, anchor=CENTER)
    tabla.column("CANTIDAD-PERSONAS", width=100, anchor=CENTER)
    tabla.column("FECHA-EMISION", width=70, anchor=CENTER)
    tabla.column("FECHA-VENCIMIENTO", width=180, anchor=CENTER)
    tabla.column("ESTADO-PAGO", width=100, anchor=CENTER)
    tabla.column("METODO-PAGO", width=130, anchor=CENTER)
    tabla.column("FECHA-PAGO", width=130, anchor=CENTER)

    tabla.heading("#0", text="")
    tabla.heading("IDFACTURA", text="IDFACTURA")
    tabla.heading("IDALQUILER", text="IDALQUILER")
    tabla.heading("MONTO-TOTAL", text="MONTO-TOTAL")
    tabla.heading("CANTIDAD-PERSONAS", text="CANTIDAD-PERSONAS")
    tabla.heading("FECHA-EMISION", text="FECHA-EMISION")
    tabla.heading("FECHA-VENCIMIENTO", text="FECHA-VENCIMIENTO")
    tabla.heading("ESTADO-PAGO", text="ESTADO-PAGO")
    tabla.heading("METODO-PAGO", text="METODO-PAGO")
    tabla.heading("FECHA-PAGO", text="FECHA-PAGO")

    def Llenartabla():
        tabla.delete(*tabla.get_children())
        Respuesta = FAC.ListarFactura()
        if Respuesta.get("Respuesta"):
            Factura = Respuesta.get("Factura")
            if Factura:
                for fila in Factura:
                    row = list(fila)
                    row = tuple(row)
                    tabla.insert("", END, text=row[0], values=row)
            else:
                messagebox.showwarning("Advertencia", "No existen facturas en la base de datos.")
        else:
            messagebox.showwarning("Advertencia", Respuesta.get("Mensaje"))

    Llenartabla()
    ventana_factura.mainloop() 