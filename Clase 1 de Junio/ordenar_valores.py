import random as r

def poblar():
    lista = []
    for i in range(10):
        lista += r.randint(1,100)
    return lista

lista = poblar()

print(sorted(lista))