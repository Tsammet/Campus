import json
from rutas import agregarModulo, obtenerRutaPorIdentificador
from estudiantes import obtenerEstudiantePorIdentificacion


def cargarNotas():

    file = open("notas.json")

    notas = json.load(file)

    return notas


def cargarModulo():

    file = open("modulos.json")

    modulo = json.load(file)

    return modulo


def crearModulo():
    
    modulos = cargarModulo()

    modulo = {}

    modulo["identificador"] = input("¿Cuál es el identificador del modulo?: ")
    modulo["nombre"] = input("¿Cuál es el nombre del modulo?: ")
    modulo["ruta"] = input("¿Cuál es la ruta a la que pertenece?: ")

    modulos.append(modulo)

    
    file = "modulos.json"

    with open(file, "w") as fileModulo:

        # AGREGAR NUEVO DATO
        
        json.dump(modulos, fileModulo)
    
        # AGREGAR NUEVO DATO

    agregarModulo(modulo["ruta"], modulo["identificador"])


def asignarNotaModulo():

    identificadorModulo = input("Que modulo desea asignar nota: ")

    modulos = cargarModulo()
    notas = cargarNotas()

    for modulo in modulos:

        if identificadorModulo == modulo["identificador"]:
        
            ruta = obtenerRutaPorIdentificador(modulo["ruta"])


            for id_estudiante in ruta["estudiantes"]:

                nota = {}
        
                notaTeorica = float(input("Cuál es la nota teorica del estudiante {} :".format(id_estudiante)))
                notaPractica = float(input("Cuál es la nota practica del estudiante {} :".format(id_estudiante)))
                promedioQuizzes = float(input("Cuál es el promedio de los quizzes del estudiante {} :".format(id_estudiante)))

                res = (notaTeorica * 0.3) + (notaPractica * 0.6) + (promedioQuizzes * 0.1)

                if res >= 60:
                    nota["estado"] = "aprobado"

                else:
                    nota["estado"] = "rendimiento bajo"


                nota["estudiante"] = id_estudiante
                nota["modulo"] = modulo["identificador"]
                nota["notaTeorica"] = notaTeorica            
                nota["notaPractica"] = notaPractica        
                nota["notaQuizzes"] = promedioQuizzes        

                notas.append(nota)    


    file = "notas.json"

    with open(file, "w") as fileNota:

        # AGREGAR NUEVO DATO
        
        json.dump(notas, fileNota)
    
        # AGREGAR NUEVO DATO



def ObtenerEstudianteRendimientoBajo():

    notas = cargarNotas()

    estudiantesConRendimientoBajo = []

    for nota in notas:

        if nota["estado"] == "rendimiento bajo":

            estudiante = obtenerEstudiantePorIdentificacion(nota["estudiante"])

            estudiantesConRendimientoBajo.append(estudiante)

    return estudiantesConRendimientoBajo