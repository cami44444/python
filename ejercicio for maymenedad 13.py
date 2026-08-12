#Un cine tiene una lista con las edades de un grupo de personas que quieren ver una pelicula clasificada para mayores de (18 años o mas)
#1. Crear una lista nueva llamada mayores de edad que guarde unicamente las edades de las personas que tiene 18
#2. Contar de forma manual cuantas personas pueden entrar a la sala
#3. Contar de forma manual cuantas personas no pueden entrar por ser menores de edad


#LISTAS PYTHON

edad=[20,80,10,14,11,21,50]
mayores_de_edad=[]

contar_mayores=0
contar_menores=0

for i in edad:
    if i >=18:
        mayores_de_edad.append(i)
        contar_mayores=contar_mayores+1
    else:
        
        contar_menores=contar_menores+1

print("Lista de edades", edad)
print("Lista de mayores de edad", mayores_de_edad)
print("Cantidad de mayores de edad", contar_mayores)
print("Cantidad de menores de edad", contar_menores)

print("Lista de mayores de edada:")
        