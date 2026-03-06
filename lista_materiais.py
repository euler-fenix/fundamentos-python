'''

Defina uma variável do tipo lista (list) com os 
seguintes itens: 'Lápis', 'Borracha', 'Apontador', 'Pacote Folhas A4', 'Lápis', 'Caneta Bic', 'Clips 
de Metal', 'Grampos', 'Post It', 'Suporte p/ Notebook', 'Borracha', 'Lápis', 'Lápis', 'Caneta Bic', 
'Grampos', 'Clips de Metal'. Na sequência, exiba na tela (terminal) a lista conforme o exemplo:

'''


itens = [
    'Lápis',
    'Borracha',
    'Apontador',
    'Pacote Folhas A4',
    'Lápis',
    'Caneta Bic',
    'Clips de Metal',
    'Grampos',
    'Post It',
    'Suporte p/ Notebook',
    'Borracha',
    'Lápis',
    'Lápis',
    'Caneta Bic',
    'Grampos',
    'Clips de Metal'
]
itens_nao_duplicados = []
itens_duplicados = []
lista_final_itens = []

for item in itens:
    if itens.count(item) == 1:
        if item not in itens_nao_duplicados:
            itens_nao_duplicados.append(item)

for item in itens:
    if itens.count(item) > 1:
        if item not in itens_duplicados:
            itens_duplicados.append(item)

lista_final_itens = itens_nao_duplicados[:]
lista_final_itens.extend(itens_duplicados)
lista_final_itens.sort()

print("MATERIAIS DE ESCRITÓRIO 2023", end="\n\n")

for item in lista_final_itens:
    print(f"{itens.count(item)}x {item}")

print()
print(f"Sua lista de compras tem {len(itens)} itens.")


