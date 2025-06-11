# Trabajo Práctico 3 - Estructuras Condicionales
# Alumno: Alex Pereyra
# Comisión: 8

# Ejercicio 1
numero = int(input("Ingrese un número: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# Ejercicio 2
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
if a > b:
    print("El mayor es:", a)
elif b > a:
    print("El mayor es:", b)
else:
    print("Ambos números son iguales.")

# Ejercicio 3
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

# Ejercicio 4
nota = float(input("Ingrese la nota (0 a 10): "))
if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

# Ejercicio 5
anio = int(input("Ingrese un año: "))
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("Es un año bisiesto.")
else:
    print("No es un año bisiesto.")

# Ejercicio 6
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Es par.")
else:
    print("Es impar.")

# Ejercicio 7
clave = input("Ingrese la contraseña: ")
if clave == "UTN2025":
    print("Contraseña correcta.")
else:
    print("Contraseña incorrecta.")

# Ejercicio 8
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))
mayor = max(n1, n2, n3)
print("El mayor es:", mayor)

# Ejercicio 9
letra = input("Ingrese una letra: ").lower()
if letra in "aeiou":
    print("Es una vocal.")
else:
    print("No es una vocal.")

# Ejercicio 10
sueldo = float(input("Ingrese su sueldo: "))
if sueldo <= 30000:
    aumento = sueldo * 0.15
elif sueldo <= 60000:
    aumento = sueldo * 0.10
else:
    aumento = sueldo * 0.05
print(f"El aumento es de ${aumento:.2f}")
