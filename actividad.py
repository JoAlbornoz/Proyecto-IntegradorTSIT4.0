#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#==================
#Funcion ingreso-lista
'''
Pedir al usuario que ingrese 5 valores enteros
Creación de lista.
'''
def Ingreso_Lista():

    lista=[]

    for x in range(5):
        while True:
            try:
                numero = int(input("Ingrese un número entero: "))
            except ValueError:
                print("Solo se permiten números enteros, vuelve a cargarlo.")
                continue
            else:
                break

        lista.append(numero)
    return lista
 
  
 
    # 1) print("Su nueva lista es: ", lista)   "retiro la porción de codigo para que no se imprima nada desde dentro de la función"
    # 2) La función devuelve lista de 5 valores para ser utilizada fuera de la función.
    # 3) Se me ocurrio agregar mejora para controlar que el número ingresado sea entero y no genere fallo (investigue y agregue: while con try y except)

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
def prom(lista):
        return sum(lista) / len (lista)




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
