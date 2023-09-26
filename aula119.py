# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

def adicionar(list):
    tarefa = input("Digite qual tarefa você deseja adicionar a lista:")
    list.append(tarefa)
    list_cache.clear
    list_cache.append(tarefa)

def remove(list):
    list.pop()

def rework(list):
    list_task.append(list_cache)

def exibir(list):
    print(list_task)
    
list_cache = []
list_task = []

finalizar = 0

while finalizar == 0:
    input_user = input('LISTA DE TASK \n Funções "ADICIONAR", "REMOVER", "LISTAR ou "RETORNAR" \n')

    if input_user == "adicionar":
        adicionar(list_task)
    elif input_user == "remover":
        remove(list_task)
    elif input_user == "listar":
        exibir(list_task)
    elif input_user == "retornar":
        rework(list_task)
    else:
        print("Digite algo válido! \n")
    print(list_task)