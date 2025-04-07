# TP 4: Estructuras Repetitivas
# Autor: Alex Pereyra
# Comisión: 8

# 1. Imprimir del 0 al 100 en orden creciente
for i in range(101):
    print(i)

# 2. Contar la cantidad de dígitos de un número
num = int(input("Ingrese un número entero: "))
print("Cantidad de dígitos:", len(str(abs(num))))

# 3. Sumar todos los enteros entre dos valores dados (excluyendo los extremos)
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
suma = 0
for i in range(min(a, b) + 1, max(a, b)):
    suma += i
print("La suma es:", suma)

# 4. Sumar números hasta que el usuario ingrese 0
total = 0
while True:
    n = int(input("Ingrese un número (0 para terminar): "))
    if n == 0:
        break
    total += n
print("Suma total:", total)

# 5. Adivinar número aleatorio entre 0 y 9
import random
objetivo = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == objetivo:
        break
print(f"¡Correcto! Lo lograste en {intentos} intentos.")

# 6. Números pares del 0 al 100 en orden decreciente
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

# 7. Sumar números entre 0 y un valor dado
limite = int(input("Ingrese un número entero positivo: "))
suma = sum(range(limite + 1))
print("Suma:", suma)

# 8. Contar pares, impares, positivos y negativos entre 100 números
pares = impares = positivos = negativos = 0
for _ in range(100):
    n = int(input("Ingrese un número: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# 9. Calcular la media de 100 números
total = 0
for _ in range(100):
    n = int(input("Ingrese un número: "))
    total += n
media = total / 100
print("Media:", media)

# 10. Invertir los dígitos de un número
num = input("Ingrese un número: ")
print("Número invertido:", num[::-1])
