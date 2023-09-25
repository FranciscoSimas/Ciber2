# Ordenar lista
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
    vendas = [12, 23, 3, 14, 5, 16 , 57, 8, 19, -3]
    print(ordenar(vendas))
    print(ordenar(vendas, -1))
