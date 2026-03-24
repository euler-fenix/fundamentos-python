from os import system
from time import sleep

print("TEMPO DE EXECUÇAO DA PROVA")
print("10 minutos")
input("Aperta a tecla enter para iniciar")

numero = 10.00  # contador

while numero >= 0:
    system("cls")
    print(f'{numero:.2f}')  # casas decimais
    numero = numero - 0.02  # subtrai 0.02 a cada repetiçao ate zerar
    sleep(0.001)   # velocidade cronometro

print("TEMPO ESGOTADO")