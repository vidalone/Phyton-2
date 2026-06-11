import math
import warnings

warnings.filterwarnings("ignore")

try:
    numero = int(input('Escribe un número positivo: '))
    try:
        print(f'La raíz cuadrada de {numero} es {math.sqrt(numero)}')
    except ValueError as ve:
        print(f'{numero} no es un número positivo.')

except ValueError as ve:
    print("Debes escribir un número entero.")