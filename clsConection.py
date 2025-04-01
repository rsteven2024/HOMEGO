import sqlite3 as bd

def conectar():
    """Establece y devuelve una conexión a la base de datos SQLite."""
    miConexion = bd.connect("db_HomeGo.db")
    miCursor = miConexion.cursor()

    try:
        ConTableArrendatario = """CREATE TABLE IF NOT EXISTS Arrendatario(
        IDArrendaatrio INTEGER PRIMARY KEY AUTOINCREMENT,
        DNIArrendatario VARCHAR(50) NOT NULL,
        NombreArr VARCHAR (50) NOT NULL,
        CoreoElectronico VARCHAR (50) NOT NULL,
        Telefono VARCHAR (50) NOT NULL,
        CantidadPersonas INTEGER)"""
        miCursor.execute(ConTableArrendatario)
        print("Tabla creada con exito")
        miCursor.close()
        return miConexion
    
    except Exception as ex:
        print("Error!", ex)
        miCursor.close()
        return miConexion


if __name__ == "__main__":
    conectar()