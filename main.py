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
    print("Se ha insertado en el sistema el juego:")
    print(parametros)
    print("Insercion completada")


def ejecutar_editar_juego(lista):
    nombre, plataforma = menu.pedir_juego(lista.get_plataformas())
    existe, dict_juego = lista.existe(nombre, plataforma)
    if existe:
        cambios = menu.pedir_cambios(lista.get_generos(),
                                     lista.get_editores())
        if menu.pedir_confirmacion_cambios(dict_juego, cambios):
            lista.update_juego(nombre, plataforma, cambios)
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


def ejecutar_eliminar(lista):
    nombre, plataforma = menu.pedir_juego(lista.get_plataformas())
    existe, dict_juego = lista.existe(nombre, plataforma)
    if existe:
        if menu.pedir_confirmacion_eliminar(dict_juego):
            lista.eliminar_juego(dict_juego)
            print("...")
            print("Se ha eliminado", nombre, "con exito")
        else:
            print()
            print("Operacion abortada")
    else:
        print()
        print("No existe el juego", nombre, "para la plataforma", plataforma)


def ejecuta_opcion(opcion, lista):
    try:
        if opcion == 1:
            menu.menu_edicion()
            opcionEdicion = menu.pedir_opcion_edicion()
            if opcionEdicion == 1:
                ejecutar_insercion(lista)
            if opcionEdicion == 2:
                ejecutar_editar_juego(lista)
            if opcionEdicion == 3:
                ejecutar_eliminar(lista)
            if opcionEdicion == 4:
                lista.escribir_lista_json()
            if opcionEdicion == 0:
                os.system("clear")
        if opcion == 2:
            menu.menu_informe()
            opcionInforme = menu.pedir_opcion_informe()
            if opcionInforme == 1:
                lista.filtrar_genero("Platform")
            if opcionInforme == 2:
                lista.mostrar_lista()
            if opcionInforme == 3:
                menu.menu_nintendo()
                opcionNintendo = menu.pedir_opcion_nintendo()
                if opcionNintendo == 1:
                    lista.filtrar_publisher("Nintendo")
                if opcionNintendo == 2:
                    lista.filtrar_consolas_nintendo()
                if opcionNintendo == 0:
                    print("\nVolviendo al men?? principal.\n")
            if opcionInforme == 4:
                lista.print_editores()
            if opcionInforme == 5:
                lista.region_best_five(menu.pedir_region())
            if opcionInforme == 6:
                lista.filtrar_year_between(1900, 2001)
            if opcionInforme == 7:
                print(lista.get_generos())
                lista.filtrar_genero(menu.ask_genre(lista.get_generos()))
            if opcionInforme == 8:
                lista.filtrar_encima_europa(lista.obtener_media_europa())
            if opcionInforme == 9:
                lista.filtrar_years_pares()
            if opcionInforme == 0:
                os.system("clear")
    except AssertionError as e:
        print(e)


def main():
    lista_juegos = lj.ListaJuegos()
    try:
        lista_juegos.carga_datos()
        lista_juegos.carga_datos_agregados()
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
