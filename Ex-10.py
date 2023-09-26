# While (dois ciclos)

semanas = [1, 2, 3, 4]
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

y = 0
while y < len(semanas):
    x = 0
    while x < len(dias):
        print(f"Semana : {semanas[y]} - Dia : {dias[x]}")
        x += 1
    y += 1
    print()
