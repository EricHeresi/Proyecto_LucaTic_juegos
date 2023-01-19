import unittest
import lectura_csv
import menu
import juego
import ListaJuegos as lj


class TestProyecto(unittest.TestCase):

    def test_pedir_opcion(self):
        valor = menu.pedir_opcion()
        self.assertEqual(type(valor), int)
        self.assertTrue(valor > 0)
        self.assertTrue(valor < 13)

    def test_ask_name(self):
        valor = menu.ask_name()
        self.assertEqual(type(valor), str)
        self.assertTrue(len(valor) > 0)

    def test_ask_platform(self):
        valor = menu.ask_platform({'Wii'})
        self.assertEqual(type(valor), str)
        self.assertTrue(len(valor) > 0)

    def test_lectura_csv(self):
        self.assertEqual(type(lectura_csv.lectura_csv()), type(list()))
        self.assertEqual(type(lectura_csv.lectura_csv()[0]),
                         type(list()))

    def test_ask_year(self):
        valor = menu.ask_year()
        self.assertEqual(type(valor), int)
        self.assertTrue(valor > 1957)
        self.assertTrue(valor < 2024)

    def test_insert_lista(self):
        lista = lj.ListaJuegos()
        dicti = {"name": "Wii Sports", "platform": "Wii", "year": 2000,
                 "genre": "Platform", "publisher": "Nintendo",
                 "na_sales": 0, "eu_sales": 0, "jp_sales": 0,
                 "other_sales": 0, "global_sales": 0}
        juego = ["Wii Sports", "Wii", "2000", "Platform", "Nintendo"]
        lista.insercion_juego(juego)
        self.assertEqual(lista.lista[0], dicti)

    def test_crear_juego(self):
        dicti = {"name": "Wii Sports", "platform": "Wii", "year": 2000,
                 "genre": "Platform", "publisher": "Nintendo",
                 "na_sales": 0, "eu_sales": 0, "jp_sales": 0,
                 "other_sales": 0, "global_sales": 0}
        params = ["Wii Sports", "Wii", "2000", "Platform", "Nintendo"]
        self.assertEqual(juego.crear_juego(params), dicti)
        self.assertEqual(type(juego.crear_juego(params)), dict)

    def test_crear_juego_parametros(self):
        dicti = {"name": "Wii Sports", "platform": "Wii", "year": 2000,
                 "genre": "Platform", "publisher": "Nintendo",
                 "na_sales": 0, "eu_sales": 0, "jp_sales": 0,
                 "other_sales": 0, "global_sales": 0}
        self.assertEqual(juego.crear_juego_parametros(
            "Wii Sports", "Wii", 2000, "Platform", "Nintendo",
            0, 0, 0, 0, 0
        ), dicti)
        self.assertEqual(juego.crear_juego_parametros(
            "Wii Sports", "Wii", 2000, "Platform", "Nintendo"
        ), dicti)
        self.assertEqual(type(juego.crear_juego_parametros(
            "Wii Sports", "Wii", 2000, "Platform", "Nintendo",
            0, 0, 0, 0, 0)), dict)

    def test_obtener_media_europa(self):
        lista = lj.ListaJuegos()
        self.assertEqual(type(lista.obtener_media_europa()), float)

    def test_get_editores(self):
        lista = lj.ListaJuegos()
        self.assertEqual(type(lista.get_editores()), set)

    def test_get_plataformas(self):
        lista = lj.ListaJuegos()
        self.assertEqual(type(lista.get_plataformas()), set)

    def test_get_generos(self):
        lista = lj.ListaJuegos()
        self.assertEqual(type(lista.get_generos()), set)

    def testexiste(self):
        lista = lj.ListaJuegos()
        self.assertEqual(type(lista.existe('Wii Sports', 'Platform')), tuple)


if __name__ == '__main__':
    unittest.main()
