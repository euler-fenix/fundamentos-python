alunos = {}

while True:
    print('Cadastro de alunos')
    print('Escolha uma opçao:')
    print('1. Adicionar aluno')
    print('2. Remover aluno')
    print('3. Visualizar todos os alunos')
    print('4. Sair')
    opcao = input('Digite o numero da opçao desejada: ')

    if opcao == '1':
        while True:
            nome = input('Digite o nome do aluno: ')
            if nome:
                break
            else: # caso aperte a tecla enter acidentalmente
                print('Nome vazio. Tente novamente.')
        
        while True:
            matricula = input('Para registrar o aluno digite o numero da matricula: ')
            if matricula:
                break
            else:  # caso aperte a tecla enter acidentalmente
                print('Numero da matricula vazio. Tente novamente.')
        
        alunos[matricula] = nome
        print(f'Aluno {nome} adicionado!\n')

    elif opcao == '2':  # Remover um aluno
        matricula = input('Digite a matricula do aluno a ser removido: ')
        if matricula in alunos:
            nome = alunos.pop(matricula)
            print(f'Aluno {nome} removido com sucesso!\n')
        else:
            print('Nmero da matricula nao encontrado.\n')

    elif opcao == '3': # visualizar todos alunos e matricula
        if alunos:
            print('Alunos matriculados:')
            for matricula, nome in alunos.items():
                print(f'Matrcula: {matricula}, Nome: {nome}')
            print()
        else:
            print('Nenhum aluno registrado.\n')

    elif opcao == '4':
        confirmar = input('Realmente quer finalizar? (s/n): ') #se nao for opcão correta
        if confirmar.lower() == 's':
            print('Programa finalizado.')
            break
        elif confirmar.lower() == 'n':
            print('Continuando o programa..\n')
    else:
        print('Opçao invalida. Tente novamente.\n')

