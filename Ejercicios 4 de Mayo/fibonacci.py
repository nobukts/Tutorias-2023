nterms = int(input("Ingrese la cantidad de términos: "))

n1, n2 = 0,1
cont = 0

if nterms <= 0:
    print("No se podra realizar la sucesión por terminos incompatibles.")
elif nterms == 1:
    print("La secuencia seria: ")
    print(n1)
else:
    print("La secuencia seria: ")
    while cont < nterms:
        print(n1, end=" ")
        new_n = n1 + n2
        n1 = n2
        n2 = new_n
        cont += 1

print("")