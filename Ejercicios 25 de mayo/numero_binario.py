binario = input()
suma = 0
largo = len(binario)

for i in binario:
    suma += (2 ** (largo-1))*int(i)
    largo -= 1

print(suma)