#Cree un programa en python que solicite al usuario su nombre y su edad mediante el teclado, 
# y muestre en pantalla un mensaje personalizado concatenando ambos datos

#Pedimos el nombre al usuario y lo guardamos en la variable nombre
nombre = input("¿Como te llamas?: ")

#Pedimos la edad (puedes agregar mas datos)
edad = input("¿Cuantos años tienes?: ")
telefono = input("¿Cual es tu numero de telefono?: ")
profesion = input("¿Cual es tu profesion?: ")

print("Hola, " + nombre + "! tienes " + edad + " años tu numero de telefono es " + telefono + "  tu profesion es " + profesion + " y estas aprendiendo python.")


