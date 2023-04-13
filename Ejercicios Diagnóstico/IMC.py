edad = int(input("Ingrese su edad: "))
peso = int(input("Ingrese su peso: "))
estatura = float(input("Ingrese su estatura (en metros): "))

imc = peso/estatura

if imc < 22:
    if edad < 45:
        print("RIESGO BAJO")
    else:
        print("RIESGO MIEDO")
else:
    if edad < 45:
        print("RIESGO MEDIO")
    else:
        print("RIESGO ALTO")