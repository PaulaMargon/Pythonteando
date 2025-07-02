"""
Ejercicio de Codificación 1
Tu tarea es crear un programa que genere un número entero aleatorio. Así es como debe comportarse el programa:

Como puedes ver, el programa primero pide al usuario que ingrese un número entero. Luego, una vez que el usuario ingresa un número, el programa le pide nuevamente que ingrese otro número.
Después, el programa devuelve un número aleatorio que se encuentra entre los dos números enteros.
"""

import random

num1 = int(input("Por favor, escribe un número: "))
num2 = int(input("Por favor, escribe un segundo número mayor que el primero: "))

numrandom = random.randint(num1, num2)
print(numrandom)

