def menu_principal():
    print("--------------------------------------------------------")
    print("MENU")
    print("1. Dar un juego de alta")
    print("2. Listar juegos de género: plataformas")
    print("3. Listar todos los juegos")
    print("4. Listar juegos para consolas de Nintendo")
    print("5. Listar editores")
    print("6. Listar los 5 juegos más vendidos del mundo")
    print("7. Listar juegos del siglo XX")
    print("8. Editar un juego")
    print("9. Borrar un juego")
    print("10. Listar juegos por género")
    print("11. Listar juegos con ventas por encima de la media")
    print("12. Listar juegos lanzados en años pares")
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


def menu_nintendo():
    print("--------------------------------------------------------")
    print("MENU NINTENDO")
    print("1. Listar juegos publicados por Nintendo")
    print("2. Listar juegos para consolas de Nintendo")
    print()
    print("0. Volver")
    print("--------------------------------------------------------")


def pedir_opcion_nintendo():
    opcion = False
    while (not opcion):
        try:
            numero = int(input("Seleccione una opcion: "))
        except ValueError:
            print("No es una opción correcta")
        else:
            if numero < 0 or numero > 2:
                print("No es un numero dentro del rango válido")
            else:
                opcion = True
    return numero


def ask_region(lista_region):
    region_ok = False
    while not region_ok:
        try:
            region = (input("Escribe de que region obtener datos: ")).lower()
            assert region in lista_region
        except AssertionError:
            print(lista_region)
            print("No es una de las regiones validas")
        else:
            region_ok = True
    return region


def pedir_region():
    region = ask_region(["na", "eu", "jp", "other"])
    if region == "na":
        region_key = "na_sales"
    if region == "eu":
        region_key = "eu_sales"
    if region == "jp":
        region_key = "jp_sales"
    if region == "other":
        region_key = "other_sales"
    return region_key


def pedir_juego(set_plataformas):
    nombre = ask_name()
    plataforma = ask_platform(set_plataformas)
    return nombre, plataforma


def ask_sales():
    sales_ok = False
    while not sales_ok:
        try:
            sales = float(input("Introduce el numero de ventas(millones): "))
            assert sales >= 0.0, "Los valores negtivos nos son validos"
        except ValueError:
            print("No es un valor numerico")
        except AssertionError as e:
            print(e)
        else:
            sales_ok = True
    return sales


def pedir_cambios(set_generos, set_editores):
    new_dict = dict({})
    yes = (input("Escribe [Y] para cambiar el año: ")).lower()
    if yes == "y":
        new_year = ask_year()
        new_dict["year"] = new_year
    yes = (input("Escribe [Y] para cambiar el genero: ")).lower()
    if yes == "y":
        new_genre = ask_genre(set_generos)
        new_dict["genre"] = new_genre
    yes = (input("Escribe [Y] para cambiar el editor: ")).lower()
    if yes == "y":
        new_publisher = ask_publisher(set_editores)
        new_dict["publisher"] = new_publisher
    yes = (input("Escribe [Y] para cambiar las ventas en NA: ")).lower()
    if yes == "y":
        new_na = ask_sales()
        new_dict["na_sales"] = new_na
    yes = (input("Escribe [Y] para cambiar las ventas en EU: ")).lower()
    if yes == "y":
        new_eu = ask_sales()
        new_dict["eu_sales"] = new_eu
    yes = (input("Escribe [Y] para cambiar las ventas en JP: ")).lower()
    if yes == "y":
        new_jp = ask_sales()
        new_dict["jp_sales"] = new_jp
        yes = (input("Escribe [Y] para cambiar las otras ventas: ")).lower()
    if yes == "y":
        new_other = ask_sales()
        new_dict["other_sales"] = new_other
    return new_dict


def pedir_confirmacion_cambios(juego_original, cambios):
    print("Del juego original:")
    print(juego_original)
    print("Se van a modificar los siguientes campos:")
    print(cambios)
    yes = (input("Confirmar la operacion? [Y]: ")).lower()
    if yes == "y" or yes == "yes":
        return True
    else:
        return False


def pedir_confirmacion_eliminar(juego_eliminar):
    print("Se va a eliminar este juego del sistema:")
    print(juego_eliminar)
    yes = (input("Confirmar la operacion? [Y]: ")).lower()
    if yes == "y" or yes == "yes":
        return True
    else:
        return False
