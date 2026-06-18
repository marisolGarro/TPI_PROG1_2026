import csv
import os
from funciones import*
import unicodedata

#Limpiar la consola
def limpiar_consola():
    os.system("cls")

#La funcion normalizar recibe un texto y lo tranforma para poder trabajar
def normalizar(texto):
    #''.join vulve a unir los caracteres sin dejar espacios para formar el texto después de analizarlo
    return ''.join(
        #En esta parte separa el texto en caracteres y tambien separa las tildes
        c for c in unicodedata.normalize('NFD', texto)
        #Acá se analiza cada tipo de caracter y si es una tilde no lo guarda
        if unicodedata.category(c) != 'Mn'
    ).lower() #convierto todo a minúscula

def buscar_pais():
    pais_buscado=normalizar(input("Ingrese el país que desea buscar: ")).strip()
    
    with open("paises.csv","r",newline="",encoding="utf-8-sig") as archivo:
        #Cada fila la representa como un diccionario
        lector=csv.DictReader(archivo)
        encontrado=False
        for fila in lector:
            #Verifica si el pais empieza por los caracteres ingresados
            if (normalizar(fila["nombre"])).startswith(pais_buscado):
                print(f"\nPais: {fila["nombre"]}")
                print(f"Población: {fila["poblacion"]}")
                print(f"Superficie: {fila["superficie"]} km²")
                print(f"Contienente: {fila["continente"]}\n")
                print("-"*30)
                encontrado=True
        if not encontrado:
            raise ValueError("El país ingresado no existe en el registro")
    
def filtrar_pais_continente():
    opcion= questionary.select(
        message="Selecciona: ",
        choices=["1. África",
"2. América",
"3. Asia",
"4. Europa",
"5. Oceanía",
"6. Salir"]
    ).ask()
    with open("paises.csv","r",newline="",encoding="utf-8-sig") as archivo:
        lector=csv.DictReader(archivo)
        encontrado=False
        match opcion:
            case "1. África":
                for fila in lector:     
                    if fila["continente"]=="África":
                        print(f"\nPais: {fila["nombre"]}")
                        print(f"Población: {fila["poblacion"]}")
                        print(f"Superficie: {fila["superficie"]} km²\n")
                        print("-"*30)
                        encontrado=True
                if not encontrado:
                    raise ValueError("No hay países registrados en ese continente")
            case "2. América":
                for fila in lector:
                    if fila["continente"]=="América":
                        print(f"\nPais: {fila["nombre"]}")
                        print(f"Población: {fila["poblacion"]}")
                        print(f"Superficie: {fila["superficie"]} km²\n")
                        print("-"*30)
                        encontrado=True
                if not encontrado:
                    raise ValueError("No hay países registrados en ese continente")
            case "3. Asia":
                for fila in lector:
                    if fila["continente"]=="Asia":
                        print(f"\nPais: {fila["nombre"]}")
                        print(f"Población: {fila["poblacion"]}")
                        print(f"Superficie: {fila["superficie"]} km²\n")
                        print("-"*30)
                        encontrado=True
                if not encontrado:
                    raise ValueError("No hay países registrados en ese continente")
            case "4. Europa":
                for fila in lector:
                    if fila["continente"]=="Europa":
                        print(f"\nPais: {fila["nombre"]}")
                        print(f"Población: {fila["poblacion"]}")
                        print(f"Superficie: {fila["superficie"]} km²\n")
                        print("-"*30)
                        encontrado=True
                if not encontrado:
                    raise ValueError("No hay países registrados en ese continente")
            case "5. Oceanía":
                for fila in lector:
                    if fila["continente"]=="Europa":
                        print(f"\nPais: {fila["nombre"]}")
                        print(f"Población: {fila["poblacion"]}")
                        print(f"Superficie: {fila["superficie"]} km²\n")
                        print("-"*30)
                        encontrado=True
                if not encontrado:
                    raise ValueError("No hay países registrados en ese continente")
            case "6. Salir":
                print("Volviendo al menú Filtrar paises")
                return

def filtrar_por_población():
    while True: 
        try:
            poblacion_menor=int(input("Ingrese el rango inferior: "))
            poblacion_sup=int(input("Ingrese el rango superior: "))
            if poblacion_menor<0 or poblacion_sup<0:
                raise ValueError("El valor de la población no puede ser negativo")
            if poblacion_menor>poblacion_sup:
                raise ValueError("El rango inferior no puede ser mayor al rango superior")
            break
        except ValueError as e:
            if "invalid literal" in str(e):
                print("El valor ingresado es incorrecto")
            else:
                print(f"Error: {e}")
    with open("paises.csv","r",newline="",encoding="utf-8-sig") as archivo:
        lector=csv.DictReader(archivo)
        encontrado=False
        for fila in lector:
            if poblacion_menor<int(fila["poblacion"])<poblacion_sup:
                print(f"\nPais: {fila["nombre"]}")
                print(f"Población: {fila["poblacion"]}")
                print(f"Superficie: {fila["superficie"]} km²")
                print(f"Contienente: {fila["continente"]}\n")
                print("-"*30)
                encontrado=True
        if not encontrado:
            raise ValueError("No se encuentraron países en el rango de población ingresado")

