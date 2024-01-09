from estudiantes import cargarEstudiantes, traerCampersInscritos, traerCampersAprobados, crearNuevoEstudiante, registroPrueba
from profesores import cargarProfesores, ingresarNuevoProfesor
from rutas import cargarRutas, crearRuta, modificarRuta
from matriculas import cargarMatriculas
from modulos import crearModulo, asignarNotaModulo, ObtenerEstudianteRendimientoBajo

def imprimirCampers(estudiantes):

    for estudiante in estudiantes:

        print("identificacion: ", estudiante["identificacion"], "Nombre:", estudiante["nombres"], "apellidos:", estudiante["apellidos"],"direccion: ",estudiante["direccion"], "Celular:", estudiante["telefonoCelular"], "Estado:", estudiante["estado"])

def imprimirRendimientoBajo(estudiantes):

    for estudiante in estudiantes:
        print("identificacion: ", estudiante["identificacion"], "Nombre:", estudiante["nombres"], "apellidos:", estudiante["apellidos"])



def imprimirProfesores(profesores):

    for profesor in profesores:

        print("Identificacion:", profesor["identificacion"], "nombre:", profesor["nombre"])


def imprimirRutas(rutas):

    for ruta in rutas:

        print("Nombre de la Ruta:", ruta["nombre"], "Nombre de quien da la clase:", ruta["profesor"], "estudiantes:", ruta["estudiantes"], "estado de la ruta:", ruta["estado"])


def imprimirMatriculas(matriculas):

    for matricula in matriculas:

        print("Nombre del estudiante:", matricula["nombreEstudiante"], "Nombre del profesor:", matricula["nombreProfesor"], "Nombre de la ruta:", matricula["nombreRuta"], "fecha Inicio:", matricula["fechaInicio"], "fecha final: ", matricula["fechaFinal"], "salon entrenamiento: ", matricula["salonEntrenamiento"])



def menuEstudiantes():

    salir = False

    while not salir:


        pregunta = int(input("1. Si desea ver todos los estudiantes \n"
                            "2. Si desea ver sólo los estudiantes Inscritos \n"
                            "3. Si desea ver los estudiantes APROBADOS\n"
                            "4. Si desea registrar un nuevo estudiante\n"
                            "5. Estudiantes Rendimiento Bajo \n"
                            "6. Volver al menú principal\n"
                            "Que opción desea ingresar: "))
        
        match pregunta:

            case 1:

                estudiantes = cargarEstudiantes()

                if len(estudiantes) == 0:
                    print("No se ha encontrado ningún estudiante")
                    
                else:
                    imprimirCampers(estudiantes)
                    

            case 2:

                estudiantes = traerCampersInscritos()

                if len(estudiantes) == 0:
                    print("No se ha encontrado ningún estudiante")

                else:
                    imprimirCampers(estudiantes)


            case 3:

                estudiantes = traerCampersAprobados()

                if len(estudiantes) == 0:
                    print("No se ha encontrado ningún estudiante")

                else:
                    imprimirCampers(estudiantes)

            
            case 4:

                crearNuevoEstudiante()

            case 5:

                estudiantes = ObtenerEstudianteRendimientoBajo()
                
                if len(estudiantes)== 0:
                    print("No hay estudiantes con rendimiento bajo")

                else:
                    imprimirRendimientoBajo(estudiantes)

            case 6: 
                salir = True


def menuPruebas():

    salir = False

    while not salir:

        pregunta = int(input("1.Para registrar la prueba inicial.\n"
                             "2 Para volver al menú principal"
                            "Que opción desea ingresar: "))

        match pregunta: 

            case 1 :

                registroPrueba()

            case 2 : 

                salir = True

def menuProfesores():

    salir = False

    while not salir:

        pregunta = int(input("1. Para ver todos los profesores \n"
                            "2. Para agregar un nuevo profesor \n"
                            "3. Para volver al menú principal\n"
                            "Que opción desea ingresar: "))
        
        match pregunta:

            case 1:

                profesores = cargarProfesores()

                if len(profesores) == 0:
                    print("No hay profesores")

                else:
                    imprimirProfesores(profesores)

            case 2:

                ingresarNuevoProfesor()


            case 3:

                salir = True
 

def menuRutas():

    salir = False

    while not salir:

        pregunta = int(input("1. Si desea mostrar todas las rutas \n"
                             "2. Si desea crear una nueva Ruta \n"
                             "3. Si desea modificar una Ruta \n"
                             "4. Si desea volver al menú principal \n"
                             "Ingrese la opción que desee: "))
        
        match pregunta:

            case 1:
                
                rutas = cargarRutas()

                if len(rutas) == 0:
                    print("No hay rutas")

                else:
                    imprimirRutas(rutas)


            case 2:
                
                crearRuta()

            case 3:

                modificarRuta()


            case 4:

                salir = True


def menuModulos():

    salir = False

    while not salir:

        pregunta = int(input("1. Si desea crear un nuevo modulo. \n"
                             "3. Asignar nota por modulo \n"
                             "2. Salir \n"
                             "Elige la opción que desees: "))
        
        match pregunta:

            case 1:

                crearModulo()

            case 2:

                asignarNotaModulo()

            case 3:

                salir = True


def menuMatriculas():

    salir = False

    while not salir:

        pregunta = int(input("1. Si desea revisar las matriculas existentes. \n"
                             "2. Si desea volver al menú principal \n"
                             "Elige la opción que desees"))

        match pregunta:

            case 1:

                matricula = cargarMatriculas()

                imprimirMatriculas(matricula)
                
            case 2: 
                
                salir = True