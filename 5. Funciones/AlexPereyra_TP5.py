# TP 5 - Funciones en Python
# Alumno: Alex Pereyra
# Comisión: 8

import math

# 1. Función que imprime "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Función que saluda al usuario
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Función que imprime información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4. Función que calcula el área del círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# 4. Función que calcula el perímetro del círculo
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Función que convierte segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Función que imprime la tabla de multiplicar del número dado
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Función que retorna suma, resta, multiplicación y división en una tupla
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return (suma, resta, multiplicacion, division)

# 8. Función que calcula el IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Función que convierte Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Función que calcula el promedio de tres números
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

if __name__ == "__main__":
    imprimir_hola_mundo()
    
    nombre_usuario = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre_usuario))
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    residencia = input("Residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    
    radio = float(input("Ingrese el radio del círculo: "))
    print(f"Área: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")
    
    segundos = int(input("Ingrese cantidad de segundos: "))
    print(f"Horas: {segundos_a_horas(segundos):.2f}")
    
    numero = int(input("Ingrese un número para la tabla de multiplicar: "))
    tabla_multiplicar(numero)
    
    a = float(input("Ingrese número a: "))
    b = float(input("Ingrese número b: "))
    suma, resta, mult, div = operaciones_basicas(a, b)
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div}")
    
    peso = float(input("Ingrese peso en kg: "))
    altura = float(input("Ingrese altura en metros: "))
    print(f"IMC: {calcular_imc(peso, altura):.2f}")
    
    celsius = float(input("Ingrese temperatura en Celsius: "))
    print(f"Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}")
    
    n1 = float(input("Ingrese número 1: "))
    n2 = float(input("Ingrese número 2: "))
    n3 = float(input("Ingrese número 3: "))
    print(f"Promedio: {calcular_promedio(n1, n2, n3):.2f}")
