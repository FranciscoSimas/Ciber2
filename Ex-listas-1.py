"""
Listas
"""
print("Exercicio1")
# 1. Cire uma lista
lista = [70, 20, 30, 90, 50, 60, 10, 80, 40]

print("Exercicio2")
# 2. Achar o maior numero da lista
maior = lista[0]

for num in lista:
    if num > maior:
        maior = num

print(maior)

print("Exercicio3")
# 3.Soma todos os elementos da lista usando "for"
total = 0
for num in lista:
    total = total + num
    print(total)

print("Exercicio4")
# 4.Soma todos os elementos da lista
total = lista[0] + lista[1] + lista[2] + lista[3] + lista[4]
print(total)

print("Exercicio5")
# 5. Imprime cada secção da lista
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

print("Exercicio6")
# 6. Imprime cada secção da lista usando "for"
for n in lista:
    print(n)
print("Exercicio7")
# 7. Imprima a lista
print(lista)

print("Exercicio8")
# 8. Agora, renova os elementos 3 e 6 (não esqueça de checar se eles estão na lista)
if 30 in lista:
    lista.remove(30)
if 60 in lista:
    lista.remove(60)

print("Exercicio9")
# 9.Imprima a lista modifica
print(lista)
