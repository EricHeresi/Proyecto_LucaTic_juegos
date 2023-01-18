def menu_principal():
    print("--------------------------------------------------------")
    print("MENU")
    print("0. Salir")
    print("1. Dar un juego de alta")
    print("2. Listar juegos de género plataformas")
    print("3. Listar todos los juegos")
    print("4. Listar juegos para consolas de Nintendo")
    print("5. Listar editores")
    print("6. Listar los 5 juegos más vendidos del mundo")
    print("7. Listar juegos del siglo XX")
    print("8. Editar un juego")
    print("9. Borrar un juegos")
    print("10. Listar todos los juegos")
    print("11. Listar juegos por género")
    print("12. Listar juegos con ventas por encima de la media")
    print("13. Listar juegos lanzados en años pares")


def pedir_opcion():
    opcion = False
    while (not opcion):
        try:
            numero = int(input("Seleccione una opcion: "))
        except ValueError:
            print("No es una opción correcta")
        else:
            if numero < 0 or numero > 13:
                print("No es un numero dentro del rango válido")
            else:
                opcion = True
    return numero
