import botonAlquiler
import botonFactura
import main_Vivienda
import arrendatario
import tkinter as tk
import clsVIV as VIV
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

ventanaMenu = Tk()
ventanaMenu.title("Menu Principal del Sistema")
ventanaMenu.resizable(1, 0)

# Crear ventana full screen
ventanaMenu.state("zoomed")  

# Color de la ventana
ventanaMenu.configure(background="#D5C2C1")

# cargar imagen de fondo
imagen =  Image.open("fondo2.jpg")
imagen = imagen.resize((1920, 1080), Image.LANCZOS)
imagen_tk = ImageTk.PhotoImage(imagen)

# Imagen de fondo con label
fondo_label = tk.Label(image=imagen_tk)
fondo_label.place(relwidth=1, relheight=1) 


############### LISTA DE CLIENTES ###########
fuenteLIS = ("Verdana", 17)
fuenteLIS2 = ("Verdana", 13)

Label(ventanaMenu, text="HOME-GO", justify="center", font=fuenteLIS).place(x=690, y=100)
Label(ventanaMenu, text="Tu hogar, donde y cuando lo necesites.", justify="center", font=fuenteLIS2).place(x=590, y=130)

tabla = ttk.Treeview(ventanaMenu)
tabla.place(x=300, y=200,width=1000,height=200)

tabla["columns"] = ("ID", "DNI", "CIUDAD", "DIRECCION", "VALOR", "ESPECIFICACIONES", "ESTADO", "CANTIDAD PERSONAS")

tabla.column("#0", width=0, stretch=NO)
tabla.column("ID", width=50, anchor=CENTER)
tabla.column("DNI", width=50, anchor=CENTER)
tabla.column("CIUDAD", width=60, anchor=CENTER)
tabla.column("DIRECCION", width=100, anchor=CENTER)
tabla.column("VALOR", width=70, anchor=CENTER)
tabla.column("ESPECIFICACIONES", width=180, anchor=CENTER)
tabla.column("ESTADO", width=75, anchor=CENTER)
tabla.column("CANTIDAD PERSONAS", width=105, anchor=CENTER)

tabla.heading("#0", text="")
tabla.heading("ID", text="ID")
tabla.heading("DNI", text="DNI")
tabla.heading("CIUDAD", text="CIUDAD")
tabla.heading("DIRECCION", text="DIRECCION")
tabla.heading("VALOR", text="VALOR")
tabla.heading("ESPECIFICACIONES", text="ESPECIFICACIONES")
tabla.heading("ESTADO", text="ESTADO")
tabla.heading("CANTIDAD PERSONAS", text="CANTIDAD PERSONAS")

def Llenartabla():
    tabla.delete(*tabla.get_children())
    Respuesta = VIV.ListarVivienda()
    
    Vivienda = Respuesta.get("Viviendas")
    for fila in Vivienda:
        row = list(fila)
        row = tuple(row)
        tabla.insert("", END, text=row[0], values=row)

Llenartabla()

# Botón para abrir la ventana de VIVIENDA
btn_RVivienda = ttk.Button(ventanaMenu, text="Registro Vivienda", command=main_Vivienda.menuVivienda)
btn_RVivienda.place(x=420, y=451, height=42, width=100)

# Botón para abrir la ventana de alquiler
btn_Alquiler = ttk.Button(ventanaMenu, text="Alquiler", command=botonAlquiler.Ventana_Alquiler)
btn_Alquiler.place(x=603, y=451, height=42, width=100)

# Botón para abrir la ventana de facturación
btn_factura = ttk.Button(ventanaMenu, text="Factura", command=botonFactura.Ventana_Factura)
btn_factura.place(x=803, y=451, height=42, width=100)

# Botón para abrir la ventana de arrendatario
btn_arrendatario = ttk.Button(ventanaMenu, text="Arrendatario", command=arrendatario.botonArrendatario)
btn_arrendatario.place(x=1023, y=451, height=42, width=100)

boton_cerrar = ttk.Button(ventanaMenu, text="Cerrar", command=ventanaMenu.destroy).place(x=723,y=541,height=42,width=100)

ventanaMenu.mainloop()