# Fichero coche.py
# Ejemplo de clase
class Coche:
    def __init__(self, marca, modelo, tipo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.capacidad_gasolina = 15
        self.nivel_gasolina = 0

    def gasolina_completo(self):
        self.nivel_gasolina = self.capacidad_gasolina
        print('El depósito de gasolina está lleno')

    def conducir(self):
        print(f'El {self.modelo} se está conduciendo.')

# Creando las instancias de la clase Coche
objeto_coche = Coche('SEAT', 'Ateca', '1.0')

# Acceder a los atributos de ese objeto
print(objeto_coche.marca, objeto_coche.modelo, objeto_coche.tipo)

# Llamando a los métodos de la clase
objeto_coche.gasolina_completo()
objeto_coche.conducir()

# Para verificar si la instancia pertenece a una clase:
print(isinstance(objeto_coche, Coche))