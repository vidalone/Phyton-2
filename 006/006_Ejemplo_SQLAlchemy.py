from sqlalchemy import create_engine, text


# Crear base de datos y conectarse a ella
cadena_conexion = create_engine("sqlite:///datos.sqlite", echo=True)

# Crear tabla
# with cadena_conexion.connect() as conexion:
#    conexion.execute(text("CREATE TABLE datos (id INTEGER PRIMARY KEY, nombre VARCHAR (50))"))


# Insertar datos
with cadena_conexion.connect() as conexion:
    conexion.execute(text("INSERT INTO datos (nombre) VALUES (:nombre)"),{"nombre": "Maria"})
    conexion.execute(text("INSERT INTO datos (nombre) VALUES (:nombre)"),[{"nombre": "Juan"}, {"nombre": "Maria"}])
    conexion.commit()

# Mostrar los datos
with cadena_conexion.connect() as conexion:
    for i in conexion.execute(text("SELECT * FROM datos")):
        print(i)

conexion.close()