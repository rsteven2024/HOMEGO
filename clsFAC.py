import clsConection as CON

def AgregarFactura(FAC):
    Factura = dict(FAC)

    try:
        db = CON.conectar()
        miCursor = db.cursor()

        columnas = tuple(Factura.keys())
        valores = tuple(Factura.values())

        Consulta = "INSERT INTO Facturacion{campos} VALUES(?,?,?,?,?,?,?,?)".format(campos=columnas)

        miCursor.execute(Consulta,valores)
        db.commit()
        Creada = miCursor.rowcount>0
        if Creada:
            return {"Respuesta":True,"Mensaje":"Factura creada con éxtio"}
        else:
            return {"Respuesta":False,"Mensaje":"Factura no guardada"}

    except Exception as ex:
        return {"Respuesta":False,"Mensaje":str(ex)}
    

def BuscarFacturaID(IDfact):
    db = CON.conectar()
    miCursor = db.cursor()

    IDFacturaB = IDfact

    try:
        
        ConsultaBuscar = "SELECT * FROM Facturacion WHERE IDFactura={ID}".format(ID=IDFacturaB)


        miCursor.execute(ConsultaBuscar)

        Resultado = miCursor.fetchall()

        if Resultado:
            info = Resultado[0]

            Factura = {"IDFactura":info[0],
                        "IDAlquiler":info[1],
                        "MontoTotal":info[2],
                        "CantidadPersonas":info[3],
                        "FechaEmision":info[4],
                        "FechaVencimiento":info[5],
                        "EstadoPago":info[6],
                        "MetodoPago":info[7],
                        "FechaPago":info[8]}
            
            miCursor.close()
            db.close()
            return {"Respuesta":True,
                    "Factura":Factura,
                    "Mensaje":"Factura encontrada con éxito"}
        else:
            return {"Respuesta":False,"Mensaje":"La factura no existe en la base de datos"}

    except Exception as ex:
        return {"Respuesta":False,"Mensaje":str(ex)}
    

def ActualizarFactura(Factu,ID):
    Factura = dict(Factu)

    try:
        db = CON.conectar()
        miCursor = db.cursor()

        valoresA = tuple(Factura.values())
        facturabuscar = ID

        Consulta = "UPDATE Facturacion SET IDFactura=?, IDAlquiler=?, MontoTotal=?, CantidadPersonas=?,FechaEmision=?,FechaVencimiento=?, EstadoPago=?,MetodoPago=?,FechaPago=? WHERE IDFactura=?{IDBuscar}".format(IDBuscar=facturabuscar)

        miCursor.execute(Consulta,valoresA + (facturabuscar,))
        db.commit()

        Modificada = miCursor.rowcount>0
        if Modificada:
            return {"Respuesta":True,"Mensaje":"Factura modificada con éxtio"}
        else:
            return {"Respuesta":False,"Mensaje":"Factura no encontrada en la base de datos"}

    except Exception as ex:
        return {"Respuesta":False,"Mensaje":str(ex)}
    

def EliminarFactura(IDFactura):
    ID = IDFactura

    try:
        db = CON.conectar()
        miCursor = db.cursor()

        Consulta = "DELETE FROM Facturacion WHERE IDFactura={IDBuscar}".format(IDBuscar=ID)

        miCursor.execute(Consulta)
        db.commit()

        Eliminado = miCursor.rowcount>0
        if Eliminado:
            return {"Respuesta":True,"Mensaje":"Factura eliminada con éxtio"}
        else:
            return {"Respuesta":False,"Mensaje":"Factura no encontrada en la base de datos"}

    except Exception as ex:
        return {"Respuesta":False,"Mensaje":str(ex)}
    

def ListarFactura():
    try:
        db = CON.conectar()
        print("Conexión a la base de datos establecida.")
        miCursor = db.cursor()

        ConsultaBuscar = "SELECT * FROM Facturacion ORDER BY IDFactura"
        miCursor.execute(ConsultaBuscar)
        Factura = miCursor.fetchall()
        print("Consulta ejecutada, registros obtenidos:", Factura)

        if Factura:
            return {"Respuesta": True, "Factura": Factura}
        else:
            return {"Respuesta": False, "Mensaje": "No existen facturas en la base de datos"}

    except Exception as ex:
        print("Error en ListarFactura:", str(ex))
        return {"Respuesta": False, "Mensaje": str(ex)}