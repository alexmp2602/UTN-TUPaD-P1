# TP 7 - Estructuras de datos complejas (sin objetos)
# Alumno: Alex Pereyra
# Comisión: 8

# 1) Añadir frutas y precios
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Crear lista con solo frutas
frutas = list(precios_frutas.keys())

# 4) Programa para cargar y consultar contactos telefónicos
def cargar_contactos():
    contactos = {}
    print("Cargar 5 contactos (nombre y número):")
    for _ in range(5):
        nombre = input("Nombre: ")
        numero = input("Número: ")
        contactos[nombre] = numero
    return contactos

def consultar_contacto(contactos):
    nombre = input("Ingrese nombre para consultar número: ")
    if nombre in contactos:
        print(f"Número de {nombre}: {contactos[nombre]}")
    else:
        print("Contacto no encontrado.")

# 5) Frase: palabras únicas y frecuencia
def analizar_frase():
    frase = input("Ingrese una frase: ")
    palabras = frase.split()
    palabras_unicas = set(palabras)
    print("Palabras únicas:", palabras_unicas)

    contador = {}
    for p in palabras:
        contador[p] = contador.get(p, 0) + 1
    print("Frecuencia de palabras:", contador)

# 6) Promedio notas de alumnos
def promedios_alumnos():
    alumnos = {}
    for _ in range(3):
        nombre = input("Nombre del alumno: ")
        notas = tuple(float(input(f"Nota {_+1}: ")) for _ in range(3))
        alumnos[nombre] = notas
    for nombre, notas in alumnos.items():
        promedio = sum(notas)/len(notas)
        print(f"Promedio de {nombre}: {promedio:.2f}")

# 7) Operaciones con sets de estudiantes
def operaciones_sets():
    parc1 = {1,2,3,4,5}
    parc2 = {4,5,6,7,8}
    ambos = parc1.intersection(parc2)
    solo_uno = parc1.symmetric_difference(parc2)
    total = parc1.union(parc2)
    print("Aprobaron ambos parciales:", ambos)
    print("Aprobaron solo uno:", solo_uno)
    print("Aprobaron al menos un parcial:", total)

# 8) Diccionario stock productos
def stock_productos():
    stock = {}
    while True:
        opcion = input("Ingrese 'consultar', 'agregar' o 'nuevo' o 'salir': ")
        if opcion == "salir":
            break
        elif opcion == "consultar":
            prod = input("Producto a consultar: ")
            print(f"Stock de {prod}: {stock.get(prod, 0)}")
        elif opcion == "agregar":
            prod = input("Producto a agregar: ")
            cant = int(input("Cantidad a agregar: "))
            stock[prod] = stock.get(prod, 0) + cant
            print(f"Nuevo stock de {prod}: {stock[prod]}")
        elif opcion == "nuevo":
            prod = input("Nuevo producto: ")
            cant = int(input("Cantidad inicial: "))
            stock[prod] = cant
            print(f"Producto {prod} agregado con stock {cant}")

# 9) Agenda con tuplas como claves
def agenda():
    agenda = {
        (1, 9): "Clase Matemáticas",
        (1, 11): "Clase Física",
        (2, 9): "Reunión Equipo",
    }
    dia = int(input("Día a consultar: "))
    hora = int(input("Hora a consultar: "))
    evento = agenda.get((dia, hora), "No hay actividad")
    print(f"Evento: {evento}")

# 10) Invertir diccionario país-capital
def invertir_diccionario(paises):
    invertido = {capital: pais for pais, capital in paises.items()}
    return invertido

# Ejemplo uso invertir diccionario
paises = {'Argentina': 'Buenos Aires', 'Brasil': 'Brasilia', 'Chile': 'Santiago'}
capitales_invertido = invertir_diccionario(paises)

if __name__ == "__main__":
    print("Ejercicios TP6 Estructuras de datos complejas")

    print("\nEjercicio 1-3:")
    print("Diccionario precios frutas:", precios_frutas)
    print("Lista frutas:", frutas)

    print("\nEjercicio 4:")
    contactos = cargar_contactos()
    consultar_contacto(contactos)

    print("\nEjercicio 5:")
    analizar_frase()

    print("\nEjercicio 6:")
    promedios_alumnos()

    print("\nEjercicio 7:")
    operaciones_sets()

    print("\nEjercicio 8:")
    stock_productos()

    print("\nEjercicio 9:")
    agenda()

    print("\nEjercicio 10:")
    print("Diccionario invertido capitales-paises:", capitales_invertido)
