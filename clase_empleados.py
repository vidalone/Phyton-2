
class Empleados:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Aptitudes(Empleados):
    def __init__(self, nombre, apellido, lenguaje, so, idioma):
        super().__init__(nombre, apellido)
        self.lenguaje = lenguaje
        self.so = so
        self.idioma = idioma
