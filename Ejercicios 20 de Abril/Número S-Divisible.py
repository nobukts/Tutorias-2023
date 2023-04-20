nro = int(input("Ingrese un número: "))
nro_aux = nro
esDivisble = True

while nro != 0:
    digito = nro%10
    if digito != 0:
        if nro % digito != 0:
            esDivisble = False
            break
    else:
        esDivisble = False
        break
    nro //= 10 

if esDivisble:
    print(f"El número {nro_aux} es S-Divisible")
else:
        print(f"El número {nro_aux} no es S-Divisible")