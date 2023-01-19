def menu_principal():
    print("--------------------------------------------------------")
    print("MENU")
    print("1. Dar un juego de alta")
    print("2. Listar juegos de género: plataformas")
    print("3. Listar todos los juegos")
    """
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
    """
    print()
    print("0. Salir")
    print("--------------------------------------------------------")


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


def ask_year():
    year_ok = False
    while not year_ok:
        try:
            year = int(input("Escribe cuando salio el juego(year): "))
            assert year < 2024 and year > 1957, "No se trata de numero valido"
        except ValueError:
            print("No es un año")
        except AssertionError as e:
            print(e)
        else:
            year_ok = True
    return year


def ask_name():
    name_ok = False
    while not name_ok:
        try:
            name = input("Escribe el nombre del juego: ")
            assert name != ""
            assert not name.isspace()
        except AssertionError:
            print("No es un nombre de juego valido")
        else:
            name_ok = True
    return name


def ask_platform(set_plataformas):
    platform_ok = False
    while not platform_ok:
        try:
            platform = input("Escribe la plataforma del juego: ")
            assert platform in set_plataformas
        except AssertionError:
            print("No es una de las plataformas validas")
            print(set_plataformas)
        else:
            platform_ok = True
    return platform


def ask_genre(set_generos):
    genre_ok = False
    while not genre_ok:
        try:
            genre = input("Escribe el genero del juego: ")
            assert genre in set_generos
        except AssertionError:
            print("No es uno de los generos validos")
            print(set_generos)
        else:
            genre_ok = True
    return genre


def ask_publisher(set_editores):
    publisher_ok = False
    while not publisher_ok:
        try:
            publisher = input("Escribe el editor del juego: ")
            assert publisher in set_editores
        except AssertionError:
            print(set_editores)
            print("No es uno de los editores validos(scroll arriba para ver" +
                  " editores validos)")
        else:
            publisher_ok = True
    return publisher


def pedir_parametros_juego(set_plataformas, set_generos, set_editores):
    lista_aux = []
    lista_aux.append(ask_name())
    lista_aux.append(ask_platform(set_plataformas))
    lista_aux.append(ask_year())
    lista_aux.append(ask_genre(set_generos))
    lista_aux.append(ask_publisher(set_editores))
    return lista_aux


def ask_region(lista_region):
    publisher_ok = False
    while not publisher_ok:
        try:
            publisher = input("Escribe la region de la que obtener datos: ")
            assert publisher in lista_region
        except AssertionError:
            print(lista_region)
            print("No es una de las regiones validas")
        else:
            publisher_ok = True
    return publisher


def pedir_region():
    return ask_region(["na_sales", "eu_sales", "jp_sales", "other_sales"])
