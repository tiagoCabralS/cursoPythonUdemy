# Controlando a quantidade de argumentos posicionais e nomeados em funções
# *argas (ilimitadi de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# Positional-only Parameters (/) - Tudo antes da barra deve ser APENAS POSICIONAL
# Tudo depois do ASTERISCO deve ser NOMEADO
def soma(x, y, /, a, b): # A barra torna os parametros atras dela como não declaraveis por nome. Eles só podem ser usados posicionalmente
    print(x + y + a + b)


soma(1, 2, a=3, b=4)
