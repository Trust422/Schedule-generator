import sys
sys.path.append("Clases")
from Clases.profesor import profesor as prof
from Clases.clase import curso as cur
import pandas as pd 

def ingresar_profesores_desde_archivo(archivo_profesores):
    profesores=[]
    for i in range(len(archivo_profesores)):
        profesores.append(prof(archivo_profesores.iloc[i,0], str(archivo_profesores.iloc[i,1]), [archivo_profesores.iloc[i,2]]))
    return profesores
def ingresar_cursos_desde_archivo(archivo_cursos):
    cursos=[]
    for i in range(len(archivo_cursos)):
        cursos.append(cur(archivo_cursos.iloc[i,0], archivo_cursos.iloc[i,1], archivo_cursos.iloc[i,2], archivo_cursos.iloc[i,3]))
    return cursos
def mostrar_cursos(cursos):
    for curso in cursos:
        print(curso.mostrarCurso())
def mostrar_profesores(profesores):
    for profesor in profesores:
        print(profesor.mostrar_profesor())
    print("Numero total de profesores: " + str(len(profesores)))
class main:
    archivo_profesores = pd.read_csv("Archivos de entrada/profesores.csv")
    archivo_clases = pd.read_csv("Archivos de entrada/clases.csv")
    profesores = ingresar_profesores_desde_archivo(archivo_profesores)
    clases = ingresar_cursos_desde_archivo(archivo_clases)

    mostrar_profesores(profesores)
    mostrar_cursos(clases)
