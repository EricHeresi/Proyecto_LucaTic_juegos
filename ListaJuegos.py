import lectura_csv
import juego


class ListaJuegos:
    def __init__(self):
        self.lista = []

    def insercion_juego(self, lista_aux):
        self.lista.append(juego.crear_juego(lista_aux))

    def carga_datos(self):
        lista_completa = lectura_csv.lectura_csv()
        for linea in lista_completa[1:]:
            self.insercion_juego(linea[1:])

    def filtrar_genero(self, genero):
        for elemento in self.lista:
            if elemento["genre"] == genero:
                print(juego.format_juego(elemento))

    def mostrar_lista(self):
        for elemento in self.lista:
            print(juego.format_juego(elemento))
