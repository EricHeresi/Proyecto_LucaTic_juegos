import ListaJuegos as lj
import menu


def ejecutar_insercion(lista):
    parametros = menu.pedir_parametros_juego(lista.get_plataformas(),
                                             lista.get_generos(),
                                             lista.get_editores())
    existe_juego = lista.existe(parametros[0], parametros[1])
    assert not existe_juego[0], "ERROR: Ya existe ese juego en esa plataforma"
    lista.insercion_juego(parametros)
    print("Insercion completada")


def ejecuta_opcion(opcion, lista):
    try:
        if opcion == 1:
            ejecutar_insercion(lista)
        if opcion == 2:
            lista.filtrar_genero("Platform")
        if opcion == 3:
            lista.mostrar_lista()
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
        ejecuta_opcion(opcion, lista_juegos)
        menu.menu_principal()
        opcion = menu.pedir_opcion()


main()
