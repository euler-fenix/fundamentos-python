peso=float(input("Digite o peso dos peixes:"))
limite=50 
if peso > limite:
    peso_extra=peso-limite
    taxa_extra=peso_extra*4.00

    print(f"Peso excedido em {peso_extra:.2f}Kg")
    print(f'Valor a ser pago e de {taxa_extra:.2f} reais')
else:
    print('Peso dentro do limite')