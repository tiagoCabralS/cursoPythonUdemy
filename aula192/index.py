# Problemas com parâmetros mutaveis

# Ao declarar uma função, caso um parâmetro for mutavel NÃO DECLARAR VALOR PADRÃO e DENTRO DA FUNÇÃO crie o parâmetro

def adiciona_clientes(nome, lista=None): # Utilizar o None para tornar o parâmetro IMUTAVEL
    if lista is None: # Essa checage faz com que para cada vez que a "lista" não for passada 
        lista = [] # se criará uma nova lista
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('Luiz')
adiciona_clientes('Joana', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Helena') # A lista que será utilizada nessa declaração é a mesma que está no momento da declaração da função la em cima
adiciona_clientes('Maria', cliente2)
print(cliente2)
