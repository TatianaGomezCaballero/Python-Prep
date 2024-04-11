#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

class Vehiculo:
    def __init__(self, color, tipo, cilindraje):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje


'''2) A la clase Vehiculo creada en el punto 1, agregar los siguientes 
métodos:<br>'''
# Acelerar<br>
# Frenar<br>
# Doblar<br>

class Vehiculo:
    def __init__(self, color, tipo, cilindraje):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje
        self.velocidad = 0
        self.direccion = 0

    def Acelerar(self, vel):
        self.velocidad = self.velocidad + vel

    def Frenar(self,vel):
        self.velocidad = self.velocidad - vel
        print(f'mi velocidad fue {vel}')

    def Doblar(self, grados):
        self.direccion = self.direccion + grados



'''Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, 
probar luego el resultado'''

vehiculo_1 = Vehiculo('rojo', 'mazda',1300)
vehiculo_2 = Vehiculo('blanco', 'mazda',1200)
vehiculo_3 = Vehiculo('negro', 'mazda',1100)

print(f'mi auto es {vehiculo_1.color}')
vehiculo_1.Frenar(234)


'''Agregar a la clase Vehiculo, un método que muestre su estado, es decir, 
a que velocidad se encuentra y su dirección. Y otro método que muestre color, 
tipo y cilindrada'''
class Vehiculo:
    def __init__(self, color, tipo, cilindraje):
        self.color = color
        self.tipo = tipo
        self.cilindraje = cilindraje
        self.velocidad = 0
        self.direccion = 0

    def Acelerar(self, vel):
        self.velocidad = self.velocidad + vel

    def Frenar(self,vel):
        self.velocidad = self.velocidad - vel
        print(f'mi velocidad fue {vel}')

    def Doblar(self, grados):
        self.direccion = self.direccion + grados

    def estado(self):
        print(f'Mi velicidad es {self.velocidad} y mi direccion es {self.direccion}')

    def detalle(self):
        print(f'mi color de auto es {self.color}, es de tipo{self.tipo} y el cilindraje es {self.cilindraje}')

a = Vehiculo('negro','mazda', 1200)
a.detalle()
a.estado()


'''Crear una clase que permita utilizar las funciones creadas en la práctica 
del módulo 7<br>'''
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

class Funciones:

    def Verificar_primo(self, numero):
        es_primo = True
        for i in range(2,numero):
            if numero % i == 0:
                es_primo = False
                break
        return es_primo

    def factorial(self, numero):
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




# 6) Probar las funciones incorporadas en la clase del punto 5

a = Funciones()
print(a.Verificar_primo(5))

# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones






