def poblar(n):
    lista = []

    for i in range(n-1):
        lista.append(int(input()))
    
    return lista

while True:
    n = int(input())
    if n == 0: break
    while n < 2 or n > 10000:
        n = int(input())
    
    lista = poblar(n)
    suma_piezas = sum(lista)
    suma_total = int((n * (n+1)/2))
    print(f"La pieza perdida: {suma_total-suma_piezas}")

print("---Adios Andres---")

