codigo_barra = int(input())

while codigo_barra != 0:
    largo = len(str(codigo_barra))

    if largo == 13:
        print("EAN-13", end=" ")
    else:
        print("EAN-8", end=" ")

    dig_ver = codigo_barra%10
    codigo_barra //= 10
    pos = 1
    suma = 0

    while codigo_barra != 0:
        dig = codigo_barra%10
        
        if pos % 2 == 0:
            suma += dig
        else:
            suma += (dig * 3)

        codigo_barra//=10
        pos += 1

    mult = 0

    while mult - suma < 0:
        mult += 10

    dig_ver_nuestro = mult - suma

    if dig_ver == dig_ver_nuestro:
        print("SI")
    else:
        print("NO")
    
    codigo_barra = int(input())