import sqlalchemy
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