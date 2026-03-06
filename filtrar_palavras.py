# - Possua uma lista contendo várias palavras.
# - Selecione apenas as palavras cujo tamanho seja maior que 5 caracteres.
# - Armazene as palavras filtradas em uma nova lista.
# - Exiba essa lista resultante na tela.
# O código deve utilizar uma função lambda em conjunto com filter para realizar o filtro



palavras = ['gato', 'cachorro', 'elefante', 'leão', 'tigre', 'papagaio']


resultado = list(filter(lambda x: len(x) > 5, palavras))

print(resultado)

