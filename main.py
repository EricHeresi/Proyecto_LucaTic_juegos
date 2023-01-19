import ListaJuegos as lj
import menu
import os


def ejecutar_insercion(lista):
    parametros = menu.pedir_parametros_juego(lista.get_plataformas(),
                                             lista.get_generos(),
                                             lista.get_editores())
    existe_juego = lista.existe(parametros[0], parametros[1])
    assert not existe_juego[0], "ERROR: Ya existe ese juego en esa plataforma"
    lista.insercion_juego(parametros)
    print("Insercion completada")


def ejecutar_editar_juego(lista):
    nombre, plataforma = menu.pedir_juego(lista.get_plataformas())
    existe, dict_juego = lista.existe(nombre, plataforma)
    if existe:
        cambios = menu.pedir_cambios(lista.get_generos(),
                                     lista.get_editores())
        if menu.pedir_confirmacion_cambios(dict_juego, cambios):
            dict_juego.update(cambios)
            print("...")
            print("Se han guardado los cambios")
            print("Nuevo juego:")
            print(dict_juego)
        else:
            print()
            print("No se ha realizado ningun cambio en el sistema")
    else:
        print()
        print("No existe el juego", nombre, "para la plataforma", plataforma)


def ejecuta_opcion(opcion, lista):
    try:
        if opcion == 1:
            ejecutar_insercion(lista)
        if opcion == 2:
            lista.filtrar_genero("Platform")
        if opcion == 3:
            lista.mostrar_lista()
        if opcion == 4:
            menu.menu_nintendo()
            opcionNintendo = menu.pedir_opcion_nintendo()
            if opcionNintendo == 1:
                lista.filtrar_publisher("Nintendo")
            if opcionNintendo == 2:
                lista.filtrar_consolas_nintendo()
            if opcionNintendo == 0:
                print("\nVolviendo al menú principal.\n")
        if opcion == 5:
            lista.print_editores()
        if opcion == 6:
            lista.region_best_five(menu.pedir_region())
        if opcion == 7:
            lista.filtrar_year_between(1900, 2001)
        if opcion == 8:
            ejecutar_editar_juego(lista)
        if opcion == 9:
            pass
        if opcion == 10:
            print(lista.get_generos())
            lista.filtrar_genero(menu.ask_genre(lista.get_generos()))
        if opcion == 11:
            lista.filtrar_encima_europa(lista.obtener_media_europa())
        if opcion == 12:
            lista.filtrar_years_pares()
    except AssertionError as e:
        print(e)


def main():
    lista_juegos = lj.ListaJuegos()
    try:
        lista_juegos.carga_datos()
    except AssertionError as e:
        print(e)
    menu.menu_principal()
    opcion = menu.pedir_opcion()
    while (opcion != 0):
        os.system("clear")
        ejecuta_opcion(opcion, lista_juegos)
        menu.menu_principal()
        opcion = menu.pedir_opcion()
    os.system("clear")
    lista_juegos.guardar_juegos_nuevos()


main()