def filtrar_por_superficie():
    while True:
        try:
                superficie_menor=int(input("Ingrese el rango inferior: "))
                superficie_sup=int(input("Ingrese el rango superior: "))
                if superficie_menor<0 or superficie_sup<0:
                    raise ValueError("El valor de la superficie no puede ser negativo")
                if superficie_menor>superficie_sup:
                    raise ValueError("El rango inferior no puede ser mayor al rango superior")
                break
        except ValueError as e:
            if "invalid literal" in str(e):
                print("El valor ingresado es incorrecto")
            else:
                print(f"Error: {e}")
    with open("paises.csv","r",newline="",encoding="utf-8-sig") as archivo:
        lector=csv.DictReader(archivo)
        encontrado=False
        for fila in lector:
            if superficie_menor<int(fila["superficie"])<superficie_sup:
                print(f"\nPais: {fila["nombre"]}")
                print(f"Población: {fila["poblacion"]}")
                print(f"Superficie: {fila["superficie"]} km²")
                print(f"Contienente: {fila["continente"]}\n")
                print("-"*30)
                encontrado=True
        if not encontrado:
            raise ValueError("No se encuentraron países en el rango de superficie ingresado")

def ordenar_por_pais():
    opcion= questionary.select(
        message="Selecciona: ",
        choices=["1. Ordenar nombres de paises de A -> Z",
"2. Ordenar nombres de paises de Z -> A"]
    ).ask()
    with open("paises.csv","r",newline="",encoding="utf-8-sig") as archivo:
        lector=csv.DictReader(archivo)
        paises=list(lector)
        match opcion:
            case "1. Ordenar nombres de paises de A -> Z":
                paises_ordenados = sorted(paises, key=lambda pais: normalizar(pais["nombre"]))
                for pais in paises_ordenados:
                    print(f"\nPais: {pais["nombre"]}")
                    print(f"Población: {pais["poblacion"]}")
                    print(f"Superficie: {pais["superficie"]} km²")
                    print(f"Contienente: {pais["continente"]}\n")
                    print("-"*30)
            case "2. Ordenar nombres de paises de Z -> A":
                paises_ordenados = sorted(paises, key=lambda pais: normalizar(pais["nombre"]),reverse=True)
                for pais in paises_ordenados:
                    print(f"\nPais: {pais["nombre"]}")
                    print(f"Población: {pais["poblacion"]}")
                    print(f"Superficie: {pais["superficie"]} km²")
                    print(f"Contienente: {pais["continente"]}\n")
                    print("-"*30)
            case _:
                print("La opción ingresada es incorrecta")

def ordenar_por_poblacion():
    opcion= questionary.select(
        message="Selecciona: ",
        choices=["1. Ordenar de manera ascendente",
"2. Ordenar de manera descendente"]
    ).ask()
    with open("paises.csv","r",newline="",encoding="utf-8-sig") as archivo:
        lector=csv.DictReader(archivo)
        paises=list(lector)
        match opcion:
            case "1. Ordenar de manera ascendente":
                paises_ordenados = sorted(paises, key=lambda pais: int(pais["poblacion"]))
                for pais in paises_ordenados:
                    print(f"\nPais: {pais["nombre"]}")
                    print(f"Población: {pais["poblacion"]}\n")
                    print("-"*30)
            case "2. Ordenar de manera descendente":
                paises_ordenados = sorted(paises, key=lambda pais: int(pais["poblacion"]),reverse=True)
                for pais in paises_ordenados:
                    print(f"\nPais: {pais["nombre"]}")
                    print(f"Población: {pais["poblacion"]}\n")
                    print("-"*30)
            case _:
                print("La opción ingresada es incorrecta")

def ordenar_por_superficie():
    opcion= questionary.select(
        message="Selecciona: ",
        choices=["1. Ordenar de manera ascendente",
"2. Ordenar de manera descendente"]
    ).ask()
    with open("paises.csv","r",newline="",encoding="utf-8-sig") as archivo:
        lector=csv.DictReader(archivo)
        paises=list(lector)
        match opcion:
            case "1. Ordenar de manera ascendente":
                paises_ordenados = sorted(paises, key=lambda pais: int(pais["superficie"]))
                for pais in paises_ordenados:
                    print(f"\nPais: {pais["nombre"]}")
                    print(f"Superficie: {pais["superficie"]} km²\n")
                    print("-"*30)
            case "2. Ordenar de manera descendente":
                paises_ordenados = sorted(paises, key=lambda pais: int(pais["superficie"]),reverse=True)
                for pais in paises_ordenados:
                    print(f"\nPais: {pais["nombre"]}")
                    print(f"Superficie: {pais["superficie"]} km²\n")
                    print("-"*30)
            case _:
                print("La opción ingresada es incorrecta")