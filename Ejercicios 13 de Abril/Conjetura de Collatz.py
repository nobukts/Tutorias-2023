'''
La conjetura de collatz nos indica que a partir de cualquier número
podemos llegar a 1 realizando los siguientes pasos:
- Si el número es par, lo divides en 2
- Si el número es impar, lo multiplicas por 3 y le sumas 1
- Repite este proceso con el resultado obtenido hasta llegar a 1
'''

nro = int(input())

while nro != 1:
    if nro % 2 == 0:
        nro //= 2
    else:
        nro = (nro * 3) + 1

    print(f"{nro} - ", end="")
