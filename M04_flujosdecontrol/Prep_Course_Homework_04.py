#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

'''Crear una variable que contenga un elemento del conjunto de
números enteros y luego imprimir por pantalla si es mayor o menor a cero'''

numero = 6
if numero > 0:
    print('Es mayor a 0')
else:
    print('Es menor a 0')

# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

variable_1 = 12
variable_2 = 'Gomez'

if type(variable_1) == type(variable_2):
    print('Son del mismo tipo')
else:
    print('Son diferentes tipos')

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

for num in range(1, 21):
    if num % 2 == 0:
        print(f'{num} es par')
    else:
        print(f'{num} es impar')

'''En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo 
a la potencia igual a 3'''

for num in range(0, 6):
    print(num ** 3)

'''Crear una variable que contenga un número entero y realizar un ciclo for la misma 
cantidad de ciclos'''

numero = 6

for num in range(0, numero):
    print(num)

'''Utilizar un ciclo while para realizar el factoreo de un número guardado 
en una variable, sólo si la variable contiene un número entero mayor a 0'''

numero = 5

if type(numero) == int:
    if numero > 0:
        factorial = numero
        while numero > 2:
            numero = numero - 1
            factorial = factorial * numero
        print(factorial)
    else:
        print('Es menor a 0')
else:
    print('No es un entero')

# 7) Crear un ciclo for dentro de un ciclo while

'''n = 4
while n < 5:
    for i in range(0,n):
        print(i ** 2)
        n = n - 1'''

# 8) Crear un ciclo while dentro de un ciclo for
# 9) Imprimir los números primos existentes entre 0 y 30
for i in range(0, 30):
    es_primo = True
    divisor = 2
    if i >= 2:
        while divisor <= i // 2:
            if i % divisor == 0:
                es_primo = False
            divisor = divisor + 1

        if es_primo:
            print(i)
    else:
        pass

'''¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break 
y/ó continue para tal fin'''
'''for i in range(0, 30):
    es_primo = True
    divisor = 2
    if i >= 2:
        while divisor <= i // 2:
            if i % divisor == 0:
                es_primo = False
            divisor = divisor + 1

        if es_primo:
            print(i)
    else:
        pass'''

'''En los puntos 9 y 10, se diseño un código que encuentra números primos 
y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?'''

'''Aplicando continue, armar un ciclo while que solo imprima los valores divisibles 
por 12, dentro del rango de números de 100 a 300'''

n = 100
while n < 300:
    n = n + 1
    if n % 12 == 0:
        print(n)
        continue

'''Utilizar la función **input()** que permite hacer ingresos por teclado, 
para encontrar números primos y dar la opción al usario de buscar el siguiente'''

numero = int(input('Por favor dame un numero: '))

for i in range(2, numero):
    if numero % i == 0:
        print(False)
    else:
        print(True)
if numero < 2:
    print(False)

'''Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer 
número divisible por 3 y además múltiplo de 6'''

for i in range(100, 301):
    if i % 6 == 0:
        print(f'El numero es {i}')
        break
