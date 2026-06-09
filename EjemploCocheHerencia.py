# Herencia: extendiendo la clase

from EjemploCoche import Coche

class CocheElectrico(Coche):
    # El método __init__() para crear una clase hija
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo, tipo)
        self.tamanio_bateria = 100
        self.nivel_carga = 0

    # Agregar un nuevo método a la clase
    def cargar(self):
        self.nivel_carga = 100
        print('El coche está cargado.')

    # Sobrescribir un método del padre
    def gasolina_completo(self):
        print('El coche no tiene depósito de gasolina!')

# Usar el método padre e hijo
obj_coche_electrico = CocheElectrico('TESLA', 'Modelo 3', 'Berlina')
print(obj_coche_electrico.marca, obj_coche_electrico.modelo,
    obj_coche_electrico.tipo)
obj_coche_electrico.cargar()
obj_coche_electrico.conducir()


# Usar el método sobreescrito
obj_coche_electrico.gasolina_completo()

print(isinstance(obj_coche_electrico, CocheElectrico))
print(issubclass(CocheElectrico, Coche))