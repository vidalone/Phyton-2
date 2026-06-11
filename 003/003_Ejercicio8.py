# *****************************************************************
# *                                                               *
# *   Ejercicio 8: Números impares con for y while               *
# *                                                               *
# *****************************************************************

# ========== VERSIÓN CON BUCLE FOR ==========
print("VERSIÓN CON BUCLE FOR:")
print("-" * 30)

for numero in range(0, 11):
    if numero % 2 != 0:  # Si el número es impar
        print(numero)

print()

# ========== VERSIÓN CON BUCLE WHILE ==========
print("VERSIÓN CON BUCLE WHILE:")
print("-" * 30)

numero = 0
while numero <= 10:
    if numero % 2 != 0:  # Si el número es impar
        print(numero)
    numero += 1
