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
def estadistica_menu():
    opcion= questionary.select(
        message="Selecciona: ",
        choices= ["1. País con mayor y menor población",
"2. Promedio de población",
"3. Promedio de superficie",
"4. Cantidad de países por continente",
"5. Salir"]
).ask()
    return opcion
