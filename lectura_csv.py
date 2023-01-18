import csv


# La función lee un archivo csv y retorna una lista
def lectura_csv():
    lista_aux = []
    try:
        csvfile = "vgsales.csv"
        file = open(csvfile)
        csv_reader = csv.reader(file)
        for elemento in csv_reader:
            lista_aux.append(elemento)
        file.close()
    except FileNotFoundError:
        print("Error, no se encuentra el fichero", csvfile)
    except Exception:
        print("Error desconocido")
    return lista_aux
