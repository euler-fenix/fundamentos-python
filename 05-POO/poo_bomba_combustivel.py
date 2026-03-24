class BombaCombustivel: 
    def __init__(self, tipo_combustivel, valor_litro, quant_combustivel): 
        self.tipo_combustivel = tipo_combustivel 
        self.valor_litro = valor_litro 
        self.quant_combustivel = quant_combustivel

    #pg por valor / atualiza quantidade bonba
    def abastecer_por_valor(self, valor):  
        quant_litros = valor / self.valor_litro 
        self.quant_combustivel -= quant_litros 
        print(f'Abastecido {quant_litros:.2f} litros de {self.tipo_combustivel}') 
        print(f'Combustivel restante na bomba: {self.quant_combustivel:.2f} litros')

    #pg por litro / atualizando quantidade bonba
    def abastecer_por_litro(self, litros): 
        valor_a_pagar = litros * self.valor_litro 
        self.quant_combustivel -= litros 
        print(f'Valor pago no abastecimento de {litros:.2f} litros de {self.tipo_combustivel}: $ {valor_a_pagar:.2f}') 
        print(f'Combustivel restante na bomba: {self.quant_combustivel:.2f} litros')

    def alterar_valor(self, novo_valor): #alteracao no valor
        self.valor_litro = novo_valor
        print(f'Novo valor litro: R$ {self.valor_litro:.2f}')

    def alterar_combustivel(self, novo_tipo_combustivel): #alterando tipo de combustivel
        self.tipo_combustivel = novo_tipo_combustivel
        print(f'Combustivel alterado p/: {self.tipo_combustivel}')

    #alerando combustivel
    def alterar_quant_combustivel(self, nova_quant):
        self.quant_combustivel = nova_quant
        print(f'quantidade alterada na bomba p/: {self.quant_combustivel:.2f} litros')

def separador():
    print('='*60)

#instancias
bomba = BombaCombustivel(tipo_combustivel='gasolina', valor_litro=6.0, quant_combustivel=4000)
separador()
bomba.abastecer_por_valor(400) 
separador()
bomba.abastecer_por_litro(200)
separador()
bomba.alterar_valor(4.5)
bomba.alterar_combustivel('alcol')
bomba.alterar_quant_combustivel(1000)
separador()