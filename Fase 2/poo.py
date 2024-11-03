# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
#
#     def saludar(self):
#         print(f"Hola mi nombre es {self.nombre}")
#
#     def mi_edad(self):
#         print(f"Yo tengo {self.edad} años")
#
# persona = Persona("Andersson Pérez", 31)
# persona.saludar()
# persona.mi_edad()

#Herencia
#Ejercicio: Crea una clase Empleado que herede de Persona e incluya un atributo salario.

class Persona:
    def salario(self):
        print("Salario es 0")

class Empleado(Persona):
    def salario(self):
        print("Mi salario es 1000")

empleado = Empleado()
empleado.salario()