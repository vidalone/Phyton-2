import sqlite3

# Establecer la conexión a la base de datos
connection = sqlite3.connect('ejemplo.sqlite')

# Crear el acceso a los datos
cursor = connection.cursor()

# Crear la tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS ejemplo(
                nombre TEXT, ciudad TEXT, telefono INTEGER,
                UNIQUE(nombre, ciudad, telefono))""")

# Ver el esquema de la base de datos
for row in connection.execute("pragma table_info('ejemplo')").fetchall():
    print(row)

# Guardar los cambios y salir
connection.commit()
connection.close()