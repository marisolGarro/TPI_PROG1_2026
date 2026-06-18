import csv
import questionary

def escribir_csv(paises):
    campos=["nombre","poblacion","superficie","continente"]
    with open("paises.csv","w",newline="",encoding="utf-8-sig") as archivo:
        writer=csv.DictWriter(archivo,fieldnames=campos)
        writer.writeheader()
        writer.writerows(paises)

paises=[
    {"nombre":"Argentina","poblacion":45376763,"superficie":2780400,"continente":"América"},  
{"nombre":"Japón","poblacion":125800000,"superficie":377975,"continente":"Asia" }, 
{"nombre":"Brasil","poblacion":213993437,"superficie":8515767,"continente":"América" }, 
{"nombre":"Alemania","poblacion":83149300,"superficie":357022,"continente":"Europa"}  
]
def menu():
    opcion= questionary.select(
        message="Selecciona: ",
        choices=["1. Agregar país",
"2. Actualizar población y superficie",
"3. Buscar país",
"4. Filtrar país",
"5. Ordenar países",
"6. Mostrar estadísticas",
"7. Salir"]
    ).ask()
    return opcion

def filtrar_menu():
    opcion= questionary.select(
        message="Selecciona: ",
        choices= ["1. Continente",
"2. Rango de población",
"3. Rango de superficie",
"4. Salir"]
).ask()
    return opcion
def ordenar_menu():
    opcion= questionary.select(
        message="Selecciona: ",
        choices= ["1. Nombre",
"2. Población",
"3. Superficie",
"4. Salir"]
).ask()
    return opcion

# SISTEMA DE GESTIÓN DE PAÍSES
# =====================================
#paises = []
# =====================================
# VALIDACIONES
# =====================================
def validar_texto(texto):
    return texto.strip() != ""


def validar_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
# =====================================
# 1 - AGREGAR PAÍS
# =====================================

def agregar_pais():

    nombre = input("Nombre del país: ")

    while not validar_texto(nombre):
        print("Nombre inválido")
        nombre = input("Nombre del país: ")

    poblacion = input("Población: ")

    while not validar_numero(poblacion):
        print("Ingrese un número válido")
        poblacion = input("Población: ")

    superficie = input("Superficie (km²): ")

    while not validar_numero(superficie):
        print("Ingrese un número válido")
        superficie = input("Superficie (km²): ")

    pais = {
        "nombre": nombre,
        "poblacion": float(poblacion),
        "superficie": float(superficie)
    }

    paises.append(pais)

    print("País agregado correctamente")
# =====================================
# 2 - ACTUALIZAR PAÍS
# =====================================

def actualizar_pais():

    nombre = input("Ingrese el país a actualizar: ")

    for pais in paises:

        if pais["nombre"].lower() == nombre.lower():

            nueva_poblacion = input("Nueva población: ")

            while not validar_numero(nueva_poblacion):
                print("Número inválido")
                nueva_poblacion = input("Nueva población: ")

            nueva_superficie = input("Nueva superficie: ")

            while not validar_numero(nueva_superficie):
                print("Número inválido")
                nueva_superficie = input("Nueva superficie: ")

            pais["poblacion"] = float(nueva_poblacion)
            pais["superficie"] = float(nueva_superficie)

            print("País actualizado correctamente")
            return

    print("País no encontrado")

# =====================================
# 6 - ESTADÍSTICAS
# =====================================

def mostrar_estadisticas():

    if len(paises) == 0:
        print("No hay países cargados")
        return

    total_poblacion = sum(
        pais["poblacion"]
        for pais in paises
    )

    total_superficie = sum(
        pais["superficie"]
        for pais in paises
    )

    promedio_poblacion = (
        total_poblacion / len(paises)
    )

    promedio_superficie = (
        total_superficie / len(paises)
    )

    mayor_poblacion = max(
        paises,
        key=lambda p: p["poblacion"]
    )

    menor_poblacion = min(
        paises,
        key=lambda p: p["poblacion"]
    )

    print("\n===== ESTADÍSTICAS =====")
    print("Cantidad de países:", len(paises))
    print("Población total:", total_poblacion)
    print("Superficie total:", total_superficie)
    print("Promedio población:", promedio_poblacion)
    print("Promedio superficie:", promedio_superficie)

    print(
        "País con mayor población:",
        mayor_poblacion["nombre"]
    )

    print(
        "País con menor población:",
        menor_poblacion["nombre"]
    )

