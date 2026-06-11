def semana (i):
    switcher = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    return switcher.get(i, "Dia inválido")



def semana(i):
    dias={
            0:'Domingo',
            1:'Lunes',
            2:'Martes',
            3:'Miércoles',
            4:'Jueves',
            5:'Viernes',
            6:'Sábado'
        }
    return dias.get(i,"No corresponde a un día de la semana")

print(semana(0))
print('***')
print(semana(10))