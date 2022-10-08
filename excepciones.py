# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 20:26:16 2022

@author: brend
"""

try:
    y = 1 / 0
except ArithmeticError: #mas general
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")

print("THE END.")