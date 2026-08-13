#Enunciado: Agenda de contactos
#Crea un programa en python que simule una agenda de contactos con las sgts funciones:
#1. Registrar contactos: El programa debe pedir al usuario que ingrese 3 nombres de contactos de contactos por teclado y guardarlos en uan lista
#2. Eliminar contacto: Despues de registrarlos, el programa dee pedir el nombre de un contacto para eliminarlo
#Si el contacto existe, eliminarlo y mostrar: Eliminado correctamente
#Si el contacto no existe, mostrar: Ese contacto no existe
#3. Mostrar agenda prdenada: Al final, ordenar todos los contactos restantes de forma alfabetica A-Z y mostrar la lista completa con el mensaje: Agenda ordenada
agenda_contactos=[]
cantidad=int(input("Ingrese la cantidad de contactos: "))
for i in range (cantidad):
    contacto=input("Ingresar el contacto") 
    agenda_contactos.append(contacto)

eliminar=input("Ingresar el contacto a eliminar") 
if eliminar in agenda_contactos:
    print("Se elimino correctamente")
else:
    print("El usuario no existe")
print("Lista de contactos",agenda_contactos.sort())


    


    

