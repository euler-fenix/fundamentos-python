# Aplica uma função anônima (lambda) sobre uma lista de números 
# usando a função map. A ideia é transformar cada elemento da lista de acordo com uma condição:
# - Se o número for par, calcular o quadrado dele
# - Se o número for ímpar, calcular o cubo

numeros = [1, 2, 3, 4, 5]

resultado = list(map(lambda x: x ** 2 if x % 2 == 0 else x ** 3, numeros))

print(resultado)
