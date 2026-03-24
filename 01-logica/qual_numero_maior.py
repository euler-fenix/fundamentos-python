numero1 = input("Informe um número: ")
numero2 = input("Informe outro número: ")

numero1 = int(numero1)
numero2 = int(numero2)

if numero1 > numero2:
    print(f"O número {numero1} é maior que o {numero2}")
elif numero2 > numero1:
    print(f"O número {numero2} é maior que o {numero1}")
else:
    print('Os números são iguais')
