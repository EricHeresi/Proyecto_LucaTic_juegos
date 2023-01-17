def crear_juego(name, platform, year, genre, publisher, na_sales=0, eu_sales=0,
                jp_sales=0, other_sales=0, global_sales=0):
    return {"name": name, "platform": platform, "year": year, "genre": genre,
            "publisher": publisher, "na_sales": na_sales, "eu_sales": eu_sales,
            "jp_sales": jp_sales, "other_sales": other_sales,
            "global_sales": global_sales}
