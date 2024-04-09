#!/usr/bin/env python
# coding: utf-8

# ## Variables

'''Crear una variable que contenga un elemento del conjunto de números
enteros y luego imprimir por pantalla'''

entero = 23
print(entero)


# 2) Imprimir el tipo de dato de la constante 8.5

print(type(8.5))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1

print(type(entero))

# 4) Crear una variable que contenga tu nombre

nombre = 'Tatianita'

# 5) Crear una variable que contenga un número complejo

complejo = 5 + 3j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5

print(type(complejo))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

pi = 3.1416

print(round(pi, 3))

'''Crear una variable que contenga el valor 'True' y otra que contenga 
el valor True. ¿Se trata de lo mismo?'''

booleano = True
caden = 'True'

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

print(type(booleano))
print(type(caden))

# 10) Asignar a una variable, la suma de un número entero y otro decimal

entero = 34
decimal = 45.7

suma = entero + decimal

# 11) Realizar una operación de suma de números complejos

complejo1 = 4 + 5j
complejo2 = 7 + 3j

suma = complejo1 + complejo2
print(suma)

# 12) Realizar una operación de suma de un número real y otro complejo

numero_real = 45
numero_complejo = 3 + 7j

suma = numero_real + numero_complejo
print(suma)

# 13) Realizar una operación de multiplicación

multiplicacion = 4 * 5
print(multiplicacion)

# 14) Mostrar el resultado de elevar 2 a la octava potencia

potencia = 2 ** 8
print(potencia)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

cociente = 27 // 4
print(cociente)

# 16) De la división anterior solamente mostrar la parte entera

entero = int(cociente)
print(entero)

# 17) De la división de 27 entre 4 mostrar solamente el resto

resto = 27 % 4
print(resto)

'''Utilizando como operandos el número 4 y los resultados obtenidos 
en los puntos 16 y 17. Obtener 27 como resultado'''

multiplicacion = 6 * 4
suma = multiplicacion + 3
print(suma)

'''Utilizar el operador "+" en una operación donde intervengan solo variables 
alfanuméricas'''

nombre = 'Tatiana'
edad = 26

print(f'mi nombre es {nombre} y tengo {edad} años')

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

print('2' == 2)

'''Utilizar las funciones de cambio de tipo de dato, para que la validación 
del punto 20 resulte verdadera'''

numero = '2'
numero2 = 2
numero_entero = int(numero)

print(numero2 == numero_entero)

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# porque string no se puede cambiar a float

'''Crear una variable con el valor 3, y utilizar el operador 
'-=' para modificar su contenido y que de como resultado 2.'''

numero = 3
numero = numero - 1
print(numero)

'''Realizar la operacion 1 << 2 ¿Por qué da ese resultado? 
¿Qué es el sistema de numeración binario?'''

print(1 << 2)

'''25) Realizar la operación 2 + '2' ¿Por qué no está permitido? 
¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?'''

# no son del mismo tipo

# 26) Realizar una operación válida entre valores de tipo entero y string

cadena = '34'
numero = 4

print(cadena * numero)




