from funciones import*
from funciones2 import*

escribir_csv(paises)

while True:
    mostrar_menu()
    opcion=input("Ingrese una opción: ")
    try:
        match(opcion):
            case "1":
                pass
            case "2":
                pass
            case "3":
                buscar_pais()
            case "4":
                while True:
                    filtrar_menu()
                    opcion=input("Ingrese una opcion: ")
                    match(opcion):
                        case "1":
                            filtrar_pais_continente()
                        case "2":
                            filtrar_por_población()
                        case "3":
                            filtrar_por_superficie()
                        case "4":
                            print("Volviendo al menú principal")
                            break
                        case _:
                            print("La opción ingresada es incorrecta")
            case "5":
                while True:
                    ordenar_menu()
                    opcion=input("Ingrese una opcion: ")
                    match(opcion):
                        case "1":
                            ordenar_por_pais()
                        case "2":
                            ordenar_por_poblacion()
                        case "3":
                            ordenar_por_superficie()
                        case "4":
                            print("Volviendo al menú principal")
                            break
                        case _:
                            print("La opción ingresada es incorrecta")
            case "6":
                while True:
                    estadistica_menu()
                    opcion=input("Ingrese una opcion: ")
                    match(opcion):
                        case "1":
                            pass
                        case "2":
                            pass
                        case "3":
                            pass
                        case "4":
                            pass
                        case "5":
                            print("Volviendo al menú principal")
                            break
                        case _:
                            print("La opción ingresada es incorrecta")
            case "7":
                print("Hasta luego!")
                break
            case _:
                print("La opción ingresada es incorrecta")
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