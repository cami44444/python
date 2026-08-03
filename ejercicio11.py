#1-. Solicitar al usuario su peso en kg. y su su estatura en metros ("m")
#2-. Calcular el IMC utilizando la formula: IMC=PESO/ALTURA 2
#3-. Mostrar los resultados de IMC
#4-. Clasificar el estado de peso de la persona segun la OMS
#Rango de IMC    Clasificacion
# Menor a 18.5   Bajo Peso
# 18.5 a 24.9    Peso Normal
# 25.0 a 29.0    Sobre Peso
# 30.0 o mas     Obesidad

peso=float(input("Ingrese su peso en kg:"))
altura=float (input("Ingrese su altura en m:"))

IMC=peso/(altura*2)

if IMC< 18.5:
    print ("Bajo peso")
elif IMC >= 18.5 and IMC < 25.0:
    print ("Peso normal")
elif IMC >= 25.0 and IMC < 30.0:
    print >= ("Sobre Peso")
elif IMC >= 30.0:
    print ("Obesidad")
print ("El resultado de tu IMC es:", IMC)