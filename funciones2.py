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
    try:
        with open("paises.csv","r",newline="",encoding="utf-8-sig") as archivo:
            #Cada fila la representa como un diccionario
            lector=csv.DictReader(archivo)
            encontrado=False
            for fila in lector:
                #verifico sila cadena de caracteres ingresado en pais_buscado esta contenido en el nombre del país
                if pais_buscado in normalizar(fila["nombre"].lower()):
                    print(f"Pais: {fila["nombre"]}")
                    print(f"Población: {fila["poblacion"]}")
                    print(f"Superficie: {fila["superficie"]}")
                    print(f"Contienente: {fila["continente"]}\n")
                    encontrado=True
            if not encontrado:
                raise ValueError("El país ingresado no existe en el registro")
    except FileNotFoundError:
        print("Error: No se encontró el archivo paises.csv")
    except KeyError:
        print("Error: el archivo no contiene las columnas esperadas")
    except PermissionError:
        print("Error: El archivo esta siendo utilizado en otro programa")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: ocurrió un error inesperado {e}")