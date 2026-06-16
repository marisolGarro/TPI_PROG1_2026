import csv
import os
from funciones import*
import unicodedata

def normalizar(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).lower()

def buscar_pais():
    pais_buscado=normalizar(input("Ingrese el país que desea buscar: "))
    
    with open("paises.csv","r",newline="",encoding="utf-8-sig") as archivo:
        #Cada fila la representa como un diccionario
        lector=csv.DictReader(archivo)
        encontrado=False
        for fila in lector:
            #verifico sila cadena de caracteres ingresado en pais_buscado esta contenido en el nombre del país
            if pais_buscado in normalizar(fila["nombre"]):
                print(f"Pais: {fila["nombre"]}")
                print(f"Población: {fila["poblacion"]}")
                print(f"Superficie: {fila["superficie"]}")
                print(f"Contienente: {fila["continente"]}\n")
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
                print(f"Superficie: {lista["superficie"]}")
                
                encontrado=True
        if not encontrado:
            raise ValueError("El país ingresado no existe en el registro")
            