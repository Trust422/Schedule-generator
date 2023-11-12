from profesor import profesor as prof
from clase import curso as cur

class main:
    profesores=[]
    matematicas= cur("IL365", "Matematicas de la ingenieria")
    profesores.append(prof ("Martin Linar", "00001111000011110000", ["Matematica", "Fisica"]))
    profesores.append(prof ("Juan Perez", "11110000000000001111", ["Matematica", "Fisica"]))
    profesores[0].agregarCurso("IL365")
    profesores[0].agregarCurso("IL440")
    matematicas.setProfesor(profesores[0])
    print (matematicas.mostrarCurso())