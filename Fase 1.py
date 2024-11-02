# Description: Fase 1 - Ejercicio para obtener el nombre de una persona y mostrarlo por pantalla
# nombre = input("¿Cual es tu nombre? ")
# print("Hola", nombre)
from random import random
from unicodedata import numeric


#Description: Fase 1 - Escribe un programa que pida un número y muestre si es par o impar.
# numero = int(input("Ingrese un numero: "))
# if numero % 2 == 0:
#     print("El número ingresado es par")
# else:
#     print("El número ingresado es impar")

#Description: Fase 1 - Crea una lista con los números del 1 al 10 y usa un bucle for para imprimir cada número multiplicado por 2.
# rango = range(1, 10)
# for num in rango:
#     print(num*2)

#Description: Fase 1 - Escribe una función que tome dos números como parámetros y devuelva su suma.
# def sumar(a, b):
#     return a+b
#
# num_a = int(input("Ingrese un numero para sumar: "))
# num_b = int(input("Ingrese el siguiente numero para sumar: "))
#
# print(sumar(num_a, num_b))

#Description: Fase 1 - Crea una tabla de multiplicar del 1 al 5 usando bucles anidados.
# for num in range(1, 6):
#     for mul in range(0, 10):
#         print(f"{num} x {mul} = {num * mul}")
#     print()

#Description: Fase 1 - Genera una lista de los cuadrados de los números del 1 al 10 usando una comprensión de listas.
# listado = [x**2 for x in range(1, 11)]
# print(listado)

#Description: Fase 1- Escribe un bucle que recorra los números del 1 al 20 y solo imprima los números impares.
#Usa continue para omitir los números pares.

# for i in range(1, 21):
#     if i % 2 == 0:
#         continue
#     else:
#         print(f"El número {i} es impar")

#Mini Proyectos

#Calculadora simple: Crea un programa que tome dos números y un operador (+, -, *, /) y devuelva el resultado.

# def operacion(num_a, num_b, op):
#     if op == "+":
#         return num_a + num_b
#     elif op == "-":
#         return num_a - num_b
#     elif op == '*':
#         return num_a * num_b
#     elif op == "/":
#         return num_a / num_b
#     else:
#         return "No se selecciono un operador valido"
#
# num_a = int(input("Ingrese un número: "))
# num_b = int(input("Ingrese otro número: "))
# operador = input("Ingrese un operador (+, -, *, /): ")
#
# print(operacion(num_a, num_b, operador))

#Adivina el número: Crea un juego en el que el programa genere un número aleatorio y el usuario deba adivinarlo, indicando si el intento es mayor o menor hasta acertar.
from random import randint

aleatorio = randint(0, 10)
num = 11

while aleatorio != num:
    num = int(input("Ingrese un numero: "))
    if num > aleatorio:
        print("El numero es menor")
    elif num < aleatorio:
        print("El numero es mayor")
    elif num == aleatorio:
        print("Adivinaste")
        break
