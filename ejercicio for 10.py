#Tienes una lista con las notas finales de un grupo de estudiantes
#donde se aprueba con 51 o mas 
#escribe un programa que recorra la lista y determine
    #cuantos estudiantes aprobaron
    #cuantos estudiantes reprobaron
    #la suma de todos los estudiantes aprobados para calcular el promedio
    
notas=[34,60,50,70,80,90]

aprobados=0
reprobados=0
suma_aprobados=0

for i in notas:
    if i>=51:
        aprobados=aprobados+1
        suma_aprobados=suma_aprobados+i
    else:
        reprobados=reprobados+1
promedio=suma_aprobados/aprobados
print("Estudiantes aprobados son: ",aprobados)
print("Estudiantes reprobados son: ",reprobados)
print("El promedio de aprobados es: ",promedio)

