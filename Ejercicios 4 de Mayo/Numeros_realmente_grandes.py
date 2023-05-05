n = int(input())
s = int(input())
cont = 0

for i in range(1,n + 1):
    suma_i = 0
    i_aux = i
    
    while i != 0:
        digito = i%10
        suma_i += digito
        i //= 10
    
    if i_aux - suma_i >= s:
        cont +=1

print(cont)