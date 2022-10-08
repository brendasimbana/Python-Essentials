# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:44:00 2022

@author: brend
"""

##LISTAS
print("\n")
lista=[5,5.6,"Hola",True,-5]
print(type(lista))
print(len(lista)) #posicion desde 0
print(lista)
print("posición 0: ",lista[0])
print("posición -1: ",lista[-1])#forma cilídrica
#NO EXISTE print("posición 5: ",lista[5])
print("posición -5: ",lista[-5])
#FUERA DE RANGO print("posición -6: ",lista[-6])
lista[0]=15 #reasignación de variable
print("nueva lista 1: ",lista)
del (lista[4])
print("nueva lista 2: ",lista)


##TUPLAS
print("\n")
tupla=(5,5.6,"Hola",True,5)
print("posicion2: ",tupla[2])
"""tupla[0]=12
print(tupla)""" #No soporta reasignacion de variables
"""del (tupla[4])
print(tupla)""" #No soporta eliminación de variables


##DICCIONARIO
print("\n")
dict1={"r1":"10.1",
       "r2":"10.2",
       5100:"Brenda",
       "email": "brenasimbana@gmail.com",
       }
"""5100:"damaris
NO PUEDEN EXISTIR VARIABLES REPETIDAS EN UN DICCIONARIO"""

print(dict1)
print("tipo de variable: ",type(dict1))
print("longitud: ",len(dict1))
print("r1: ",dict1["r1"])
print("5100: ",dict1[5100])
print("email",dict1["email"])
dict1["s1"]="10.3"
dict1[6]=566 #se añade key/valor #dict1[key]=value
print("Nuevo dict1: ", dict1)
print("está r3 en dict1? ","R3" in dict1)#comando key in dictionario
print("está s1 en dict1? ","s1" in dict1)#comando key in dictionario


