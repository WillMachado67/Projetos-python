horario = input('Que horas são? ')

if horario.isnumeric():
    horario = int(horario)

    if horario >= 0 and horario <= 11:
        print('Bom dia!')
    elif horario >= 12 and horario <= 17:
        print('Boa tarde!')
    elif horario >= 18 and horario <= 23:
        print('Boa noite!')
    else:
        print('Horario inserido não esta correto!')
else:
    print('O valor inserido não é um horario.')
