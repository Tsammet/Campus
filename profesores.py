import json

def cargarProfesores():

    # TRAE PROFESORES DEL ARCHIVO JSON

    file = open("profesores.json")

    profesores = json.load(file)

    return profesores


def ingresarNuevoProfesor():

    profesores = cargarProfesores()

    nuevoProfesor = {}

    nuevoProfesor["identificacion"] = input("Ingrese la identificación del profesor: ")
    nuevoProfesor["nombre"] = input("Ingrese el nombre del profesor: ")
    nuevoProfesor["horario"] = {
        "maniana": "disponible",
        "tarde": "disponible",
        "noche": "disponible"
    }

    profesores.append(nuevoProfesor)


    file = "profesores.json"

    with open(file, "w") as file:

        # AGREGAR NUEVO DATO
        
        json.dump(profesores, file)
    
        # AGREGAR NUEVO DATO
        