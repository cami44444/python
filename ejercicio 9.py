#crear una variable con una contraseña (python123) pide al usuario
#que ingrese la clave y siga pidiendo con un bucle while hasta que se ingrese 
#la contraseña correcta, termina en bucle cuando aciertes la contraseña
contraseña="python123"
intentos=input("Ingrese su contraseña: ")

while intentos!=contraseña:
    print("Contraseña incorrecta")
    intentos=input("Ingrese su contraseña: ")
    
print("Acceso concedidoooooo")


