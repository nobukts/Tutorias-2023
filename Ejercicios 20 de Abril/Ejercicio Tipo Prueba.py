cant_conductores = int(input())

while cant_conductores <= 0 or cant_conductores > 1000:
    cant_conductores = int(input())

cont_inf_1 = 0
cont_inf_2 = 0
cont_eb_1 = 0
cont_eb_2 = 0
cont_inf_rein = 0
cont_inf_susp = 0

print("TOTAL INFRACTORES LEY TOLERANCIA")
print("--------------------------------")

for i in range(cant_conductores):
    suspension_licencia = 0
    multa = 0
    pena_libertad = 0
    yaContabilizado = True
    rut = input()
    grado = float(input())
    reincidencia = int(input())
    tipo_lesion = int(input())
    print(f"Rut infractor : {rut}")
    print("Estado etílico : ", end="")
    if grado >= 0.3 and grado < 0.8:
        print("Bajo la influenza del alcohol")
        cont_inf_1 += 1
        cont_inf_2 += grado

        if tipo_lesion == 1:
            suspension_licencia = "3 meses"
            multa = "5 UTM"
            pena_libertad = "0 dias"
        elif tipo_lesion == 2:
            suspension_licencia = "6 meses"
            multa = "5 UTM"
            pena_libertad = "0 dias"
        elif tipo_lesion == 3:
            suspension_licencia = "9 meses"
            multa = "10 UTM"
            pena_libertad = "20 dias"
        elif tipo_lesion == 4:
            cont_inf_susp += 1
            yaContabilizado = False
            suspension_licencia = "3 años"
            multa = "20 UTM"
            pena_libertad = "541 dias"
        elif tipo_lesion == 5:
            cont_inf_susp += 1
            yaContabilizado = False
            suspension_licencia = "5 años"
            multa = "30 UTM"
            pena_libertad = "5 años"
        elif tipo_lesion == 6:
            cont_inf_susp += 1
            yaContabilizado = False
            suspension_licencia = "5 años"
            multa = "5 UTM"
            pena_libertad = "5 años"

        if reincidencia > 1:
            if yaContabilizado: 
                cont_inf_susp += 1
            suspension_licencia = "72 meses"
            cont_inf_rein += 1
    else:
        print("En estado de ebriedad")
        cont_eb_1 += 1
        cont_eb_2 += grado

    print(f"N° reincidencia : {reincidencia}")
    print(f"Tipo lesión o daño Causado: {tipo_lesion}")

    if grado >= 0.3 and grado < 0.8:
        print(f"Tiempo máximo de suspensión licencia : {suspension_licencia}")
        print(f"Multa máxima : {multa}")
        print(f"Pena máxima : {pena_libertad}")
    
    print("--------------------------------")

print("\nREPORTE FINAL")
print("=============")
promedio_inf = round(cont_inf_1/cant_conductores, 1)
promedio_eb = round(cont_eb_1/cant_conductores, 1)
print(f"Promedio de conductores bajo la influenza del alchohol: {promedio_inf}")
if promedio_inf > 0:
    print(f"Promedio de grados de alcohol por litro de sangre: {round(cont_inf_2/cont_inf_1, 2)}")

print(f"Promedio de conductores ebrios: {promedio_eb}")
if promedio_eb > 0:
    print(f"Promedio de grados de alcohol por litro de sangre: {round(cont_eb_2/cont_eb_1, 2)}")

print(f"Cantidad de conductores bajo la influenza del alcohol reincidentes: {cont_inf_rein}")
print(f"Cantidad de licencias suspendidas superior a 3 años: {cont_inf_susp}")