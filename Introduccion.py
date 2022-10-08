# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script" f(ile.
"""
#comentario de una sola linea
print("hola mundo")

"""
COMENTARIOS DE MULTIPLES LÍNEAS
5+5
5*5
5-5
"""
#Creacion de variables
x=3
y=float()
z=int()
a=bool(True)
#Uso de variables
print(x)
print(x+2)
print(x*2)
str1="Cisco "
print(str1*10)
print("\n"*2) #Salto de linea doble
print(x+2)
print(x*2)

##CONCATENAR VARIABLES SOLO DE STRING
#Creación de variables
str1="Cisco"
str2="Netrworking"
str3="Academy"
space=" "
#Union de SOLO strings
print (str1+space+str2+space+str3)
print("\n")
print(str1,str2,str3) #solo muestra variables
print("\n")

##INT Y STRING
print("el valor de x es: "+ str(x)) #no modifica el int
x=str(x) #Reasignación a str
x=int(x) #Reasignación a int
