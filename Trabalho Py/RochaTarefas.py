from funcoe_projeto import menuInicial,menuAlterarTarefa,menuListagem,listarTodasTarefas,abrirTarefa,listarPorPrioridade
from funcoe_projeto import cadastroTarefa,lista_tarefas,tarefa
from funcoe_projeto import novaPrioridade,ListarPorCategoria,MarcarOuDesmarcarTarefa
import random   
opcao = 0

while opcao != 6:
    opcao = menuInicial()
    match  opcao:
        case 1:
            novatarefa = cadastroTarefa()
            lista_tarefas.append(novatarefa)
            
        case 2 :
            busca = input("Digite a tarefa que deseja alterar: ")
            for i in lista_tarefas:
                print(i["Nome"])
                if busca  == i["Nome"]:
                    alterar = 0
                    
                    alterar = menuAlterarTarefa()
                    match alterar:
                        case 1:
                            i["Nome"] = input("Digite o novo nome: ")
                        case 2:
                            i["Descrição"] = input("Digite a nova descrição")
                        case 3:
                            novaPrioridade(i)
                        case 4:
                            i["Categoria"] = input("Digite a nova categoria: ")
                        case _:
                            print("Opção invalida")
        case 3:
            print("-"*30)
            busca = input("Digite a tarefa que deseja excluir: ")
            for i in lista_tarefas:
                if busca == i["Nome"]:
                    del lista_tarefas[lista_tarefas.index(i)]
                    print("Tarefa excluida com sucesso")
                    break
            else:
                print("Tarefa não encontrada")
        case 4:
            opcaoListagem = menuListagem()
            match opcaoListagem:
                case 1:
                    retorno = listarTodasTarefas()
                    if retorno == True:
                        abrirTarefa()
                case 2: 
                    listarPorPrioridade()
                case 3:
                    ListarPorCategoria()
                case _:
                    print("Opção invalida!")
        case 5:
            MarcarOuDesmarcarTarefa()
        case 6:
            print("Saindo do programa...")
        case _:
            print("Opção Invalida")

                    
                    
                    
            
