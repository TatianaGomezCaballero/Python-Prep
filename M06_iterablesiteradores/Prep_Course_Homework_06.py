#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

'''A partir de una lista vacía, utilizar un ciclo while para
cargar allí números negativos del -15 al -1'''

lista = []
n = -15
while n < -1:
    n = n + 1
    lista.append(n)

print(lista)

'''¿Con un ciclo while sería posible recorrer la lista para imprimir 
sólo los números pares?'''

n = 0
while n < len(lista):
    if lista[n] % 2 == 0:
        print(lista[n])
    n = n + 1


# 3) Resolver el punto anterior sin utilizar un ciclo while

for i in lista:
    if i % 2 == 0:
        print(i)
    else:
        pass
# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

for i in lista[:3]:
    print(i)
'''Utilizar la función **enumerate** para obtener dentro del iterable, 
tambien el índice al que corresponde el elemento'''

for i, e in enumerate(lista):
    print(f'{i}:{e}')

'''Dada la siguiente lista de números enteros entre 1 y 20, crear 
un ciclo donde se completen los valores faltantes: 
lista = [1,2,5,7,8,10,13,14,15,17,20]'''

lista = [1,2,5,7,8,10,13,14,15,17,20]

n = 1

while n <=20:
    if not(n in lista):
        lista.insert((n-1),n)
    n = n + 1

print(lista)

# 2 forma funcion
lista = [1,2,5,7,8,10,13,14,15,17,20]

def poner_numeros(lista):
    n = 1
    while n < 20:
        if not(n in lista):
            lista.insert((n-1), n)
        n = n + 1
    print(lista)

poner_numeros(lista)




'''La sucesión de Fibonacci es un listado de números 
que sigue la fórmula: 
n<sub>0</sub> = 0
n<sub>1</sub> = 1
n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
Crear una lista con los primeros treinta números de la sucesión.<br>'''

fibo = [0,1]
n = 2

while n < 30:
    fibo.append(fibo[n-1] + fibo[n-2])
    n = n + 1
print(fibo)


# funcion
def fibonacci(n):
    fibo = [0, 1]
    for i in range(2,n):
        fibo.append(fibo[i -1] + fibo[i -2])
    print(fibo)

fibonacci(10)

# 2 forma de hacerlo
fibon = [0,1]
n = 12

for i in range(2,n):
    fibon.append(fibon[i -1] + fibon[i-2])
print(fibon)

# 8) Realizar la suma de todos elementos de la lista del punto anterior

suma = sum(fibo)
print(suma)
'''9) La proporción aurea se expresa con una proporción matemática que nace 
el número irracional Phi= 1,618… que los griegos llamaron número áureo. 
El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista 
del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos 
números contiguos:
<br>Donde i es la cantidad total de elementos<br>
n<sub>i-1</sub> / n<sub>i</sub><br>
n<sub>i-2</sub> / n<sub>i-1</sub><br>
n<sub>i-3</sub> / n<sub>i-2</sub><br>
n<sub>i-4</sub> / n<sub>i-3</sub><br>
n<sub>i-5</sub> / n<sub>i-4</sub><br>'''

numeros = 15
n = numeros - 5
while n < numeros:
    print(fibo[n -1] / fibo[n - 2])
    n = n + 1

'''10) A partir de la variable cadena ya dada, mostrar en qué posiciones 
aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'''

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

for i,e in enumerate(cadena):
    if e == 'n':
        print(i)
# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

diccionario ={'nombre':'tati',
              'profesion': 'biologa'}

for nombre, info in diccionario.items():
    print(nombre)

'''Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con 
un iterador'''

varriable = 'cadena'

lista = list(varriable)

for i in lista:
    print(i)

# 13 Crear dos listas y unirlas en una tupla utilizando la función zip

lista = [1,2,3]
lista_2 = [4,5,6]
combinar = zip(lista, lista_2)
print(list(combinar))

'''14) A partir de la siguiente lista de números, crear una nueva 
sólo si el número es divisible por 7<br>
lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]'''

lista = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lista2 = []

for i in lista:
    if i % 7 == 0:
        lista2.append(i)
print(lista2)

'''15) A partir de la lista de a continuación, contar la cantidad total de 
elementos que contiene, teniendo en cuenta que un elemento de la lista 
podría ser otra lista:<br>
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]'''

lista = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

cantidad = 0
for i in lista:
    if type(i) == list:
        cantidad = cantidad + len(i)
    else:
        cantidad = cantidad + 1
print(cantidad)


'''16) Tomar la lista del punto anterior y convertir cada elemento en una lista 
si no lo es'''

for i in lista:
    if type(i) != list:
        print(list(i))

