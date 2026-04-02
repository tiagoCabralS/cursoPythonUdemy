# Evitando o uso de condicionais

def adicionar_tarefa(tarefa, lista=None):
    if lista == None:
        lista = []
    lista.append(tarefa)
    return lista
    
    
def listar(lista):
    for item in lista:
        print(item)
    
    
def desfazer(lista, undones=None, modo=1):
    try:
        if undones == None:
            undones = []
        
        undones.append(lista.pop())
        
        return undones
    except IndexError:
        if modo == 1:
            opc = 'des'
        elif modo == 2:
            opc = 're'
        print(f'Não há nada a ser {opc}feito!')
    

def linha(tam=40):
    print('-'*tam)


tarefas = []
desfeitas = []
while True:
    print('Comandos: listar, desfazer, refazer')
    acao = input('Digite uma tarefa ou comando: ')
    
    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, desfeitas),
        'refazer': lambda: desfazer(desfeitas, tarefas, 2),
        'adicionar': lambda: adicionar_tarefa(acao, tarefas),
    }
    
    comando = comandos.get(acao) if comandos.get(acao) is not None else comandos['adicionar'] 
    comando()
    
    """if acao == "listar":
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
        tarefas = adicionar_tarefa(acao, tarefas)"""

print('-'*40)
print(desfeitas)
