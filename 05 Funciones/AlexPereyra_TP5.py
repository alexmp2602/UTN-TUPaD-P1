# TP 4: Estructuras Repetitivas
# Autor: Alex Pereyra
# Comisión: 8

# Ejercicio 1: Función imprimir_hola_mundo
def imprimir_hola_mundo():
    print("¡Hola Mundo!")

# Llamar a la función
imprimir_hola_mundo()

# Ejercicio 2: Función saludar_usuario
def saludar_usuario(nombre):
    return f"¡Hola {nombre}!"

# Solicitar el nombre y llamar a la función
nombre_usuario = input("Introduce tu nombre: ")
print(saludar_usuario(nombre_usuario))

# Ejercicio 3: Función informacion_personal
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

# Solicitar los datos y llamar a la función
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = input("Introduce tu edad: ")
residencia = input("Introduce tu lugar de residencia: ")

print(informacion_personal(nombre, apellido, edad, residencia))

# Ejercicio 4: Función calcular_area_circulo
import math
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

# Solicitar el radio y llamar a la función
radio = float(input("Introduce el radio del círculo: "))
print(f"El área del círculo es: {calcular_area_circulo(radio)}")

# Ejercicio 5: Función segundos_a_horas
def segundos_a_horas(segundos):
    return segundos / 3600

# Solicitar los segundos y llamar a la función
segundos = int(input("Introduce el número de segundos: "))
print(f"{segundos} segundos son {segundos_a_horas(segundos)} horas.")

# Ejercicio 6: Función tabla_multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicitar el número y llamar a la función
numero = int(input("Introduce un número para la tabla de multiplicar: "))
tabla_multiplicar(numero)

# Ejercicio 7: Función operaciones_basicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido"  # Para evitar división por 0
    return suma, resta, multiplicacion, division

# Solicitar los números y llamar a la función
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}, Resta: {resultados[1]}, Multiplicación: {resultados[2]}, División: {resultados[3]}")

# Ejercicio 8: Función calcular_imc
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Solicitar los datos y llamar a la función
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))
print(f"Tu IMC es: {calcular_imc(peso, altura)}")

# Ejercicio 9: Función calcular_celsius_a_fahrenheit
def calcular_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Solicitar la temperatura en Celsius y llamar a la función
celsius = float(input("Introduce la temperatura en grados Celsius: "))
print(f"Temperatura en Fahrenheit: {calcular_celsius_a_fahrenheit(celsius)}")

# Ejercicio 10: Función calcular_promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Solicitar los números y llamar a la función
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
c = float(input("Introduce el tercer número: "))
print(f"El promedio es: {calcular_promedio(a, b, c)}")
