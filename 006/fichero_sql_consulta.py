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