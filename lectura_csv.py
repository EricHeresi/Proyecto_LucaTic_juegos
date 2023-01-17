import csv


def lectura_csv():
    with open('vgsales.csv') as file:
        print("leido")
        csv_reader = csv.reader(file)
        return csv_reader
