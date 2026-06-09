# *****************************************************************
# *                                                               *
# *   Ejercicio 7: Lista con primero/último y máximo/mínimo       *
# *                                                               *
# *****************************************************************

# Solicitar números al usuario
numeros = []
cantidad = 0

print("Ingrese entre 5 y 10 números:")

while cantidad < 5 or cantidad > 10:
    try:
        entrada = input(f"¿Cuántos números desea ingresar? (5-10): ")
        cantidad = int(entrada)
        
        if cantidad < 5 or cantidad > 10:
            print("Por favor, ingrese un valor entre 5 y 10.")
            continue
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")
        continue
    
    # Recopilar los números
    numeros = []
    for i in range(cantidad):
        while True:
            try:
                num = float(input(f"Ingrese el número {i+1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Entrada inválida. Ingrese un número.")
    
    break

# Crear listas según lo requerido
primero_ultimo = [numeros[0], numeros[-1]]
maximo_minimo = [max(numeros), min(numeros)]

# Mostrar resultados
print("\n" + "="*50)
print("RESULTADOS:")
print("="*50)
print(f"Lista de números ingresados: {numeros}")
print(f"Primero y último: {primero_ultimo}")
print(f"Máximo y mínimo: {maximo_minimo}")
print("="*50)
