from funciones import*

while True:
    mostrar_menu()
    opcion=input("Ingrese una opción: ")

    match(opcion):
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            while True:
                filtrar_menu()
                opcion=input("Ingrese una opcion: ")
                match(opcion):
                    case "1":
                        pass
                    case "2":
                        pass
                    case "3":
                        pass
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
                        pass
                    case "2":
                        pass
                    case "3":
                        pass
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