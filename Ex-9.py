# 1. Cria uma lista com os nomes das ilhas do grupo central
ilhas = ["Terceira", "São Jorge", "Graciosa", "Pico", "Faial"]

# 2. Pede valores para cada ilha

# 3. Apresneta: Total
#               Valor minimo e ilhas com esse valor
#               Valor máximo e ilhas com esse valor
#               Ordena de forma crescente
#               Ordena de forma decrescente
vendas = [0] * 5
total = min = max = casa = 0
for ilha in ilhas:
    print(f"insira as vendas para {ilha}")
    vendas[casa] = int(input())
    total += vendas[casa]
    if casa == 0:
        min = vendas[casa]
        max = vendas[casa]
    else:
        if vendas[casa] < min:
            min = vendas[casa]
        if vendas[casa] > max:
            max = vendas[casa]
    casa += 1

print(f"O total de vendas é {total}")
print(f"O valor minimo é [{max}] nas ilhas:")
for casa in range(len(vendas)):
    if vendas[casa] == max:
        print(ilhas[casa])

print(f"O valor máximo é [{min}] nas ilhas:")
for casa in range(len(vendas)):
    if vendas[casa] == min:
        print(ilhas[casa])

# 4. Ordenar lista por ordem crescente e decrescente
def ordenar(vendas, ordem=1):
    troquei = True
    while troquei:
        troquei = False
        x = 0
        while x < len(vendas) - 1:
            if vendas[x] * ordem > vendas[x + 1] * ordem:
                c1 = vendas[x]
                vendas[x] = vendas[x + 1]
                vendas[x + 1] = c1
                troquei = True
            x += 1
    return vendas
if __name__ == '__main__':
    print(ordenar(vendas))
    print(ordenar(vendas, -1))
