# #Este programa realiza o cálculo da média das notas de um aluno e determina sua situação acadêmica com base no resultado. Ele funciona da seguinte forma:
# - Solicita o nome do aluno, garantindo que não contenha números.
# - Permite inserir várias notas, aceitando apenas valores numéricos e encerrando a entrada quando o usuário digita "sair".
# - Calcula a média das notas utilizando função 
# - Verifica a situação do aluno (Aprovado, Reprovado ou Média 10 com destaque) 
# - Exibir o nome do aluno, sua média formatada e sua situação final.


def calcular_media(nota):
    soma=sum(nota)
    provas_realizadas=len(nota)

    media = soma/provas_realizadas  # calculo da media
    return  media

def verifica_situacao(media):  # verifica media e situacao do aluno
    if media < 7 :
        return (f'REPROVADO')

    elif media >= 7 and media < 10:
        return (f'APROVADO !!')

    elif media == 10 :
        return (f"APROVADO 'Parabens' sua media é 10")

def main():
    while True:
        nome = input('Digite o nome do aluno: ')  # Solicita nome do aluno
        if any(char.isdigit() for char in nome):
            print('nome invalido. Tente novamente.')
        else:
            break

    notas = []
    while True:
        nota = input("Digite a nota (ou 'sair' para finalizar): ")
        if nota.lower() == 'sair':
            if notas:
                break
            else:
                print("A nota ainda nao foi digitada.")
                continue
        
        try: # convertendo a entrada
            nota = float(nota)
            notas.append(nota)

        except ValueError:  # para evitar erros str
            print("Digite um valor valido")

    if notas:
        media = calcular_media(notas)
        situacao = verifica_situacao(media)
        print(f'Aluno: {nome}')  #aluno
        print(f'Media: {media:.2f}')  #casa decimai
        print(f'Situacao: {situacao}') #aprovado reprovado
        
if __name__ == "__main__":
    main()
