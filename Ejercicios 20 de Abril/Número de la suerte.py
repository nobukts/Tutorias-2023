"""
Un número de la suerte es aquello que esta compuesto si y solo si por dígitos 4 o 7.
Por ejemplo:

444, 777, 474 son números de la suerte
123, 421, 471 no son números de la suerte

Se le pide realizar un programa en Python que lea primero una línea correspondiente a la cantidad de casos a procesar. Valide
que el número de casos se encuentra en 1 y 200.
Luego del número de casos, lea los números tanto enteros positivos como negativos e indique si es un número de la suerte o no.

"""

cant_casos = int(input("Ingrese la cantidad de casos a analizar: "))

while cant_casos < 1 or cant_casos > 200:
    cant_casos = int(input("Vuelva a ingresar el valor: "))

for i in range(cant_casos):
    nro = int(input("Ingrese un número entero: "))
    nro_aux = nro
    esDeLaSuerte = True
    while nro != 0:
        digito = nro%10
        if digito != 4 and digito != 7:
            esDeLaSuerte = False
        nro //= 10
    if esDeLaSuerte:
        print(f"El número {nro_aux} es de la suerte")
    else:
        print(f"El número {nro_aux} no es de la suerte.")