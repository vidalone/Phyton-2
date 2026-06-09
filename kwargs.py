# Ejemplo de función admitiendo pares de valores
# Como argumento de entrada utiliza **kwargs

def test_kwargs(**kwargs):

    for clave, valor in kwargs.items():
        print("{0} = {1}".format(clave, valor))

kwargs = {"tres": 3, "cinco": 5}

test_kwargs(**kwargs)

# ******************************

def crar_lista(n):
    Lista = []
    for i in range(n):
        Lista.append(i)
    return Lista


print(crar_lista(10))