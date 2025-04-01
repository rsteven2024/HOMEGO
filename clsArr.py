import clsConection as CON

def AgregarArrendatario(Vivienda):
    Alquiler = dict(Vivienda)
    try:
        db = CON.conectar()
        miCursor = db.cursor()
        columnas = tuple(Alquiler.keys())
        valores = tuple(Alquiler.values())
        Consulta = "INSERT INTO Arrendatario{campos} VALUES(?,?,?,?)".format(campos=columnas)
        miCursor.execute(Consulta, valores)
        db.commit()
        Creada = miCursor.rowcount > 0
        if Creada:
            return {"Respuesta": True, "Mensaje": "Arrendatario creado con éxito"}
        else:
            return {"Respuesta": False, "Mensaje": "Arrendatario no guardado"}
    except Exception as ex:
        return {"Respuesta": False, "Mensaje": str(ex)}

def ActualizarArrendatario(Vivi,ID):
    Vivienda = dict(Vivi)

    try:
        db = CON.conectar()
        miCursor = db.cursor()
        valoresA = tuple(Vivienda.values())
        Arrendatariobuscar =int(ID) 
        print("ID que se va a actualizar:"+ID)

        Consulta = "UPDATE Arrendatario SET DNIArrendatario=?, NombreArr=?, CoreoElectronico=?, Telefono=? WHERE IDArrendaatrio=?{ArrendatarioID}".format(ArrendatarioID=Arrendatariobuscar)

        miCursor.execute(Consulta,valoresA+(ID,))
        db.commit()

        Modificada = miCursor.rowcount>0
        if Modificada:
            return {"Respuesta":True,"Mensaje":"Vivienda modificada con éxtio"}
        else:
            return {"Respuesta":False,"Mensaje":"Vivienda no encontrada en la base de datos"}

    except Exception as ex:
        return {"Respuesta":False,"Mensaje":str(ex)}
    
def EliminarVivienda(IDArrendatario):
    ID = IDArrendatario

    try:
        db = CON.conectar()
        miCursor = db.cursor()

        Consulta = "DELETE FROM Arrendatario WHERE IDArrendaatrio={IDBuscar}".format(IDBuscar=ID)

        miCursor.execute(Consulta)
        db.commit()

        Eliminado = miCursor.rowcount>0
        if Eliminado:
            return {"Respuesta":True,"Mensaje":"Vivienda eliminada con éxtio"}
        else:
            return {"Respuesta":False,"Mensaje":"Vivienda no encontrada en la base de datos"}

    except Exception as ex:
        return {"Respuesta":False,"Mensaje":str(ex)}
    
def ListarArrendatario():
    db = CON.conectar()
    miCursor = db.cursor()

    try:
        ConsultaBuscar = "SELECT * FROM Arrendatario ORDER BY IDArrendaatrio"
        miCursor.execute(ConsultaBuscar)
        ArrendatarioTabla = miCursor.fetchall()

        if ArrendatarioTabla:
            return {"Respuesta":True,"Arrendatario":ArrendatarioTabla}
        else:
            return {"Respuesta":False,"Mensaje":"No existe el arendatario en la base de datos"}

    except Exception as ex:
        return {"Respuesta":False,"Mensaje":str(ex)}