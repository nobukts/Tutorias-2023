def poblar(n):
    lista = []
    for i in range(n):
        lista += [input()]
    return lista

def compararLista(lista1, lista2):
    lista3 = []
    for i in lista1:
        seEncuentra = True
        for j in lista2:
            if i == j:
                seEncuentra = False
                break
        if seEncuentra: lista3 += [i]

    return lista3

def igualLista(lista1, lista2):
    lista3 = []
    for i in lista1:
        seEncuentra = False
        for j in lista2:
            if i == j:
                seEncuentra = True
                break
        if seEncuentra: lista3 += [i]

    return lista3

n1 = int(input("Cuantas palabras tiene la lista 1: "))
lista1 = poblar(n1)
print(f"La primera lista es: {lista1}")

n2 = int(input("Cuantas palabras tiene la lista 2: "))
lista2 = poblar(n2)
print(f"La segunda lista es: {lista2}")

print(f"Palabras que solo aparecen en la lista 1: {compararLista(lista1,lista2)}")
print(f"Palabras que solo aparecen en la lista 2: {compararLista(lista2,lista1)}")
print(f"Palabras que se encuentran en ambas listas: {igualLista(lista1, lista2)}")
