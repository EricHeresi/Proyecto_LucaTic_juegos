import lectura_csv
import juego


class ListaJuegos:
    def __init__(self):
        self.lista = []

    def insercion_juego(self, lista_aux):
        self.lista.append(juego.crear_juego(lista_aux))

    def carga_datos(self):
        lista_completa = lectura_csv.lectura_csv()
        assert len(lista_completa) > 1, ("No se ha podido leer la cabecera " +
                                         " del fichero")
        for linea in lista_completa[1:]:
            try:
                self.insercion_juego(linea[1:])
            except ValueError:
                print("El orden de los datos leidos de un juego no se" +
                      " corresponde con los que admite el programa")
        assert len(self.lista) > 0, ("No se ha podido leer bien el formato " +
                                     "de todos los datos del fichero")

    def filtrar_genero(self, genero):
        lista_aux = []
        for elemento in self.lista:
            if elemento["genre"] == genero:
                lista_aux.append(juego.format_juego(elemento))
        assert len(lista_aux) > 0, ("No se han podido encontrar juegos " +
                                    "del genero " + genero)
        self.mostrar_lista_aux(lista_aux)

    def mostrar_lista_aux(self, lista_aux):
        for elemento in lista_aux:
            print(elemento)

    def mostrar_lista(self):
        for elemento in self.lista:
            print(juego.format_juego(elemento))

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
                                                        and item["platform"] ==
                                                        platfrm))
        except StopIteration:
            existe = False
            game = {}
        else:
            existe = True
        return existe, game
