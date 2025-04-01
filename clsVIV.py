# Construir todo el procesamiento de los datos de los clientes
import clsConection as CON

def AgregarVivienda(Vivi):
    Vivienda = dict(Vivi)

    try:
        db = CON.conectar()
        miCursor = db.cursor()

        columnas = tuple(Vivienda.keys())
        valores = tuple(Vivienda.values())

        Consulta = "INSERT INTO Vivienda{campos} VALUES(?,?,?,?,?,?,?)".format(campos=columnas)

        miCursor.execute(Consulta,valores)
        db.commit()
        Creada = miCursor.rowcount>0
        if Creada:
            return {"Respuesta":True,"Mensaje":"Vivienda creada con éxtio"}
        else:
            return {"Respuesta":False,"Mensaje":"Vivienda no guardada"}

    except Exception as ex:
        return {"Respuesta":False,"Mensaje":str(ex)}

def EliminarVivienda(IDVivienda):
    ID = IDVivienda

    try:
        db = CON.conectar()
        miCursor = db.cursor()

        Consulta = "DELETE FROM Vivienda WHERE IDVivienda={IDBuscar}".format(IDBuscar=ID)

        miCursor.execute(Consulta)
        db.commit()

        Eliminado = miCursor.rowcount>0
        if Eliminado:
            return {"Respuesta":True,"Mensaje":"Vivienda eliminada con éxtio"}
        else:
            return {"Respuesta":False,"Mensaje":"Vivienda no encontrada en la base de datos"}

    except Exception as ex:
        return {"Respuesta":False,"Mensaje":str(ex)}

def ActualizarVivienda(Vivi, ID):
    Vivienda = dict(Vivi)

    try:
        db = CON.conectar()
        miCursor = db.cursor()

        valoresA = tuple(Vivienda.values())  # Asegúrate de que esto tenga el número correcto de valores
        viviendabuscar = ID

        Consulta = "UPDATE Vivienda SET DNIVivienda=?, Ciudad=?, Direccion=?, ValorAlquiler=?, EspecificacionDelAlquiler=?, Estado=?, CantidadPersonas=? WHERE IDVivienda=?"
        miCursor.execute(Consulta, valoresA + (viviendabuscar,))  # Asegúrate de que esto esté correcto
        db.commit()

        Modificada = miCursor.rowcount > 0
        if Modificada:
            return {"Respuesta": True, "Mensaje": "Vivienda modificada con éxito"}
        else:
            return {"Respuesta": False, "Mensaje": "Vivienda no encontrada en la base de datos"}

    except Exception as ex:
        return {"Respuesta": False, "Mensaje": str(ex)}

def BuscarViviendaID(IDviv):
    db = CON.conectar()
    miCursor = db.cursor()

    IDviviendaB = IDviv
    try:
        ConsultaBuscar = "SELECT * FROM Vivienda WHERE IDVivienda={ID}".format(ID=IDviviendaB)

        # Ejecutamos la accion en la base de datos
        miCursor.execute(ConsultaBuscar)

        # Recojo los valores que la consulta me trae
        Resultado = miCursor.fetchall()

        if Resultado:
            info = Resultado[0]

            Vivienda = {"IDVivienda":info[0],
                        "DNIVivienda":info[1],
                        "Ciudad":info[2],
                        "Direccion":info[3],
                        "ValorAlquiler":info[4],
                        "EspecificacionesDelAlquiler":info[5],
                        "Estado":info[6],
                        "CantidadPersonas":info[7]}
            
            miCursor.close()
            db.close()
            return {"Respuesta":True,
                    "Vivienda":Vivienda,
                    "Mensaje":"vivienda encontrada con éxito"}
        else:
            return {"Respuesta":False,"Mensaje":"La vivienda no existe en la base de datos"}

    except Exception as ex:
        return {"Respuesta":False,"Mensaje":str(ex)}

def ListarVivienda():
    db = CON.conectar()
    miCursor = db.cursor()

    try:
        ConsultaBuscar = "SELECT * FROM Vivienda ORDER BY Estado"
        miCursor.execute(ConsultaBuscar)
        Viviendas = miCursor.fetchall()

        if Viviendas:
            return {"Respuesta":True,"Viviendas":Viviendas}
        else:
            return {"Respuesta":False,"Mensaje":"No existen viviendas en la base de datos"}

    except Exception as ex:
        return {"Respuesta":False,"Mensaje":str(ex)}