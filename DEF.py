"""""
Primeiro Programa
"""

def multiplicar(n1, n2):
    resultado = n1 * n2
    return resultado

def imprimir(inf):
    print(inf)

width = 10
height = 20

perimeter = 2*(width+height)
print(f"Perimeter = {perimeter}")

area = multiplicar(width, height)
print(f"Area = {area}")

imprimir(f"Area = {area}")
