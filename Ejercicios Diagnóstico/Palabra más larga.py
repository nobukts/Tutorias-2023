palabra1 = input("Ingrese la palabra 1: ")
palabra2 = input("Ingrese la palabra 2: ")

largo1 = len(palabra1)
largo2 = len(palabra2)

if largo1 > largo2:
    print(f"{palabra1} > {palabra2} por {largo1 - largo2} letras")
elif largo1 < largo2:
    print(f"{palabra2} > {palabra1} por {largo2 - largo1} letras")
else:
    print(f"{palabra1} = {palabra2} con {largo1}")