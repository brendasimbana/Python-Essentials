# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 20:09:01 2022

@author: brend
"""

""" 
Crear una función que reciba un parámetro (n)
y cree los numero de la sucesión de Fibonacci.
Ejemplo:
Fibonacci(8)
Resultado:
0 1 1 2 3 5 8
"""
def fibonacci(n):
    a=0
    b=1
    total=0
    count=1
    print("Fibonacci: ")
    while(count<n):    
        print(total)
        count+=1
        a=b
        b=total
        total=a+b	
    
n=input("numero: ")
n=int(n)
fibonacci(n)