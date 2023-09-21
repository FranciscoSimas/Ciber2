"""
Exercicio com Lista 2
"""

lista = [10, 20, 20, 15, 5, 60, 140, 80, 48]
print(lista)

# Se o valor do elemento da lista é >= 20,
# # então o valor do elemento da lista é o valor do elemento da lista dividido por 2

for n in lista:
    if n >= 20:
        n = n/2
        print(n)