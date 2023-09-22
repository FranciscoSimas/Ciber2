lista = [44, 88, 61, 23, 1, 25, 145, 854, 2, 45, 72, 32]

# Imprime o numero de casas na listas
print(len(lista))

# Imprime a sequencia de numeros entre zero e o numero de casas na lista menos um.
# Usa a variavel "x" para percorrer a lista
for x in range(len(lista)):
    print(x)

# Imprime a sequencia de numeros entre o numero de casas da lista menos um e zero.
# Usa a variavel i
n = len(lista) - 1
for i in range(len(lista)):
    print(n)
    n = n - 1
