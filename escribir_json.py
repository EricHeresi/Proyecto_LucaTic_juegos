import json


def escritura_json(lista_dicts):
    json_string = json.dumps(lista_dicts)
    json_file = open("data.json", "w")
    json_file.write(json_string)
    json_file.close()
