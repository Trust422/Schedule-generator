import random

class Cromosoma:
    def __init__(self, materias, salones, turnos):
        # Inicializar el cromosoma con asignaciones aleatorias
        self.asignaciones = {}
        self.generar_asignaciones_aleatorias(materias, salones, turnos)

    def generar_asignaciones_aleatorias(self, cursos, salones, turnos):
        # Generar 4 cursos por cada materia
        for cursos, lista_cursos in cursos.items():
            cursos_seleccionados = random.sample(lista_cursos, 4)
            for curso in cursos_seleccionados:
                # Utilizar los valores de turno y salon del objeto curso
                turno = curso.getTurno()
                salon = curso.getSalon()
                profesor=curso.getProfesor()
                self.asignaciones[(curso.getMateria(), turno)] = {"salon": salon, "profesor": profesor}

    def __str__(self):
        # Método para imprimir el cromosoma de manera legible
        return str(self.asignaciones)
    
    def mostrar(self):
        # Método para mostrar cada asignación en una línea separada
        for (materia, turno), info in self.asignaciones.items():
            print(f"{materia.getNombre()} - {turno}: salon: {info['salon']} - profesor:  {info['profesor'].getNombre()}")
