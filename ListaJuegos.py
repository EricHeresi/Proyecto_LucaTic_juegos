import lectura_csv
import escribir_json
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
        lista_completa = lectura_csv.lectura_csv("vgsales.csv")
        assert len(lista_completa) > 1, ("No se ha podido leer la cabecera "
                                         + " del fichero principal")
        for linea in lista_completa[1:]:
            try:
                self.lista.append(juego.crear_juego(linea[1:]))
            except ValueError:
                print("El orden de los datos leidos de un juego no se"
                      + " corresponde con los que admite el programa")
        assert len(self.lista) > 0, ("No se ha podido leer bien el formato "
                                     + "de todos los datos del fichero")

    def carga_datos_agregados(self):
        fichero = "lista_aux.csv"
        lista_completa = lectura_csv.lectura_csv(fichero)
        assert len(lista_completa) > 1, ("No se han encontrado juegos extra "
                                         + "para cargar en", fichero)
        for linea in lista_completa[1:]:
            try:
                self.lista.append(juego.crear_juego(linea))
                self.lista_nuevos.append(juego.crear_juego(linea))
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

    def existe_en_nuevo(self, name, platfrm):
        try:
            game = next(gm for gm in self.lista_nuevos if (gm["name"] == name
                                                           and gm["platform"]
                                                           == platfrm))
        except StopIteration:
            existe = False
            game = {}
        else:
            existe = True
        return existe, game

    def guardar_juegos_nuevos(self):
        lectura_csv.escritura_csv(self.lista_nuevos)

    def filtrar_publisher(self, publisher):
        lista_aux = []
        for elemento in self.lista:
            if elemento["publisher"] == publisher:
                lista_aux.append(elemento)
        assert len(lista_aux) > 0, ("No se han podido encontrar juegos "
                                    + "del publisher " + publisher)
        self.print_tabla(lista_aux)
        print("Se han encontrado", len(lista_aux),
              "juegos publicados por:", publisher)

    def filtrar_consolas_nintendo(self):
        consolas_nintendo = ["Wii", "NES", "GB", "DS",
                             "SNES", "GBA", "3DS", "N64", "GC", "WiiU"]
        lista_aux = []
        for elemento in self.lista:
            if elemento["platform"] in consolas_nintendo:
                lista_aux.append(elemento)
        assert len(lista_aux) > 0, ("No se han podido encontrar juegos "
                                    + "de consolas de Nintendo.")
        self.print_tabla(lista_aux)
        print("Se han encontrado", len(lista_aux),
              "juegos para consolas de Nintendo.")

    def region_best_five(self, region):
        lista_aux = sorted(self.lista, key=itemgetter(region), reverse=True)
        self.print_tabla(lista_aux[0:5])

    def print_editores(self):
        set_editores = self.get_editores()
        for editor in set_editores:
            print(editor)

    def print_tabla(self, lista):
        tabla = tt.Texttable()
        tabla.add_row(self.headers)
        cont = 0
        iterador = 0
        salir = False
        while not salir:
            cont += 1
            tabla.add_row(lista[iterador].values())
            if cont == 50:
                tabla.set_cols_width(self.col_width)
                print(tabla.draw())
                print("Mostrando elementos", iterador-48, "-", iterador+1)
                tecla = (input("Presiona Q para salir: ")).lower()
                if tecla == "q":
                    salir = True
                else:
                    cont = 0
                    tabla = tt.Texttable()
                    tabla.add_row(self.headers)
            iterador += 1
            if iterador >= len(lista):
                salir = True
        if cont < 50:
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
        print("Se han encontrado", len(lista_aux),
              "juegos del siglo XX.")

    def filtrar_years_pares(self):
        lista_aux = []
        for elemento in self.lista:
            if (elemento["year"] % 2 == 0):
                lista_aux.append(elemento)
        assert len(lista_aux) > 0, ("No se han podido encontrar juegos "
                                    + "en años pares.")
        self.print_tabla(lista_aux)
        print("Se han encontrado", len(lista_aux),
              "juegos lanzados en años pares.")

    def obtener_media_europa(self):
        suma = 0
        for elemento in self.lista:
            suma += elemento["eu_sales"]
        if len(self.lista) > 0:
            media = suma/len(self.lista)
        else:
            media = 0.0
        return media

    def filtrar_encima_europa(self, media):
        lista_aux = []
        for elemento in self.lista:
            if (elemento["eu_sales"] > media):
                lista_aux.append(elemento)
        assert len(lista_aux) > 0, ("No se han podido encontrar juegos "
                                    + "con mayor media que la de europa")
        self.print_tabla(lista_aux)
        print("La media es de:", media)
        print("El numero de juegos con ventas "
              + "por encima de la media en EU es", len(lista_aux))

    def eliminar_juego(self, dict_juego):
        try:
            self.lista.remove(dict_juego)
            self.lista_nuevos.remove(dict_juego)
        except ValueError:
            pass

    def update_juego(self, nombre, plataforma, cambios):
        existe, juego = self.existe(nombre, plataforma)
        if existe:
            juego.update(cambios)
        existe, juego = self.existe_en_nuevo(nombre, plataforma)
        if existe:
            juego.update(cambios)

    def escribir_lista_json(self):
        escribir_json.escritura_json(self.lista)
