import csv
import os.path


def lectura_csv():
    print(os.path.isfile("vgsales.csv"))
    with open('vgsales.csv') as file:
        print("leido")
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)


lectura_csv()
