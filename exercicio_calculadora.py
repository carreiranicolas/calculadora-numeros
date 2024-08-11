""" Calculadora com while """
while True:
    n1 = input('Digite o primeiro número: ')
    n2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(n1)
        num_2_float = float(n2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

   
    if operador == '+':
        soma = num_1_float + num_2_float
        print(f'Resultado da soma: {soma}')
    elif operador == '-':
        menos = num_1_float - num_2_float
        print(f'Resultado da subtração: {menos}')
    elif operador == '*':
        multiplicar = num_1_float * num_2_float
        print(f'Resultado da multiplicação = {multiplicar}')
    elif operador == '/':
        dividir = num_1_float / num_2_float
        print(f'Resultado da divisão: {dividir}')
    else:
        print("Ok, isso não era pra acontecer. Você achou um erro :/")

    ###

    sair = input('Deseja [s]air da calculadora? ').lower().startswith('s')

    if sair is True:
        break