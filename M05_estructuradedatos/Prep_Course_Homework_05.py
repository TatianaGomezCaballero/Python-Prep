#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

'''Crear una lista que contenga nombres de ciudades del mundo que contenga
más de 5 elementos e imprimir por pantalla'''


ciudades = ['popayan', 'neiva','cali','medellin', 'pasto','armenia']
print(ciudades)

# 2) Imprimir por pantalla el segundo elemento de la lista

print(ciudades[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento

print(ciudades[1:3])

# 4) Visualizar el tipo de dato de la lista

print(type(ciudades))

'''Visualizar todos los elementos de la lista a partir del tercero de manera 
genérica, es decir, sin explicitar la posición del último elemento'''

print(ciudades[2:])


# 6) Visualizar los primeros 4 elementos de la lista

print(ciudades[:4])


'''Agregar una ciudad más a la lista que ya exista y otra que no 
¿Arroja algún tipo de error?'''

nueva_ciudades = ciudades.append('valledupar')
ciudad_repetida = ciudades.append('popayan')
print(ciudades)

# No arroja ningun error

# 8) Agregar otra ciudad, pero en la cuarta posición

ciudades.insert(3,'risaralda')
print(ciudades)
# 9) Concatenar otra lista a la ya creada

departamentos = ['valle','cauca', 'nariño']
concatenacion = departamentos + ciudades

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
indice = ciudades.index('popayan')
print(indice)

# 11) ¿Qué pasa si se busca un elemento que no existe?
'''indice_2 = ciudades.index('paris')
print(indice_2)'''

# 12) Eliminar un elemento de la lista

ciudades.pop()
print(ciudades)
# 13) ¿Qué pasa si el elemento a eliminar no existe?

'''ciudades.pop(8)
print(ciudades)'''
# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

ultimo = ciudades[-1]
print(ultimo)
# 15) Mostrar la lista multiplicada por 4

print(ciudades * 4)
# 16) Crear una tupla que contenga los números enteros del 1 al 20

tupla = tuple(range(1,21))
print(tupla)
# 17) Imprimir desde el índice 10 al 15 de la tupla

print(tupla[10:15])
# 18) Evaluar si los números 20 y 30 están dentro de la tupla
compribacion = 20 in tupla or 30 in tupla
print(compribacion)

'''Con la lista creada en el punto 1, validar la existencia del elemento 
'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.'''

comprobacion = 'Paris' in ciudades
print(comprobacion)

ciudades.append('Paris')
print(ciudades)

'''Mostrar la cantidad de veces que se encuentra un elemento específico 
dentro de la tupla y de la lista'''

cantidad = ciudades.count('popayan')
print(cantidad)

# 21) Convertir la tupla en una lista

lista = list(tupla)
print(lista)

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
tupla = (1,2,3)
a,b,c = tupla
print(a,b,c)

'''Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave 
"ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".'''

informacion = {'ciudad':ciudades,
               'pais':['colombia','colombia'],
               'continente':['america', 'america']
               }


# 24) Imprimir las claves del diccionario

print(informacion.keys())

# 25) Imprimir las ciudades a través de su clave

print(informacion['ciudad'])




