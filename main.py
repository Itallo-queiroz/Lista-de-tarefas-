# Tarefa 
tarefas = []

# Menu
while True:
    print('1 - Inserir lista de Tarefas.')
    print('2 - Exibir lista de Tarefas.')
    print('3 - Exibir em ordem alfabetica.')
    print('4 - sair do programa.')

    # Opções do usuario
    opcao = input('Opção do usuario: ')

    # Verrificar a opção escolhida
    match opcao:
        case '1':
            nova_tarefa = input('Insira uma nova Tarefa: ').capitalize()
            tarefas.append(nova_tarefa)
            print(f'{nova_tarefa} Insirida com sucesso.')
            continue
        case '2':
            print('\nLista de tarefas:\n')
            for tarefa in tarefas:
                print(tarefa)
                continue
        case '3':
            tarefas.sort()
            for tarefa in tarefas:
                print(tarefa)
            print('\nLista ordenada com sucesso.')
            continue
        case '4':
            print('Programa encerrado.')
            break
        case _:
            print('Opção invalida')


