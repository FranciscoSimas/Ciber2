"""
Exercicio com Lista 2
"""
# Lista
lista = [10, 20, 20, 15, 5, 60, 140, 80, 48]

# Inicializar uma lista nova vazia para guardar a contagem [0, 0, 0, 0, 0, ...]
n = [0] * 11

# Contar os elementos em cada intervalo
for num in lista:
    if 0 <= num <= 10:
        n[0] += 1
    elif 11 <= num <= 20:
        n[1] += 1
    elif 21 <= num <= 30:
        n[2] += 1
    elif 31 <= num <= 40:
        n[3] += 1
    elif 41 <= num <= 50:
        n[4] += 1
    elif 51 <= num <= 60:
        n[5] += 1
    elif 61 <= num <= 70:
        n[6] += 1
    elif 71 <= num <= 80:
        n[7] += 1
    elif 81 <= num <= 90:
        n[8] += 1
    elif 91 <= num <= 99:
        n[9] += 1
    else:
        n[10] += 1

# Lista de intervalos
intervalos = ["0 a 10", "11 a 20", "21 a 30", "31 a 40", "41 a 50", "51 a 60", "61 a 70", "71 a 80", "81 a 90",
              "91 a 99", ">100"]

i = 0
for intervalo in intervalos:
    print(f"Elementos de {intervalo}: {n[i]}")
    i += 1

# Resolução prof.

lista = [10, 20, 20, 15, 5, 60, 140, 80, 48]

# Inicializar uma lista nova vazia para guardar a contagem [0, 0, 0, 0, 0, ...]
listamod = [0, 0, 0, 0, 0, 0]  # ou listamod= [0] * 6

# Contar os elementos em cada intervalo
for num in lista:
    if num <= 10:
        listamod[0] += 1
    elif 11 <= num <= 20:
        listamod[1] += 1
    elif 21 <= num <= 30:
        listamod[2] += 1
    elif 31 <= num <= 40:
        listamod[3] += 1
    elif 41 <= num <= 50:
        listamod[4] += 1
    else:
        listamod[5] += 1

print(f"De 0 a 10 = {listamod[0]}")
print(f"De 11 a 20 = {listamod[1]}")
print(f"De 21 a 30 = {listamod[2]}")
print(f"De 31 a 40 = {listamod[3]}")
print(f"De 41 a 50 = {listamod[4]}")
print(f"Maior que 50 = {listamod[5]}")

# Ou usando for:
for x in range(0, len(listamod)):
    print(f"res[{x}] = {listamod[x]}")


# Saber quantos elementos tem a lista
print(f"A lista tem {len(lista)} elementos")
print(f"A lista tem {len(listamod)} elementos")

# Saber a ultima casa da lista
len (lista) - 1
len(listamod) - 1

