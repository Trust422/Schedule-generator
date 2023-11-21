import sys
sys.path.append("Clases")
from Clases.profesor import Profesor as prof
from Clases.materia import Materia as mat
from Clases.curso import Curso as cur
from Clases.oferta import Oferta as of
from Clases.cromosoma import Cromosoma as cr
import pandas as pd #libreria para la lectura de archivos de entrada tipo (csv)
turnos=[    "l-x 9-11", "l-x 11-13", "l-x 13-15", "l-x 15-17",
            "m-j 9-11", "m-j 11-13", "m-j 13-15", "m-j 15-17",
            "x-v 9-11", "x-v 11-13", "x-v 13-15", "x-v 15-17",
        ] #lista de los turnos con los que se creará por dia y hora- 12 pares en total
salones=[   "x001", "x002", "x003", "x004", "x005",
            "x006", "x007", "x008", "x009", "x010",
            "x011", "x012", "x013", "x014", "x015",
            "x016", "x017", "x018", "x019", "x020",
            ]#lista de los salones del edificio x - 20 salones en total
#metodos para lectura de csv
def ingresar_profesores_desde_archivo(archivo_profesores): #funcion que regresa la lsita de profesores recibiendo como entrada el archivo csv de profesores, cada profesor tiene como campo ('Nombre´, 'Disponibilidad', 'area')
    profesores=[]
    for i in range(len(archivo_profesores)):
        profesores.append(prof(archivo_profesores.iloc[i,0], str(archivo_profesores.iloc[i,1]), [archivo_profesores.iloc[i,2]])) #creacion de objetos profesor para añadirlos a la lista
    return profesores
def ingresar_cursos_desde_archivo(archivo_cursos):#funcion que regresa la lista de cursos recibiendo como entrada el archivo csv de materias,, cada materia tiene como campos ('Nombre, 'Departamento', 'Academia', 'Clave')
    cursos=[]
    for i in range(len(archivo_cursos)):
        cursos.append(mat(archivo_cursos.iloc[i,0], archivo_cursos.iloc[i,1], archivo_cursos.iloc[i,2], archivo_cursos.iloc[i,3])) #creacion de objetos materia para añadirlos a la lista
    return cursos
def mostrar_cursos(cursos): #funcion para imprimir en pantalla los cursos leidos
    for curso in cursos:
        print(curso.mostrarMateria())
def mostrar_profesores(profesores): #funcion para imprimir la lista de profesores
    for profesor in profesores:
        print(profesor.mostrar_profesor())
    print("Numero total de profesores: " + str(len(profesores)))
#filtrado de profesores
def profesores_pertenecientes_Area(profesores, area):#funcion en la que se regresa una lista de profesores pertenecientes al area definida en la llamda a la funcion
    profesores_re=[]
    for profesor in profesores:
        if profesor.perteneceArea(area)==1:
            profesores_re.append(profesor)
    return profesores_re
#filtrado de materias
def cursos_disponibles_posibles(profesores: prof, materias: mat):
    cursos_dispo = {}
    materias_por_area = {}
    #creacion de un diccionario con todas las materias con la clave siendo el area, ejem("programacion", "matematicas")
    for materia in materias:
        if materia.getAcademia() not in materias_por_area:
            materias_por_area[materia.getAcademia()] = []
        materias_por_area[materia.getAcademia()].append(materia)
    #funcion que creara todas las posibles combinaciones de materias dependiendo el area de la materia, el area del profesor y la disponibilidad de este
    for profesor in profesores:
        area_buscar = str(profesor.getArea())
        area_buscar=area_buscar[2:-2] #elimina los 2 primeros elementos y los dos ultimos de un string ya que se area_buscar regresa la variable como ['Matematicas']
        if area_buscar in materias_por_area: #verifica que el area del profeosor se encuentre en el diccionario materias_por_area
            materias_misma_area = materias_por_area[area_buscar] #obtencion de una sublista de  materias que el profesor puede dar
            for materia in materias_misma_area:
                for salon in salones:
                    for i in range(len(turnos)):
                            if profesor.getDisponibilidad()[i] == "1" and profesor.getDisponibilidad()[i+7] == "1": #se verifica la disponibiliad de esta manera ya que se manejan 12 turnos, los dias se manejan por pares a la misma hora
                                curso=cur(profesor, materia, salon, turnos[i]) #creacion de un objeto curso
                                if materia.getNombre() not in cursos_dispo: #verificacion si en el diccionario de cursos_dispo ya hay un apartado con el nombre de la materia
                                    cursos_dispo[materia.getNombre()]=[] #si no existe se crea la key
                                cursos_dispo[materia.getNombre()].append(curso) #guardado del curso potencial en el diccionario cursos_disoi
    return cursos_dispo
#implementación del Algortimo Genetico
def inicializacion_AG(cursos_dispo, num_cromosomas):
    cromosomas=[]
    fitness_cromo={}
    for i in range(num_cromosomas):
        cromosoma_nuevo=cr(cursos_dispo, salones, turnos)
        cromosomas.append(cromosoma_nuevo)
        fitness_cromo[cromosoma_nuevo]=fitness(cromosoma_nuevo)
    sorted_fitness = dict(sorted(fitness_cromo.items(), key=lambda item: item[1]))
    #print(sorted_fitness)
    print(list(sorted_fitness.keys())[0].mostrar())
    print(fitness_cromo[(list(sorted_fitness.keys()))[0]])

def fitness(solucion):
    def contar_choques_prof(solucion):
        choques_profesor = {}
        choques=0

        for asignacion, detalles in solucion.asignaciones.items():
            profesor = detalles['profesor']
            turno = asignacion[1]

            if turno not in choques_profesor:
                choques_profesor[turno] = {}

            if profesor in choques_profesor[turno]:
                choques_profesor[turno][profesor] += 1
                choques+=1
            else:
                choques_profesor[turno][profesor] = 1
        return choques
    def imprimir_choques(choques_profesor):
        for turno, profesores_en_turno in choques_profesor.items():
            print(f"\nTurno: {turno}")
            for profesor, cantidad_choques in profesores_en_turno.items():
                if cantidad_choques > 1:
                    print(f"Profesor: {profesor.getNombre()} - Choques: {cantidad_choques}")
    def contar_choques_salon(solucion):
        choques_salon={}
        choques=0
        for asignacion, detalles in solucion.asignaciones.items():
            salon = detalles['salon']
            turno = asignacion[1]

            if turno not in choques_salon:
                choques_salon[turno] = {}

            if salon in choques_salon[turno]:
                choques_salon[turno][salon] += 1
                choques+=1
            else:
                choques_salon[turno][salon] = 1
        return choques
    choques_prof=contar_choques_prof(solucion)
    choques_sal=contar_choques_salon(solucion)
    #print(choques_prof, choques_sal)
    return(choques_prof*250 + choques_sal*50)



class main:    
    profesores = ingresar_profesores_desde_archivo(pd.read_csv("Archivos de entrada/profesores.csv"))
    materias = ingresar_cursos_desde_archivo( pd.read_csv("Archivos de entrada/clases.csv"))
    oferta_academica=of()
    inicializacion_AG(cursos_disponibles_posibles(profesores, materias), 1000)
    
    


    
