import csv


def lectura_csv():
    file = open('vgsales.csv')
    csv_reader = csv.reader(file)
    lista_aux = []
    for elemento in csv_reader:
        lista_aux.append(elemento)
    file.close()
    return lista_aux
