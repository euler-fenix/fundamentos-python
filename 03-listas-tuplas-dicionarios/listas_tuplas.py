# Faça um programa que solicite ao usuário que digite 10 valores para prencher uma lista. 
# Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. 
# Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista, 
# e a soma de todos os números pares e ímpares, respectivamente.


# 10 valores
print('Digita 10 valores conforme for solicitado:')

valores = []
for i in range(10):
    valor = int(input('Digite um valor: '))
    valores.append(valor)

# listas separadas

pares = [num for num in valores if num % 2 == 0]
impares = [num for num in valores if num % 2 != 0]

# colocando os numeros em sequencia
pares_ordenados = sorted(pares)
impares_ordenados = sorted(impares)

# numeros pares e impares em tupla e a quantidade d cada e soma dos numeors pares e impar

print('Numeros pares:', tuple(pares_ordenados)) # tupla
print('Numeros impares:', tuple(impares_ordenados))
print('Quantidade de numeros pares:', len(pares))  # quantidade nueros pares
print('Quantidde de numeros impares:', len(impares))
print('Soma dos numeros pares:', sum(pares))  # soma n pares
print('Soma dos numeros impares:', sum(impares))