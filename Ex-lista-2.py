"""
Exercicio com Lista 1
"""
# Se o valor do elemento da lista é >= 20,
# então o valor do elemento da lista é o valor do elemento da lista dividido por 2

# Lista
lista = [10, 20, 20, 15, 5, 60, 140, 80, 48]
print("lista original:", lista)

# Inicializa uma lista vazia para a lista modificada
lista_mod = [0] * 9  # O tamanho da lista é conhecido (9 elementos)

# Modifica a lista dividindo por 2 nos números >= 20
pos = 0  # Contador para a posição atual

for n in lista:
    if n >= 20:
        lista_mod[pos] = n / 2
    else:
        lista_mod[pos] = n
    pos += 1
print("lista modificada:", lista_mod)
