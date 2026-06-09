# ******************************************************************
#    Fichero festivalMusical.py
#    Ejemplo de clase y creación de una instancia de la misma
# ******************************************************************

import datetime
# from datetime import datetime

class FestivalMusical:
        # Inicializa el método __init__ de la clase
        def __init__(self, nombre, pais, estilo_musical):
            # Inicializa los parámetros
            self.nombre = nombre
            self.pais = pais
            self.estilo_musical = estilo_musical

        def festival_metodo(self):
            print('El mejor festival es:', self)
            return self
        
        @classmethod
        def valor_ticket(cls, valor):
            cls.valor_ticket = valor
            return print('El valor del ticket es:', valor)
        
        @staticmethod
        def dia_evento(dia):
            if dia.weekday() == 5 or dia.weekday() == 6:
                print("El evento es en fin de semana.")
            else:
                print("El evento es entre semana.")
            
festival1 = FestivalMusical("Lollapalooza", "Estados Unidos", "Rock")

dia1 = datetime.date.today()

FestivalMusical.valor_ticket(100) # El valor del ticket es: 100

print(FestivalMusical.dia_evento(dia1)) # Salida: El evento es en fin de semana.

print(festival1.nombre)  # Salida: None 

print(FestivalMusical.festival_metodo(festival1.nombre)) # Salida: Lollapalooza

print(FestivalMusical.valor_ticket) # Salida: 100

print(festival1.valor_ticket) # Salida: 100

# print(festival1.__dict__)
# print(FestivalMusical.__dict__)
