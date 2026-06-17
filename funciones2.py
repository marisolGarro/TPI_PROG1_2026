import csv
import os
from funciones import*
import unicodedata

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
    pais_buscado=normalizar(input("Ingrese el país que desea buscar: "))
    
    with open("paises.csv","r",newline="",encoding="utf-8-sig") as archivo:
        #Cada fila la representa como un diccionario
        lector=csv.DictReader(archivo)
        encontrado=False
        for fila in lector:
            #verifico sila cadena de caracteres ingresado en pais_buscado esta contenido en el nombre del país
            if pais_buscado in normalizar(fila["nombre"]):
                print(f"\nPais: {fila["nombre"]}")
                print(f"Población: {fila["poblacion"]}")
                print(f"Superficie: {fila["superficie"]}")
                print(f"Contienente: {fila["continente"]}\n")
                print("-"*30)
                encontrado=True
        if not encontrado:
            raise ValueError("El país ingresado no existe en el registro")
    
def filtrar_pais_continente():
    buscar_continente=normalizar(input(f"Ingrese el continente: "))
    with open("paises.csv","r",newline="",encoding="utf-8-sig") as archivo:
        lector=csv.DictReader(archivo)
        encontrado=False
        for lista in lector:
            if buscar_continente==normalizar(lista["continente"]):
                print(f"\nPais: {lista["nombre"]}")
                print(f"Población: {lista["poblacion"]}")
                print(f"Superficie: {lista["superficie"]}\n")  
                print("-"*30)
                encontrado=True
        if not encontrado:
            raise ValueError("El país ingresado no existe en el registro")

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
                print(f"Superficie: {fila["superficie"]}")
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
                print(f"Superficie: {fila["superficie"]}")
                print(f"Contienente: {fila["continente"]}\n")
                print("-"*30)
                encontrado=True
        if not encontrado:
            raise ValueError("No se encuentraron países en el rango de superficie ingresado")

def ordenar_por_pais():
    print("""
\n1)Ordenar nombres de paises de A -> Z
2)Ordenar nombres de paises de Z -> A
""")
    opcion=input("Ingrese la opción deseada: ")
    with open("paises.csv","r",newline="",encoding="utf-8-sig") as archivo:
        lector=csv.DictReader(archivo)
        match opcion:
            case "1":
                paises=list(lector)
                paises_ordenados = sorted(paises, key=lambda pais: normalizar(pais["nombre"]))
                for pais in paises_ordenados:
                    print(f"\nPais: {pais["nombre"]}")
                    print(f"Población: {pais["poblacion"]}")
                    print(f"Superficie: {pais["superficie"]}")
                    print(f"Contienente: {pais["continente"]}\n")
                    print("-"*30)
            case "2":
                pass
