"""
Ejemplo de función admitiendo valores.
Como argumento de entrada utiliza *args ya
que se desconoce la cantidad de los mismos
"""

def calcular_media(*args):
    total = 0
    for i in args:
        total += i
    resultado_media = total / len(args)
    return resultado_media

a, b, c = 5, 15, 10
media = calcular_media(a, b, c)

print(f"La media de {a}, {b} y {c} es: {media}")
print("Programa terminado")