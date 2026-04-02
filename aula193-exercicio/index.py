# Lista de tarefas com opções de desfazer e refazer

def adicionar_tarefa(tarefa, lista=None):
    if lista == None:
        lista = []
    lista.append(tarefa)
    return lista
    
    
def listar(lista):
    for item in lista:
        print(item)
    
    
def desfazer(lista, undones=None):
    if undones == None:
        undones = []
    
    undones.append(lista.pop())
    
    return undones
    

def linha(tam=40):
    print('-'*tam)


tarefas = []
desfeitas = []
while True:
    print('Comandos: listar, desfazer, refazer')
    acao = input('Digite uma tarefa ou comando: ')
    
    if acao == "listar":
        linha()
        listar(tarefas)
    elif acao == "desfazer":
        try:
            linha()
            desfeitas = desfazer(lista=tarefas, undones=desfeitas)
        except IndexError:
            print('Não há nada a ser desfeito!')
    elif acao == "refazer":
        try:
            linha()
            tarefas = desfazer(lista=desfeitas, undones=tarefas)
        except IndexError:
            print('Não há nada a ser refeito!')
    elif acao == "close":
        linha()
        break
    else:
        linha()
        # Adicionar o que foi digitado para a lista
        acao = str(acao)
        tarefas = adicionar_tarefa(acao, tarefas)

print('-'*40)
print(desfeitas)
