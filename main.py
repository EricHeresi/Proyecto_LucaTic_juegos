import ListaJuegos as lj
import menu


def ejecuta_opcion(opcion, lista):
    if opcion == 3:
        lista.mostrar_lista()


def main():
    lista_juegos = lj.ListaJuegos()
    lista_juegos.carga_datos()
    menu.menu_principal()
    opcion = menu.pedir_opcion()
    ejecuta_opcion(opcion, lista_juegos)


main()
