#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, time
import winsound   

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
#Funcion Seleccion

def seleccion(): # no recibe ningun parametro de entrada
    print ("""
    Estas son las operaciones que puedo realizar:

    1 - Sumar los numeros ingresados.
    2 - Calcular el promedio de los numeros ingresados.
    3 - Mostrar el valor maximo ingresado.
    4 - Mostrar el valor minimo ingresado.
    5 - Terminar y salir.
    """)
    #El usuario ingresa el numero de la operacion que quiere realizar
    opcion = input("Ingresar el numero de la operacion: ")
    return opcion




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
#prueba
def prom(lista):
    return sum(lista) / len (lista)



True
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
    #res = min(lista)
    #return res

    Menor=lista[0]
    for x in lista:
        if x < Menor:
           Menor=x
    return Menor
    

#==================
#Funcion Principal

def main():
    winsound.PlaySound("hussein_got_im.wav", winsound.SND_ASYNC)   #Para el grupo
    print('''
    
     ''')
    print('='*50)

    print('Actividad integradora Programacion Inicial IT4.0')
    print('-'*22+'Aula 4'+'-'*22)
    print('''
    
     ''')

    lista = Ingreso_Lista()

    while True:
        opcion = seleccion()

        if opcion == '1':
            print('La suma de los elementos es:', suma(lista))
            
        elif opcion == '2':
            print('El promedio de los elementos es:', prom(lista))

        elif opcion == '3':
            print('El máximo elemento es:', maximo(lista))

        elif opcion == '4':
            print('El mínimo elemento es:', minimo(lista))

        elif opcion == '5': #siguiendo la idea de Nahuel, se puede hacer un saludo sin salir del ciclo hasta que se ejecute sys.exit(1)
            print(
                '''
                SUERTE
                '''
            )   #Esto se puede embellecer
            time.sleep(.5)      #detiene la ejecución x segundos (0,5 en este caso)
            sys.exit(1)
        else:
            print('La opción seleccionada no es válida, por favor intentelo de nuevo.')

        

if __name__ == '__main__':
    main()