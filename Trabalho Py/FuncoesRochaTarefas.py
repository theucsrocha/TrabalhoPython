import random
lista_tarefas = []
tarefa = {
    "Nome":"",
    "Descrição":"",
    "Prioridade":"",
    "Categoria":""
    
    }
mensagens_motivacionais = (
    "Mantenha o foco!",
    "Você consegue!",
    "Cada passo conta!",
    "Acredite em si mesmo!",
    "Não desista!"
)
def menuInicial():
    print("-"*30)
    print("*ROCHA TAREFAS📋*")
    print("-"*30)
    print(f"{random.choice(mensagens_motivacionais)}💪")
    print("-"*30)
    print("Selecione a opção desejada:")
    print("-"*30)
    print("1 - Cadastrar Tarefa")
    print("2 - Alterar Tarefa")
    print("3 - Excluir Tarefa")
    print("4 - Listar Tarefas")
    print("5 - Marcar Tarefa")
    print("6 - Sair")
    print("-"*30)
    opcao = int(input("Digite a opção desejada: "))
    
    return opcao

def cadastroTarefa():
    print("-"*30)
    tarefa = {  # Cria um novo dicionário vazio
        "Nome": input("Digite o Nome da tarefa(Obs: Não é recomendado por tarefas com nomes iguais): "),
        "Descrição": input("Digite a Descrição da tarefa: "),
        "Prioridade": "",
        "Categoria": input("Digite a Categoria da tarefa: "),
        "Estado":False
    }
    print("-"*30)
    print("Selecione a prioridade")
    print("1 - Alta")
    print("2 - Media")
    print("3 - Baixa")
    print("-"*30)
    opcaoPrioridade = int(input("Digite a opção:"))
    while(opcaoPrioridade != 1 and opcaoPrioridade != 2 and opcaoPrioridade != 3):
        opcaoPrioridade = int(input("Opção invalida,digite novamente:"))
    match opcaoPrioridade:
        case 1:
            tarefa["Prioridade"] = "Alta"
        case 2:
            tarefa["Prioridade"] = "Media"
        case 3:
            tarefa["Prioridade"] = "Baixa"
        
    

    return  tarefa
def  menuAlterarTarefa():
    print("-"*30)
    print("1 - Nome")
    print("2 - Descrição")
    print("3 - Prioridade")
    print("4 - Categoria")
    print("-"*30)
    
    opcaoAlterar = int(input("Digite a opção:"))
    return opcaoAlterar
def menuListagem():
       print("-"*30)
       print("1 - Todas as tarefas")
       print("2 - Por prioridade")
       print("3 - Por categoria")
       print("-"*30)
       opcao = int(input("Digite a opção: "))
       return opcao
def listarTodasTarefas():
    print("-"*30)
    if len(lista_tarefas) == 0:
           print("Sem Tarefas")
           return False
    else:
        for dicionario in lista_tarefas:
            if dicionario["Estado"] == False:
                print(f"[ ] {dicionario["Nome"]}")
            elif dicionario["Estado"]== True:
                print(f"[✔️] {dicionario["Nome"]}")
        else:
            return True


def abrirTarefa():
    print("-"*30)
    opcaoAbrir = input("Deseja abrir alguma tarefa?(S/N)").upper()
    if opcaoAbrir == "S":
        busca = input("Qual: ")
        for i in lista_tarefas:
            if busca == i["Nome"]:
                print("-"*30)
                for chave, valor in i.items():
                        if(chave != "Estado"):
                            print(f"{chave}: {valor}")
                break
        else:
            print("Tarefa não encontrada")
def listarPorPrioridade():
    print("-"*30)
    print("1 - Alta")
    print("2 - Media")
    print("3 - Baixa")
    opcaoListarPrioridade = int(input("Digite sua opção: "))
    match opcaoListarPrioridade:
        case 1:
            for i in lista_tarefas:
                if i["Prioridade"] == "Alta":
                    if i["Estado"] == False:
                        print(f"[ ] {i["Nome"]}")
                    elif i["Estado"]== True:
                        print(f"[✔️] {i["Nome"]}")
        case 2:
            for i in lista_tarefas:
                if i["Prioridade"] ==  "Media":
                    if i["Estado"] == False:
                        print(f"[ ] {i["Nome"]}")
                    elif i["Estado"]== True:
                        print(f"[✔️] {i["Nome"]}")
        case 3:
            for i in lista_tarefas:
                if i["Prioridade"] == "Baixa":
                    if i["Estado"] == False:
                        print(f"[ ] {i["Nome"]}")
                    elif i["Estado"]== True:
                        print(f"[✔️] {i["Nome"]}")
        case _:
            print("Opção invalida")

def novaPrioridade(tarefa):
    print("-"*30)
    print("Selecione a prioridade")
    print("1 - Alta")
    print("2 - Media")
    print("3 - Baixa")
    opcaoPrioridade = int(input("Digite a opção:"))
    while(opcaoPrioridade != 1 and opcaoPrioridade != 2 and opcaoPrioridade != 3):
         opcaoPrioridade = int(input("Opção invalida,digite novamente:"))
    match opcaoPrioridade:
        case 1:
            tarefa["Prioridade"] = "Alta"
        case 2:
            tarefa["Prioridade"] = "Media"
        case 3:
            tarefa["Prioridade"] = "Baixa"
def ListarPorCategoria():
    print("-"*30)
    busca = input("Digite a categoria que deseja filtrar.(Observação: Sera filtrado apenas as tarefas cujo a categoria estaja escrita exatamente como o usuário informar!):")
    for dicionario in lista_tarefas:
        if busca == dicionario["Categoria"]:
            if dicionario["Estado"] == False:
                print(f"[ ] {dicionario["Nome"]}")
            elif dicionario["Estado"]== True:
                print(f"[✔️] {dicionario["Nome"]}") 
def MarcarOuDesmarcarTarefa():
    print("-"*30)
    busca = input("Digite o nome da tarefa:")
    for dicionario in lista_tarefas:
        if busca == dicionario["Nome"]:
            dicionario["Estado"] = True
            break
    else:
        print("Tarefa Inexistente")