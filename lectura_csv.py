import csv


# La función lee un archivo csv y retorna una lista
def lectura_csv(archivo):
    lista_aux = []
    try:
        csvfile = archivo
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


def escritura_csv(lista_dict):
    with open("lista_aux.csv", 'w', newline="") as output_file:
        if len(lista_dict) > 0:
            keys = lista_dict[0].keys()
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(lista_dict)
            output_file.close()
        else:
            escritor = csv.writer(output_file)
            escritor.writerow([])
            output_file.close()
