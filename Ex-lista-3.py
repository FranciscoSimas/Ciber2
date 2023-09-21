"""
Exercicio com Lista 2
"""
# Lista
lista = [10, 20, 20, 15, 5, 60, 140, 80, 48]

# Inicializa uma lista para armazenar as contagens em cada intervalo
contagens = [0] * 11

# Conta os elementos em cada intervalo
for num in lista:
    if 0 <= num <= 10:
        contagens[0] += 1
    elif 11 <= num <= 20:
        contagens[1] += 1
    elif 21 <= num <= 30:
        contagens[2] += 1
    elif 31 <= num <= 40:
        contagens[3] += 1
    elif 41 <= num <= 50:
        contagens[4] += 1
    elif 51 <= num <= 60:
        contagens[5] += 1
    elif 61 <= num <= 70:
        contagens[6] += 1
    elif 71 <= num <= 80:
        contagens[7] += 1
    elif 81 <= num <= 90:
        contagens[8] += 1
    elif 91 <= num <= 99:
        contagens[9] += 1
    else:
        contagens[10] += 1

# Lista de intervalos
intervalos = ["0 a 10", "11 a 20", "21 a 30", "31 a 40", "41 a 50", "51 a 60", "61 a 70", "71 a 80", "81 a 90", "91 a 99", ">100"]

# Exibe as contagens para cada intervalo
i = 0
for intervalo in intervalos:
    print(f"Elementos de {intervalo}: {contagens[i]}")
    i += 1
