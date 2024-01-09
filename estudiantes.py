import json

def cargarEstudiantes():

    # TRAE ESTUDIANTES DEL ARCHIVO .JSON

    file = open("estudiantes.json")

    estudiantes = json.load(file)

    return estudiantes
    


def traerCampersInscritos():

    estudiantes = cargarEstudiantes()

    estudiantesInscritos = []

    for estudiante in estudiantes:

        if estudiante["estado"].lower() == "inscrito":

            estudiantesInscritos.append(estudiante)            
    
    return estudiantesInscritos


def crearNuevoEstudiante():

    estudiantes = cargarEstudiantes()
    nuevoEstudiante = {}

    nuevoEstudiante["identificacion"] = input("Ingrese la identificacion del estudiante: ")
    nuevoEstudiante["nombres"] = input("Ingrese los nombres del estudiante: ")
    nuevoEstudiante["apellidos"] = input("Ingrese los apellidos del estudiante: ")
    nuevoEstudiante["direccion"] = input("Ingrese la dirección del estudiante: ")
    nuevoEstudiante["telefonoCelular"] = int(input("Ingrese el número de celular: "))
    nuevoEstudiante["estado"] = "inscrito"

    estudiantes.append(nuevoEstudiante)


    file = "estudiantes.json"

    with open(file, "w") as file:

        # AGREGAR NUEVO DATO
        
        json.dump(estudiantes, file)
    
        # AGREGAR NUEVO DATO
        

def registroPrueba():


    estudiantes = cargarEstudiantes()

    for estudiante in estudiantes:

        if estudiante["estado"].lower() == "inscrito":

            print("{} Usted puede presentar la prueba ya que su estado es {}".format(estudiante["nombres"], estudiante["estado"]))

            notaTeorica = int(input("Cuál es el resultado de su nota teorica: "))
            notaPractica = int(input("Cuál es el resultado de su nota practica: "))

            promedio = (notaPractica + notaTeorica) / 2

            if promedio >= 60:

                estudiante["estado"] = "Aprobado"

                print("Usted logró superar el promedio de la prueba con un {}".format(promedio))

            else:

                estudiante["estado"] = "Reprobado"

                print("Usted no logró superar el promedio su nota fue {} ".format(promedio))

    
    file ="estudiantes.json"

    with open(file, "w") as file:

        
        json.dump(estudiantes, file)


def traerCampersAprobados():

    estudiantes = cargarEstudiantes()

    campersAprobados = []

    for estudiante in estudiantes:

        if estudiante["estado"].lower() == "aprobado":

            campersAprobados.append(estudiante)

    return campersAprobados

def obtenerEstudiantePorIdentificacion(identificacionEstudiante):

    estudiantes = cargarEstudiantes()

    for estudiante in estudiantes:

        if estudiante["identificacion"] == identificacionEstudiante:

            return estudiante