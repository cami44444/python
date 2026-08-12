#Crear una lista de frutas vacia  y añade la cantidad de frutas que quieres ingresar y luego agregar o ingresa a la lista de frutas
#y por ultimo elimina las frutas ingresadas

frutas=[]
#ingresar  la cantidad de frutas
Cantidad_de_frutas=int (input("Ingresar la cantidad de frutas:"))

for i in range (Cantidad_de_frutas):
    fruta=input("Ingrese el nombre de la fruta: ")
    frutas.append(fruta)

print("Lista de frutas ingresadas:", frutas)

 #eliminar las frutas ingresadas
    
eliminar=input("Ingrese la fruta que quieres eliminar: ")
if eliminar in frutas:
    #si frutilla esta en mi lista de frutas?
    frutas.remove(eliminar)
    
    print("La lista actualizada es :",frutas)

else:
    print("La fruta no esta en la lista")
    