import clsConection as CON

def AgregarAlquiler(ALQ):
    Alquiler = dict(ALQ)

    try:
        db = CON.conectar()
        miCursor = db.cursor()

        columnas = tuple(Alquiler.keys())
        valores = tuple(Alquiler.values())

        Consulta = "INSERT INTO Alquiler{campos} VALUES(?,?,?,?,?,?)".format(campos=columnas)

        miCursor.execute(Consulta,valores)
        db.commit()
        Creada = miCursor.rowcount>0
        if Creada:
            return {"Respuesta":True,"Mensaje":"Alquiler creado con éxtio"}
        else:
            return {"Respuesta":False,"Mensaje":"Alquiler no guardado"}

    except Exception as ex:
        return {"Respuesta":False,"Mensaje":str(ex)}
    
def BuscarAlquilerID(IDAlq):
    db = CON.conectar()
    miCursor = db.cursor()

    IDAlquilerB = IDAlq

    try:
        
        ConsultaBuscar = "SELECT * FROM Alquiler WHERE IDAlquiler={ID}".format(ID=IDAlquilerB)


        miCursor.execute(ConsultaBuscar)

        Resultado = miCursor.fetchall()

        if Resultado:
            info = Resultado[0]

            Alquiler = {"IDAlquiler":info[0],
                        "IDVivienda":info[1],
                        "FechaInicioAlquiler":info[2],
                        "FechaFinAlquiler":info[3],
                        "MontoAlquiler":info[4],
                        "EstadoAlquiler":info[5],
                        "CnatidadPersonas":info[6]}
            
            miCursor.close()
            db.close()
            return {"Respuesta":True,
                    "Alquiler":Alquiler,
                    "Mensaje":"Alquiler encontrado con éxito"}
        else:
            return {"Respuesta":False,"Mensaje":"El alquiler no existe en la base de datos"}

    except Exception as ex:
        return {"Respuesta":False,"Mensaje":str(ex)}
    
def ActualizarAlquiler(ALqui,ID):
    Alquiler = dict(ALqui)

    try:
        db = CON.conectar()
        miCursor = db.cursor()

        valoresA = tuple(Alquiler.values())
        alquilerbuscar = ID

        Consulta = "UPDATE Alquiler SET IDVivienda=?, FechaInicioAlquiler=?, FechaFinAlquiler=?, MontoAlquiler=?, EstadoAlquiler=?, CantidadPersonas=? WHERE IDAlquiler=?{IDBuscar}".format(IDBuscar=alquilerbuscar)

        miCursor.execute(Consulta,valoresA)
        db.commit()

        Modificada = miCursor.rowcount>0
        if Modificada:
            return {"Respuesta":True,"Mensaje":"Alquiler modificado con éxtio"}
        else:
            return {"Respuesta":False,"Mensaje":"Alquiler no encontrado en la base de datos"}

    except Exception as ex:
        return {"Respuesta":False,"Mensaje":str(ex)}
    
def EliminarAlquiler(IDAlquiler):
    ID = IDAlquiler

    try:
        db = CON.conectar()
        miCursor = db.cursor()

        Consulta = "DELETE FROM Alquiler WHERE IDAlquiler={IDBuscar}".format(IDBuscar=ID)

        miCursor.execute(Consulta)
        db.commit()

        Eliminado = miCursor.rowcount>0
        if Eliminado:
            return {"Respuesta":True,"Mensaje":"Alquiler eliminado con éxtio"}
        else:
            return {"Respuesta":False,"Mensaje":"Alquiler no encontrado en la base de datos"}

    except Exception as ex:
        return {"Respuesta":False,"Mensaje":str(ex)}
    
def ListarAlquiler():
    db = CON.conectar()
    miCursor = db.cursor()

    try:
        ConsultaBuscar = "SELECT * FROM Alquiler ORDER BY EstadoAlquiler"
        miCursor.execute(ConsultaBuscar)
        Alquiler = miCursor.fetchall()

        if Alquiler:
            return {"Respuesta":True,"Alquiler":Alquiler}
        else:
            return {"Respuesta":False,"Mensaje":"No existen alquileres en la base de datos"}

    except Exception as ex:
        return {"Respuesta":False,"Mensaje":str(ex)}