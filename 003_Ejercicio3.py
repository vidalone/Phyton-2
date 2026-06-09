Dollar = 0.86666146
Euro = 1.15382816
Cambio = 0

Cantidad_Euros = int(input('Introduce la cantidad en euros: '))
Cantidad_Euros = int(Cantidad_Euros)


def calcula_cambio ():
    cambio = Cantidad_Euros * Dollar
    return cambio

print('\nEl valor de', Cantidad_Euros, '€ es de', calcula_cambio(), 'dólares\n')

print('Euro/Dollar', 1/Euro, 'Euros\n')
print('Dollar/Euro', 1/Dollar, 'Dólares\n')