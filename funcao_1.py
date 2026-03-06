# Crie uma função que receba dois números como parâmetros e verifique se o primeiro número é maior ou igual a 15.
# - Se for maior ou igual, some 15 ao segundo número.
# - Caso contrário, some 40 ao primeiro número.
# A função deve retornar uma mensagem contendo os valores finais de ambos os números.
# Em seguida, chame a função passando dois valores e exiba o resultado no terminal



num1 = 10

num2= 20


def print_message(num1,num2):

    if(num1 >= 15):

        num2 += 15

    else:

        num1 += 40

    return f"numero 1 = {num1}, numero 2 = {num2}"


print(print_message(num1, num2))
