import csv


def lectura_csv():

    try:
        csvfile = "vgsales.csv"
        file = open(csvfile)
        print("leido")
        csv_reader = csv.reader(file)
        file.close()
        return csv_reader
    except FileNotFoundError:
        print("Error, no se encuentra el fichero", csvfile)
    except Exception:
        print("Error desconocido")
