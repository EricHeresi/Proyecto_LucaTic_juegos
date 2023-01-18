import ListaJuegos as lj
import menu


def ejecuta_opcion(opcion, lista):
    if opcion == 1:
        lista_parametros = menu.pedir_parametros_juego()
        lista.insercion_juego(lista_parametros)
        print("Insercion completada")
    if opcion == 2:
        lista.filtrar_genero("Platform")
    if opcion == 3:
        lista.mostrar_lista()


def main():
    lista_juegos = lj.ListaJuegos()
    lista_juegos.carga_datos()
    menu.menu_principal()
    opcion = menu.pedir_opcion()
    while (opcion != 0):
        ejecuta_opcion(opcion, lista_juegos)
        menu.menu_principal()
        opcion = menu.pedir_opcion()


main()
