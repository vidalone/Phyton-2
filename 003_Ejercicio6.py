# *****************************************************************
# *                                                               *
# *   Ejercicio 6: Par, impar y múltiplo de 4.                    *
# *                                                               *
# *****************************************************************

entrada = input("Ingrese un número: ")

try:
    numero = int(entrada)
except ValueError:
    print("Entrada inválida. Ingrese un número entero.")
else:
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")

if (numero % 4) == 0:
    print("El número es múltiplo de 4.")