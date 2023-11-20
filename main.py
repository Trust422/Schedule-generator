import sys
sys.path.append("Clases")
from Clases.profesor import Profesor as prof
from Clases.materia import Materia as mat
from Clases.curso import Curso as cur
from Clases.oferta import Oferta as of
from Clases.cromosoma import Cromosoma as cr
import pandas as pd
turnos=["l-x 9-11", "l-x 11-13", "l-x 13-15", "l-x 15-17",
            "m-j 9-11", "m-j 11-13", "m-j 13-15", "m-j 15-17",
            "x-v 9-11", "x-v 11-13", "x-v 13-15", "x-v 15-17",
        ] 
salones=["x001", "x002", "x003", "x004", "x005",
            "x006", "x007", "x008", "x009", "x010",
            "x011", "x012", "x013", "x014", "x015",
            "x016", "x017", "x018", "x019", "x020",]
#metodos para lectura de csv
def ingresar_profesores_desde_archivo(archivo_profesores):
    profesores=[]
    for i in range(len(archivo_profesores)):
        profesores.append(prof(archivo_profesores.iloc[i,0], str(archivo_profesores.iloc[i,1]), [archivo_profesores.iloc[i,2]]))
    return profesores
def ingresar_cursos_desde_archivo(archivo_cursos):
    cursos=[]
    for i in range(len(archivo_cursos)):
        cursos.append(mat(archivo_cursos.iloc[i,0], archivo_cursos.iloc[i,1], archivo_cursos.iloc[i,2], archivo_cursos.iloc[i,3]))
    return cursos
def mostrar_cursos(cursos):
    for curso in cursos:
        print(curso.mostrarMateria())
def mostrar_profesores(profesores):
    for profesor in profesores:
        print(profesor.mostrar_profesor())
    print("Numero total de profesores: " + str(len(profesores)))
#filtrado de profesores
def profesores_pertenecientes_Area(profesores, area):
    profesores_re=[]
    for profesor in profesores:
        if profesor.perteneceArea(area)==1:
            profesores_re.append(profesor)
    return profesores_re
def profesores_disponibles_hora(profesores, dia, hora):
    profesores_dis=[]
    for profesor in profesores:
        if profesor.getDisponibilidad()[0]=="1":
            profesores_dis.append(profesor)
    return profesores_dis
#filtrado de materias
def cursos_disponibles_posibles(profesores: prof, materias: mat):
    cursos_dispo = {}
    materias_por_area = {}
    for materia in materias:
        if materia.getAcademia() not in materias_por_area:
            materias_por_area[materia.getAcademia()] = []
        materias_por_area[materia.getAcademia()].append(materia)
    for profesor in profesores:
        area_buscar = str(profesor.getArea())
        area_buscar=area_buscar[2:-2]
        if area_buscar in materias_por_area:
            materias_misma_area = materias_por_area[area_buscar]
            for materia in materias_misma_area:
                for salon in salones:
                    for i in range(len(turnos)):
                            if profesor.getDisponibilidad()[i] == "1" and profesor.getDisponibilidad()[i+7] == "1":
                                curso=cur(profesor, materia, salon, turnos[i])
                                if materia.getNombre() not in cursos_dispo:
                                    cursos_dispo[materia.getNombre()]=[]
                                cursos_dispo[materia.getNombre()].append(curso)
    return cursos_dispo

class main:    
    profesores = ingresar_profesores_desde_archivo(pd.read_csv("Archivos de entrada/profesores.csv"))
    materias = ingresar_cursos_desde_archivo( pd.read_csv("Archivos de entrada/clases.csv"))
    oferta_academica=of()
    cursos_dispo=cursos_disponibles_posibles(profesores, materias)
    cromosoma_ejemplo = cr(cursos_dispo, salones, turnos)
    print((cromosoma_ejemplo.mostrar()))

    
