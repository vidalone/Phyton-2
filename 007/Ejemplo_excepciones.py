
def funcion_excepciones():

    try:
        # Dividir entre cero genera una excepción
        print(10 / 0)
    except ZeroDivisionError:
        print("Error. No se puede dividir por cero.")
    else:
        #La excepción no ha ocurrido
        print("La excepción no ha ocurrido")
    finally:
        # Este bloque se ejecuta cuando todas
        # las excepciones han sido ejecutadas
        print("Finalizadas las excepciones.")


funcion_excepciones()