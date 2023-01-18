def crear_juego_parametros(name, platform, year, genre, publisher, na_sales=0,
                           eu_sales=0, jp_sales=0, other_sales=0,
                           global_sales=0):
    return {"name": name, "platform": platform, "year": year, "genre": genre,
            "publisher": publisher, "na_sales": na_sales, "eu_sales": eu_sales,
            "jp_sales": jp_sales, "other_sales": other_sales,
            "global_sales": global_sales}


def crear_juego(lista_parametros):
    if len(lista_parametros) == 10:
        if lista_parametros[2] == "N/A":
            lista_parametros[2] = 1899
        return crear_juego_parametros(lista_parametros[0],
                                      lista_parametros[1],
                                      int(lista_parametros[2]),
                                      lista_parametros[3],
                                      lista_parametros[4],
                                      float(lista_parametros[5]),
                                      float(lista_parametros[6]),
                                      float(lista_parametros[7]),
                                      float(lista_parametros[8]),
                                      float(lista_parametros[9]))
    elif len(lista_parametros) == 5:
        return crear_juego_parametros(lista_parametros[0],
                                      lista_parametros[1],
                                      int(lista_parametros[2]),
                                      lista_parametros[3],
                                      lista_parametros[4])
