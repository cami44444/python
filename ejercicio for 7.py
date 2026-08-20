#Escriba un programa en Python que solicite un número entero al usuario
# y genere su tabla de multiplicar del 1 al 10 utilizando un bucle for. 

#Pide un numero al usuario y genera su tabla de multiplicar
# del 1 al 10
numero=int(input("Ingrese numero para saber la tabla: "))

for i in range (1,11,1):
    resultado=numero*i
    print(numero,"x",i,"=",resultado)
    

    
    
           