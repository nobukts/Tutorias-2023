nro_original = int(input("Ingrese un número: "))
nro_aux = nro_original
esBonito = True

while nro_aux != 0:
    digito = nro_aux%10
    if digito != 0:
        if nro_original % digito != 0:
            esBonito = False
    nro_aux = nro_aux // 10

if esBonito == True:
    print(f"El número {nro_original} es BONITO")
else:
    print(f"El número {nro_original} es FEO")