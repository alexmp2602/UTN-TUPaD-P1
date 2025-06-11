# TP 1 - Estructuras Secuenciales
# Alumno: Alex Pereyra
# Comisión: 8

# Ejercicio 1: Imprimir "Hola Mundo!"
print("Hola Mundo!")

# Ejercicio 2: Pedir el nombre del usuario e imprimir un saludo
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# Ejercicio 3: Pedir nombre, apellido, edad y lugar de residencia
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4: Calcular el área y perímetro de un círculo
import math
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El área del círculo es {area:.2f} y su perímetro es {perimetro:.2f}")

# Ejercicio 5: Convertir segundos en horas
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# Ejercicio 6: Imprimir la tabla de multiplicar de un número
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7: Realizar operaciones con dos números
num1 = int(input("Ingrese el primer número entero distinto de 0: "))
num2 = int(input("Ingrese el segundo número entero distinto de 0: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division:.2f}")

# Ejercicio 8: Calcular el índice de masa corporal (IMC)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal (IMC) es {imc:.2f}")

# Ejercicio 9: Convertir grados Celsius a Fahrenheit
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# Ejercicio 10: Calcular el promedio de tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es {promedio:.2f}")
