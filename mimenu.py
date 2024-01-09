import json
from menusSecundarios import menuEstudiantes, menuPruebas, menuProfesores, menuRutas, menuMatriculas, menuModulos
from profesores import cargarProfesores
from rutas import *


def menuPrograma():

    salir = False

    while  not salir:

        pregunta = int(input("1. Si desea ir al menú de los estudiantes.\n"
                            "2. Si desea ir al menú de pruebas.\n"
                            "3. Si desea ir al menú de profesores. \n"
                            "4. Si desea ir al menú de las Rutas. \n"
                            "5. Si desea ir al menú de las matriculas. \n"
                            "6. Si desea ir al menú de los modulos. \n"
                            "7. Para Salir\n"
                            "¿Qué opción desea ingresar?: "))

        match pregunta:

            case 1:

                menuEstudiantes()

            case 2:
                
                menuPruebas()
                

            case 3:
                
                menuProfesores()

            
            case 4:

                menuRutas()


            case 5:

                menuMatriculas()


            case 6:

                menuModulos()

            case 7:
                print("Hasta luego, que tenga un buen día")
                salir = True

menuPrograma()