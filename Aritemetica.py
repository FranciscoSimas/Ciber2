"""
Aritemética
"""

n1 = int(input("Introduza o primeiro número"))
n2 = int(input("Introduza o segundo número"))


def aritemetica(op, n1, n2):
    if op == "+":
        resultado = n1 + n2
    elif op == "-":
        resultado = n1 - n2
    elif op == "*":
        resultado = n1 * n2
    elif op == "/":
        resultado = n1 / n2
    else:
        resultado = "Opereação inválida"
    return resultado


def contas(op, n1, n2):
    if op == "+":
        resultado = n1 + n2
    else:
        if op == "-":
            resultado = n1 - n2
        else:
            if op == "*":
                resultado = n1 * n2
            else:
                if op == "/":
                    resultado = n1 / n2
                else:
                    resultado = "Opereção inválida"
    return resultado


def continhas(op, n1, n2):
    resultado = "Opereção inválida"
    if op == "+":
        resultado = n1 + n2
    if op == "-":
        resultado = n1 - n2
    if op == "*":
        resultado = n1 * n2
    if op == "/":
        resultado = n1 / n2
    print(type(op))
    print(f"O type de op é {type(op)}")
    print(f"O type de 'n1' é {type(n1)}")
    return resultado


print(aritemetica("+", n1, n2))
print(aritemetica("-", n1, n2))
print(aritemetica("*", n1, n2))
print(aritemetica("/", n1, n2))
print(aritemetica("b", n1, n2))

print(contas("+", n1, n2))
print(contas("-", n1, n2))
print(contas("*", n1, n2))
print(contas("/", n1, n2))
print(contas("b", n1, n2))

print(continhas("+", n1, n2))
print(continhas("-", n1, n2))
print(continhas("*", n1, n2))
print(continhas("/", n1, n2))
print(continhas("b", n1, n2))
