#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es


def verifica_primo(nro):
    es_primo = True
    for i in range(2, nro):
        if nro % i == 0:
            es_primo = False
            break
    return es_primo


resultado = verifica_primo(23)
print(resultado)


'''Utilizando la función del punto 1, realizar otra función que reciba de 
parámetro una lista de números y devuelva sólo aquellos que son primos 
en otra lista'''

def son_primos(lista):
    lista2 = []
    for i in lista:
        if verifica_primo(i):
            lista2.append(i)
    print(lista2)

son_primos([1,2,3,4,5,6,7])


'''Crear una función que al recibir una lista de números, devuelva el 
que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", 
que devuelva cualquiera¿'''

def mas_repetido(lista):
    mas_repetido = []
    cantidad = 0
    for i in range(len(lista)):
        numero_mas_repetido = i
        for j in range(i + 1, len(lista)):
            if lista.count(numero_mas_repetido) < lista.count(j):
                numero_mas_repetido = j
                mas_repetido.append(j)
    return mas_repetido

resultado = mas_repetido([1,2,2,3,4,4,4])
print(resultado)


# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 


# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:


'''Armar una función que devuelva el factorial de un número. Tener en cuenta 
que el usuario puede equivocarse y enviar de parámetro un número no entero 
o negativo'''

def factorial(numero):
    if type(numero) == int:
        if numero > 1:
            factorial = numero

            while numero > 2:
                numero = numero - 1
                factorial = factorial * numero
            return factorial

        else:
            print('Es menor a 1')
    else:
        print('No es entero')

resultado = factorial(6)
print(resultado)







