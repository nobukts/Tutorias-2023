def poblar():
    lista = []
    numero = 1
    while numero >= 0:
        numero = int(input())
        if numero < 0: break
        lista += [numero]

    return lista

def calculoMediana(lista, largo):
    if largo % 2 == 0:
        return (lista[(largo//2) - 1] + lista[(largo//2)])/2
    return lista[(largo//2)]

lista = poblar()

print("Lista de numeros sin ordenar: ", end="")
for i in lista:
    print(i, end=" ")

lista = sorted(lista)

print("\nLista de numeros ordenados: ", end="")
for i in lista:
    print(i, end=" ")

print(f"\nLa mediana de la lista es {calculoMediana(lista, len(lista))}")

