import lectura_csv
import juego
import texttable as tt
from operator import itemgetter


class ListaJuegos:
    headers = ["Name", "Platform", "Year", "Genre", "Publiser",
               "NA Sales", "EU Sales", "JP Sales", "Other",
               "Global"]
    col_width = [35, 10, 4, 20, 40, 6, 6, 6, 6, 6]

    def __init__(self):
        self.lista = []
        self.lista_nuevos = []

    def insercion_juego(self, lista_aux):
        self.lista.append(juego.crear_juego(lista_aux))
        self.lista_nuevos.append(juego.crear_juego(lista_aux))

    def carga_datos(self):
        lista_completa = lectura_csv.lectura_csv()
        assert len(lista_completa) > 1, ("No se ha podido leer la cabecera "
                                         + " del fichero")
        for linea in lista_completa[1:]:
            try:
                self.lista.append(juego.crear_juego(linea[1:]))
            except ValueError:
                print("El orden de los datos leidos de un juego no se"
                      + " corresponde con los que admite el programa")
        assert len(self.lista) > 0, ("No se ha podido leer bien el formato "
                                     + "de todos los datos del fichero")

    def filtrar_genero(self, genero):
        lista_aux = []
        for elemento in self.lista:
            if elemento["genre"] == genero:
                lista_aux.append(elemento)
        assert len(lista_aux) > 0, ("No se han podido encontrar juegos "
                                    + "del genero " + genero)
        self.print_tabla(lista_aux)
        print("Se han encontrado", len(lista_aux),
              "juegos cuyo genero sea:", genero)

    def mostrar_lista(self):
        self.print_tabla(self.lista)

    def get_editores(self):
        set_editores = set({})
        for elemento in self.lista:
            set_editores.add(elemento["publisher"])
        return set_editores

    def get_plataformas(self):
        set_plataformas = set({})
        for elemento in self.lista:
            set_plataformas.add(elemento["platform"])
        return set_plataformas

    def get_generos(self):
        set_generos = set({})
        for elemento in self.lista:
            set_generos.add(elemento["genre"])
        return set_generos

    def existe(self, name, platfrm):
        try:
            game = next(item for item in self.lista if (item["name"] == name
                                                        and item["platform"]
                                                        == platfrm))
        except StopIteration:
            existe = False
            game = {}
        else:
            existe = True
        return existe, game

    def guardar_juegos_nuevos(self):
        pass

    def region_best_five(self, region):
        lista_aux = sorted(self.lista, key=itemgetter(region), reverse=True)
        self.print_tabla(lista_aux)

    def print_editores(self):
        set_editores = self.get_editores()
        for editor in set_editores:
            print(editor)

    def print_tabla(self, lista):
        tabla = tt.Texttable()
        tabla.add_row(self.headers)
        for elemento in lista:
            tabla.add_row(elemento.values())
        tabla.set_cols_width(self.col_width)
        print(tabla.draw())

    def filtrar_year_between(self, year_min, year_max):
        lista_aux = []
        for elemento in self.lista:
            if (elemento["year"] > year_min and elemento["year"] < year_max):
                lista_aux.append(elemento)
        assert len(lista_aux) > 0, ("No se han podido encontrar juegos "
                                    + "del siglo 20")
        self.print_tabla(lista_aux)
