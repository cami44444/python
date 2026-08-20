#Escriba un programa en python  que solicite las notas de 3 modulos de un estudiante. Calcule el promedio final
#y determine si el estudiante aprobo (promedio mayor o igual a 61) o reprobo (Promedio menor a 61),
#mostrando el mensaje correspondiente junto con la nota obtenida

nota1 = float(input("Ingrese la nota del modulo 1: "))
nota2 = float(input("Ingrese la nota del modulo 2: "))
nota3 = float(input("Ingrese la nota del modulo 3: "))

result_suma = nota1 + nota2 + nota3

promedio = result_suma / 3

print("El promedio final del alumno es: ", promedio)

if promedio >= 61:
    print("Alumno aprobado con la nota de: ", promedio)
else:
    print("Alumno reprobado con la nota de: ", promedio)