import json

def cargarMatriculas():

    file = open("matriculas.json")

    matriculas = json.load(file)

    return matriculas