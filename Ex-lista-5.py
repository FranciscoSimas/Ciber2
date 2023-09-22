# Imprime a lista na ordem inversa
lista = [44, 88, 61, 23, 1, 25, 145, 854, 2, 45, 72, 32]

n = len(lista) - 1
for i in range(len(lista)):
    print(lista[n])
    n = n - 1

