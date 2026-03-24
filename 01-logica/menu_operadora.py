print(
"""
MENU DIGITAL OPERADORAS

1 - Mudança de Plano
2 - Cobranças
3 - Suporte Técnico
4 - Segunda Via de Contas
5 - Falar com o Atendente
"""
)

opcao = input("Informe uma opção: ")

if opcao == "1":
    print('O seu plano atual é o mais acessivel! Vamos encaminhar as opçoes de upgrade')
elif opcao == "2":
    print('Estamos encaminhando para o setor financeiro ! Aguarde na linha !')
elif opcao == "3":
    print('Aguarde um instante todas as linhas estao ocupadas')
elif opcao == "4":
    print('O seu boleto foi encaminhado para o email cadastrado')
elif opcao == "5":
    print('Voçe é o proximo da linha')
else:
    print("Opção inválida")