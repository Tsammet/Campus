import json
from estudiantes import cargarEstudiantes
from profesores import cargarProfesores
from matriculas import cargarMatriculas
from datetime import datetime, timedelta

def cargarRutas():

    file = open("rutas.json")

    rutas = json.load(file)

    return rutas


def crearRuta():

    rutas = cargarRutas()

    nuevaRuta = {}

    nuevaRuta["identificador"] = input("Ingrese el identificador de la Ruta: ")
    nuevaRuta["nombre"] = input("Ingrese el nombre de la ruta: ")
    nuevaRuta["profesor"] = "No asignado"
    nuevaRuta["estudiantes"] = []
    nuevaRuta["estado"] = "No matriculado"
    nuevaRuta["horario"] = input("En que horario se da esta ruta\nmaniana / tarde / noche : ")
    nuevaRuta["areaEntrenamiento"] = input("Ingrese el area de entrenamiento \n Sputnik / Apolo / Artemis")
    nuevaRuta["modulos"] = []

    rutas.append(nuevaRuta)


    file = "rutas.json"

    with open(file, "w") as file:

        # AGREGAR NUEVO DATO
        
        json.dump(rutas, file)
    
        # AGREGAR NUEVO DATO
        

def modificarRuta():

    rutas = cargarRutas()
    profesores = cargarProfesores()
    estudiantes = cargarEstudiantes()
    matriculas = cargarMatriculas()

    rutaMod = input("Cuál ruta desea modificar: ")

    for ruta in rutas:
        
        if rutaMod == ruta["nombre"]:
                
            profesorImparte = input("Cuál es el nombre del profesor que dará la clase: ")

            for profesor in profesores:


                if profesorImparte == profesor["nombre"]:

                    if profesor["horario"][ruta["horario"]] == "disponible":

                        ruta["profesor"] = profesorImparte

                        # CAMBIO EL HORARIO DEL PROFESOR A OCUPADO SEGÚN SEA EL HORARIO DE LA RUTA
                        profesor["horario"][ruta["horario"]] = "ocupado"
                        break

                    else:

                        print("El horario que se requiere para esta ruta no la tiene disponible el profesor")
                        break


            
            opcionEstudiante = input("1. Si desea ingresarle un estudiante a la ruta \n"
                                        "2. Si desea salir \n"
                                        "Que opción eligirás : ")
            
            for estudiante in estudiantes:


                while opcionEstudiante != "2":

                    identificadorEstudiante = input("Cuál es el identificador  del estudiante: ")

                    if identificadorEstudiante == estudiante["identificacion"]:

                        if estudiante["estado"].lower() == "aprobado":

                            ruta["estudiantes"].append(identificadorEstudiante)

                            estudiante["estado"] = "matriculado"

                            matriculaNueva = {}

                            fecha_today = datetime.now().strftime("%Y-%m-%d")
                            fecha_futura = datetime.now() + timedelta(days= 8*30)
                            fecha_futura_actualizada = fecha_futura.strftime("%Y-%m-%d")

                            matriculaNueva["nombreEstudiante"] = estudiante["nombres"]
                            matriculaNueva["nombreProfesor"] = ruta["profesor"]
                            matriculaNueva["nombreRuta"] = ruta["nombre"]
                            matriculaNueva["fechaInicio"] = fecha_today
                            matriculaNueva["fechaFinal"] = fecha_futura_actualizada
                            matriculaNueva["salonEntrenamiento"] = ruta["areaEntrenamiento"]

                            matriculas.append(matriculaNueva)

                            break

                        else:

                            print("El estudiante no aprobó la prueba inicial o aún no presenta la prueba.")

                    else:
                        
                        print("El estudiante no está registrado")

                    opcionEstudiante = input("1. Si desea ingresarle otro estudiante a la ruta \n"
                                            "2. Si desea salir\n"
                                            "Seleccione una opción: ")

            if len(ruta["estudiantes"]) > 0 and ruta["profesor"] != "no asignado":
                ruta["estado"] = "matriculado"

    file = "rutas.json"

    with open(file, "w") as file:

        # AGREGAR NUEVO DATO
        
        json.dump(rutas, file)
    
        # AGREGAR NUEVO DATO



    fileProf = "profesores.json"

    with open(fileProf, "w") as fileProf:

        json.dump(profesores, fileProf)



    fileEstudiante = "estudiantes.json"

    with open(fileEstudiante, "w") as fileEstudiante:

        json.dump(estudiantes, fileEstudiante)
        


    fileMatricula = "matriculas.json"

    with open(fileMatricula, "w") as fileMatricula:

        json.dump(matriculas, fileMatricula)


def agregarModulo(identificadorRuta, identificadorModulo):
    
    rutas = cargarRutas()

    for ruta in rutas:
    
        if identificadorRuta == ruta["identificador"]:

            ruta["modulos"].append(identificadorModulo)


    file = "rutas.json"

    with open(file, "w") as fileRutas:

        # AGREGAR NUEVO DATO
        
        json.dump(rutas, fileRutas)
    
        # AGREGAR NUEVO DATO


def obtenerRutaPorIdentificador(identificadorRuta):

    rutas = cargarRutas()

    for ruta in rutas: 

        if ruta["identificador"] == identificadorRuta:

            return ruta