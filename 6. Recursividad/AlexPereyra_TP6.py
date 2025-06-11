# TP 6 - Recursividad - UTN a distancia
# Alumno: Alex Pereyra
# Comisión: 8

# 1. Factorial recursivo
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def mostrar_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"{i}! = {factorial(i)}")

# 2. Fibonacci recursivo
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci(hasta):
    for i in range(hasta):
        print(f"F({i}) = {fibonacci(i)}")

# 3. Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# 4. Conversión decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def convertir_a_binario(n):
    binario = decimal_a_binario(n)
    return binario if binario else "0"

# 5. Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# 6. Suma de dígitos recursiva
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# 7. Contar bloques para una pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# 8. Contar apariciones de un dígito
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
