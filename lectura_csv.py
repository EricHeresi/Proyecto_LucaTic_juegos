import csv


def lectura_csv():
    file = open('vgsales.csv')
    print("leido")
    csv_reader = csv.reader(file)
    file.close()
    return csv_reader
