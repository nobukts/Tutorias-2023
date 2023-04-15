'''
Llamamos suma descendente de un número, a la suma de los números resultantes 
de ir quitando de forma reiterada el dígito más significativo
de dicho número. Si tenemos un número de 6 dígitos, ABCDEF, entonces la suma sera:

ABCDEF + BCDEF + CDEF + DEF + EF + F

Por ejemplo, en la suma descendente del número 4578:

4578 + 578 + 78 + 8 = 5242
'''

nro = input()
potencia = len(nro)
nro = int(nro)
suma = 0

while potencia > 0:
    separacion = nro%(pow(10, potencia))
    suma += separacion
    potencia -= 1

print(suma)