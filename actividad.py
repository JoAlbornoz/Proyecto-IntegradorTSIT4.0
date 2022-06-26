#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#==================
#Funcion ingreso-lista
'''
Pedir al usuario que ingrese 5 valores enteros
Creación de lista.
'''

lista=[]

for x in range(5):
    numero = int(input("Ingrese un número entero: "))
    lista.append(numero)

print("Su nueva lista es: ", lista)


#==================
#Funcion Suma
'''
Recibe como parámetro la lista
Devuelve la suma total de todos sus elementos.
'''

def suma(lista):
	resultado = sum(lista)
	return resultado



#==================
#Funcion Promedio
'''
Recibe como parámetro la lista
devuelve el promedio de sus elementos.
'''





#==================
#Funcion Maximo
'''
Recibe como parámetro la lista
devuelve el valor máximo de todos los elementos que contiene.
'''

def maximo(lista):
    res = max(lista)
    return res



#==================
#Funcion Minimo
'''
Recibe como parámetro la lista
devuelve el valor mínimo de todos los elementos que contiene.
'''
def minimo(lista):
    res = min(lista)
    return res
    

#==================
#Funcion Principal
