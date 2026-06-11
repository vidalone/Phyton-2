x = input('Introduce el valor de x: ')
x = int(x)

def calculo():
    y = 3*(x**3)-2*(x**2)+3*x-1
    return y

print('El resultado de la ecuación es', calculo())
