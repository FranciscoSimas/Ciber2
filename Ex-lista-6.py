lista = [44, 88, 61, 23, 1, 25, 145, 854, 2, 45, 72, 32, 78, 36]

# Imprimir os elementos da lista e dizer se é par ou impar
par = 0
impar = 0
par1 = 0
impar1 = 0

for x in lista:
    if x % 2 == 0:
        print(f"O numero {x} é par")
        par = par + 1

    else:
        print(f"O numero {x} é impar")
        impar = impar + 1

print(f"Existe {par} numeros pares")
print(f"Existe {impar} numeros impares")

# Ou
for x in range(len(lista)):
    if lista[x] % 2 == 0:
        print(f"O numero {lista[x]} é par")
        par1 = par1 + 1
    else:
        print(f"O numero {lista[x]} é impar")
        impar1 = impar1 + 1

print(f"Existe {par1} numeros pares")
print(f"Existe {impar1} numeros impares")
