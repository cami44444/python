#crear una variable con una contraseña (cami4) pide al usuario
#que ingrese la clave y siga pidiendo con un bucle while hasta que se ingrese 
#la contraseña correcta, termina en bucle cuando aciertes la contraseña
contraseña="cami4"
intentos=input("Ingrese su contraseña: ")

while intentos!=contraseña:
    print("Contraseña incorrecta")
    intentos=input("Ingrese su contraseña: ")
    
print("Acceso concedidoolololo")
