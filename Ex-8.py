# 1. Cria uma lista com os nomes das ilhas do grupo central

ilhas = ["Terceira", "São Jorge", "Graciosa", "Pico", "Faial"]

# 2. Cria uma lista com 5 casas, inicializadas a zero

vendas = [0] * 5

# 3. Pede ao utilizador para inserir vendas para cada ilha
total = 0
casa = 0
for ilha in ilhas:
    vendas[casa] = float(input(f"Insira as vendas para {ilha}"))
    casa = casa + 1

for venda in vendas:
    total = total + venda
print(f"O total de vendas é {total}")
print(vendas)

# Média
# Ilha(s) e montante(s) que venderam mais
# Ilha(s) e montante(s) que venderam mais
# Ilha(s) e montante(s) que vendaram mais que a média
# Ilha(s) e montante(s) que venderam menos que a média
