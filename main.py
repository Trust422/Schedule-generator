import sys
sys.path.append("Clases")
from Clases.profesor import Profesor as prof
from Clases.materia import Materia as mat
from Clases.curso import Curso as cur
from Clases.oferta import Oferta as of
import pandas as pd 

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
class main:
    
    archivo_profesores = pd.read_csv("Archivos de entrada/profesores.csv")
    archivo_clases = pd.read_csv("Archivos de entrada/clases.csv")
    profesores = ingresar_profesores_desde_archivo(archivo_profesores)
    clases = ingresar_cursos_desde_archivo(archivo_clases)
    curso=cur(profesores[0],clases[0])
    curso2=cur(profesores[1], clases[0])
    oferta_academica=of()
    curso.setNRC(69420)
    curso2.setNRC(4859434854)
    # (hora, dia, salon)
    oferta_academica.asignar_clase(0, 0, 0, curso)
    oferta_academica.asignar_clase(0,0, 3, curso2)
    oferta_academica.asignar_clase(1, 2, 1, curso)
    oferta_academica.asignar_clase(2, 4, 3, curso)
    print(oferta_academica.mostrar_horario_clases())
    #mostrar_profesores(profesores)
    #mostrar_cursos(clases)
