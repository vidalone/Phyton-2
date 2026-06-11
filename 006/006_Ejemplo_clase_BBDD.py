import sqlalchemy

# Fichero para crear DB: fichero_sql_tablas.py

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Métodos para relacionar la tabla
# from sqlalchemy.orm import relationship, ForeignKey

engine = create_engine('sqlite:///estudiantes.db', echo=True)
base = sqlalchemy.orm.declarative_base()

class Estudiante(base):
    __tablename__ = "estudiante"
    id = Column(Integer, primary_key=True)
    usuario = Column(String)
    nombre = Column(String)
    apellido1 = Column(String)
    apellido2 = Column(String)
    universidad = Column(String)

    def __init__(self, usuario, nombre, apellido1, apellido2, universidad):
        self.usuario = usuario
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.universidad = universidad

# crea la tabla
base.metadata.create_all(engine)

# Fichero para inserir datos en la DB: fichero_sql_datos.py
from sqlalchemy.orm import sessionmaker
from fichero_sql_tablas import Estudiante, create_engine

engine = create_engine('sqlite:///estudiantes.db', echo=True)

# crea una sesión
session1 = sessionmaker(bind=engine)
session = session1()

# Crea las instancias
usuario = Estudiante("juan", "Juan", "Perez", "Lopez", "Complutense")
session.add(usuario)

usuario = Estudiante("Maria", "María", "García", "Gomez", "UPC")
session.add(usuario)

usuario = Estudiante("Beatriz", "Beatriz", "Suarez", "Gonzalez", "Carlos III")
session.add(usuario)

# commit a la base de datos
session.commit()
session.close()

# Fichero para consultar datos en la DB: fichero_sql_consulta.py
from sqlalchemy.orm import sessionmaker
from fichero_sql_tablas import Estudiante, create_engine

engine = create_engine('sqlite:///estudiantes.db', echo=True, future=True)

# Crea una sesion
session1 = sessionmaker(bind=engine)
session = session1()

# Consulta a la base de datos
for estudiante1 in session.query(Estudiante).order_by(Estudiante.id):
    print(estudiante1.nombre, estudiante1.apellido1, estudiante1.apellido2)

session.close()


# Ejemplo filtrar base de datos
for estudiante2 in session.query(Estudiante).filter(
        Estudiante.universidad == 'UPC'):
    print(estudiante2.nombre, estudiante2.apellido1, estudiante2.apellido2)