import sys
import random
import time 
sys.path.append("Clases")
from Clases.profesor import Profesor as prof
from Clases.materia import Materia as mat
from Clases.curso import Curso as cur
from Clases.oferta import Oferta as of
from Clases.cromosoma_v2 import Cromosoma as cr
import pandas as pd #libreria para la lectura de archivos de entrada tipo (csv)
#variables globales
cant_cursos_por_materia=2 #variable que define la cantidad de cursos por materia
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
horas_dispo_area={}
materias_por_area={}
def ingresar_profesores_desde_archivo(archivo_profesores): #funcion que regresa la lsita de profesores recibiendo como entrada el archivo csv de profesores, cada profesor tiene como campo ('Nombre´, 'Disponibilidad', 'area')
    profesores=[]
    x=random.randint(1,2)
    for i in range(len(archivo_profesores)):
        profesores.append(prof(archivo_profesores.iloc[i,0], str(archivo_profesores.iloc[i,1]), [archivo_profesores.iloc[i,2]])) #creacion de objetos profesor para añadirlos a la lista
        horas_dispo_area[archivo_profesores.iloc[i,2]]= horas_dispo_area[archivo_profesores.iloc[i,2]]+profesores[i].contarHoras() #creacion de un diccionario con el nombre del area como key y las horas de los profesores como valor
    return profesores
def ingresar_cursos_desde_archivo(archivo_cursos):#funcion que regresa la lista de cursos recibiendo como entrada el archivo csv de materias,, cada materia tiene como campos ('Nombre, 'Departamento', 'Academia', 'Clave')
    cursos=[]
    for i in range(len(archivo_cursos)):
        cursos.append(mat(archivo_cursos.iloc[i,0], archivo_cursos.iloc[i,1], archivo_cursos.iloc[i,2], archivo_cursos.iloc[i,3])) #creacion de objetos materia para añadirlos a la lista
        if archivo_cursos.iloc[i,2] not in materias_por_area:
            materias_por_area[archivo_cursos.iloc[i,2]]=1
        else:
            materias_por_area[archivo_cursos.iloc[i,2]]=materias_por_area[archivo_cursos.iloc[i,2]]+1
        if archivo_cursos.iloc[i,2] not in horas_dispo_area:
            horas_dispo_area[archivo_cursos.iloc[i,2]]=0 #creacion de un diccionario con el nombre de la materia como key y las horas de la materia como valor
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
                            if profesor.getDisponibilidad()[i] == "1" and profesor.getDisponibilidad()[i+7] == "1": #se verifica la disponibiliad de esta manera ya que se manejan 12 turnos
                                curso=cur(profesor, materia, salon, turnos[i]) #creacion de un objeto curso
                                if materia.getNombre() not in cursos_dispo: #verificacion si en el diccionario de cursos_dispo ya hay un apartado con el nombre de la materia
                                    cursos_dispo[materia.getNombre()]=[] #si no existe se crea la key
                                cursos_dispo[materia.getNombre()].append(curso) #guardado del curso potencial en el diccionario cursos_disoi

    return cursos_dispo
#implementación del Algortimo Genetico
def inicializacion_AG(cursos_dispo, num_cromosomas):
    cromosomas=[]
    for i in range(num_cromosomas): #creacion de los cromosomas iniciales
            cromosoma_nuevo=cr(cursos_dispo)
            cromosomas.append(cromosoma_nuevo)

    fitness_cromo=calcula_fitness_cromosomas(cromosomas)
    return fitness_cromo

def calcula_fitness_cromosomas(cromosomas):
    fitness_cromo={}
    for i in range(len(cromosomas)):
        fitness_cromo[cromosomas[i]]=cromosomas[i].fitness()
    fitness_cromo = dict(sorted(fitness_cromo.items(), key=lambda item: item[1])) #ordenamiento del diccionario de fitness de menor a mayor
    return fitness_cromo

def seleccionar_mejores(diccionario, n):

    sorted_diccionario = dict(sorted(diccionario.items(), key=lambda item: item[1], reverse=True))
    mitad_superior = dict(list(sorted_diccionario.items())[n:])
    return mitad_superior


def crossover(padres):
    hijos=[]
    elitismo=int(len(list(padres.keys()))*.10)
    for i in range(0, elitismo, 1):
        padre1 = list(padres.keys())[i]
        hijos.append(padre1)
    for i in range(int(elitismo/2)-1, len(padres)-1, 1):
        padre1 = list(padres.keys())[i]
        padre2 = list(padres.keys())[i + 1]
        hijo1, hijo2 = padre1.crossover(padre2)
        hijos.append(hijo1)
        hijos.append(hijo2)
    return hijos

def seleccion(padres, mid):
    regreso={}

    for i in range (int(mid/2)):
        regreso[list(padres.keys())[i]]=padres[list(padres.keys())[i]]
    return regreso

def mutacion(cromosoma):
    cromosoma.mutacion()
    return cromosoma

class main:    
    materias = ingresar_cursos_desde_archivo( pd.read_csv("Archivos de entrada/clases.csv", encoding='latin-1'))
    profesores = ingresar_profesores_desde_archivo(pd.read_csv("Archivos de entrada/profesores.csv", dtype={'Disponibilidad': str},encoding='latin-1'))
    poblacion=1000
    generaciones=200

    tiempo_inicial=time.time()  
    cursos_dispo=cursos_disponibles_posibles(profesores, materias)
    generacion_inicial=inicializacion_AG(cursos_dispo, poblacion)
    print (len(list(cursos_dispo.keys())))
    
    for i in range(generaciones):
    
        #padres=seleccionar_mejores(generacion_inicial, int(poblacion*.8))
        print(f"mejor fitness genearcion:{i} ", generacion_inicial[list(generacion_inicial.keys())[0]])
        descendencia=crossover(generacion_inicial)
        descendencia_fitness=calcula_fitness_cromosomas(descendencia)
        descendencia_fitness=seleccion(descendencia_fitness, len(list(descendencia_fitness.keys())))
        generacion_inicial=descendencia_fitness
        if(generacion_inicial[list(generacion_inicial.keys())[0]]==0):
            break
        for j in range(int(poblacion*.1)):  
            list(generacion_inicial.keys())[j].mutacion( turnos) 
        
    tiempo_final=time.time()
    tiempo_ejecucion=tiempo_final-tiempo_inicial
    print('tiempo de ejecucion en segundos: ', tiempo_ejecucion)
    dic=list(generacion_inicial)[0].mostrar(list(cursos_dispo.keys()))
    print (len(dic.keys()))


    #medir la cantidad de horas disponibles por area
    for curso in horas_dispo_area:
        x=horas_dispo_area[curso]/(materias_por_area[curso]*cant_cursos_por_materia*4)
        if x<1:
            print("Profesores insuficientes para el area: ", curso)
        else:
            print("Todo bien ", curso)
