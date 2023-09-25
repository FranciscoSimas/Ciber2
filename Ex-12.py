# 1. Lista com 6 empresa  **
# 2. Inserir Vendas de cada empresa  **
# 3. Total do valor de vendas das empresas  **
# 4. Apresentar qual a empresa com maior e menor valor de venda e o respetivo valor
# 5. Ordenar a lsita do valor de venda em ordem crescente e decrescente

empresas = ["Google", "Apple", "Samsung", "Lg", "Adidas", "Nike"]
vendas = [0] * 6
total = max = min = 0
x = 0

for empresa in empresas:
    print(f"insira as vendas para {empresa}")
    vendas[x] = int(input())
    total += vendas[x]
    if x == 0:
        min = vendas[x]
        max = vendas[x]
    else:
        if vendas[x] < min:
            min = vendas[x]
        if vendas[x] > max:
            max = vendas[x]
    x += 1

print(f"O valor de vendas total é:{total}")
print(f"O valor minimo é [{max}] nas empresas:")
for x in range(len(vendas)):
    if vendas[x] == max:
        print(empresas[x])

print(f"O valor máximo é [{min}] nas ilhas:")
for x in range(len(vendas)):
    if vendas[x] == min:
        print(empresas[x])