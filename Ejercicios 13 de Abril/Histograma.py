'''
Escriba un programa que lea varios valores enteros que 
pueden ser positivos o negativos. CUando se ingrese un cero el programa debe
terminar y mostrar un gráfico de cuantos valores positivos y negativos fueron ingresados
Ejemplo:

5 6 7 -5 0

Positivos: ***
Negativos: *
'''

nro = int(input())
contP = 0
contN = 0

while nro != 0:
    if nro > 0:
        contP += 1
    elif nro < 0:
        contN += 1

    nro = int(input())

print("Positivos: ", end="")
while contP != 0:
    print("*", end="")
    contP -= 1

print("\nNegativos: ", end="")
while contN != 0:
    print("*", end="")
    contN -= 1