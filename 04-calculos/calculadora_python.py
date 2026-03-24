numero_1 = float(input('Digite o 1º número: '))
numero_2 = float(input('Digite o 2º número: '))
simbolo = input('Digite +, -, / ou *')
resultado = 0
if simbolo == '+':
    resultado = numero_1 + numero_2
    print('A soma é:', resultado)

elif simbolo == '-':
    resultado = numero_1 - numero_2
    print('A subtração é:', resultado)

elif simbolo == '*':
    resultado = numero_1 * numero_2
    print('A multiplicação é:', resultado)

elif simbolo == '/':
    if numero_2 != 0:
        resultado = numero_1 / numero_2
        print('A divisao é:', resultado)
    else:
        print('Erro: divisão por zero')

else:
    print('Símbolo inválido')