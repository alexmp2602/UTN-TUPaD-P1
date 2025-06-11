# TP 5.1 - Listas - UTN a distancia
# Alumno: Alex Pereyra
# Comisión: 8

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4
multiplos_de_4 = list(range(4, 101, 4))
print("Ejercicio 1:", multiplos_de_4)

# 2) Crear una lista con cinco elementos y mostrar el penúltimo
favoritos = ["pizza", "programación", "gatos", "montaña", "música"]
print("Ejercicio 2:", favoritos[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimirla
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print("Ejercicio 3:", lista_vacia)

# 4) Reemplazar segundo y último valor en la lista 'animales'
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("Ejercicio 4:", animales)

# 5) Este ejercicio solicita análisis. Lo agregás manualmente en el README.

# 6) Crear lista de 10 a 30, saltos de 5, mostrar los dos primeros
rango_saltos = list(range(10, 31, 5))
print("Ejercicio 6:", rango_saltos[:2])

# 7) Reemplazar valores centrales en la lista 'autos'
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["civic", "focus"]
print("Ejercicio 7:", autos)

# 8) Crear lista 'dobles' con los dobles de 5, 10 y 15
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Ejercicio 8:", dobles)

# 9) Manipular lista 'compras'
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print("Ejercicio 9:", compras)

# 10) Crear lista anidada con elementos indicados
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("Ejercicio 10:", lista_anidada)
