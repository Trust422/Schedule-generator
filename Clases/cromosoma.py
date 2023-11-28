import random

class Cromosoma:
    def __init__(self, materias):
        # Inicializar el cromosoma con asignaciones aleatorias
        self.asignaciones = []  # Inicializar como una lista
        self.generar_asignaciones_aleatorias(materias)

    def generar_asignaciones_aleatorias(self, cursos: dict):

        for lista_cursos in cursos.keys():  # Usar .values() para obtener solo los valores del diccionario
            cursos_seleccionados = random.sample(cursos)
            for curso in cursos_seleccionados:
                # Utilizar los valores de turno y salon del objeto curso
                print (curso, "curso")
                #self.asignaciones.append(curso)  # Agregar el curso directamente

    def __str__(self):
        # Método para imprimir el cromosoma de manera legible
        return str(self.asignaciones)

    def mostrar(self):
        # Método para mostrar cada asignación en una línea separada
        print("Cromosoma:")
        for curso in self.asignaciones:
            print(curso.getProfesor().getNombre() + "\n" + curso.getMateria().getNombre() + "\n" + curso.getSalon() + "\n" + curso.getTurno() + "\n\n")

    def contar_choques_prof(self):
        choques_profesor = {}
        choques = 0
        for curso in self.asignaciones:
            profesor = curso.getProfesor()
            turno = curso.getTurno()
            if turno not in choques_profesor:
                choques_profesor[turno] = {}

            if profesor in choques_profesor[turno]:
                choques_profesor[turno][profesor] = curso.getMateria()
                choques += 1
            else:
                choques_profesor[turno][profesor] = curso.getMateria()
        return choques, choques_profesor

    def contar_choques_salon(self):
        choques_salon = {}
        choques = 0
        for curso in self.asignaciones:
            salon = curso.getSalon()
            turno = curso.getTurno()
            if turno not in choques_salon:
                choques_salon[turno] = {}

            if salon in choques_salon[turno]:
                choques_salon[turno][salon] += 1
                choques += 1
            else:
                choques_salon[turno][salon] = 1
        return choques

    def fitness(self):
        choques_prof, _ = self.contar_choques_prof()
        choques_sal = self.contar_choques_salon()
        #print (choques_prof, choques_sal, "fitness")
        return choques_prof + choques_sal

    def crossover(self, otro):
        punto_corte = random.randint(0, len(self.asignaciones))
        # punto_corte = len(self.asignaciones) // 2  # Comentado para usar el punto de corte aleatorio
        hijo = Cromosoma([])
        hijo.asignaciones = self.asignaciones[:punto_corte] + otro.asignaciones[punto_corte:]
        return hijo

    def mutacion(self, turnos):
        _, choques_profesor = self.contar_choques_prof()

        for curso in self.asignaciones:
            profesor = curso.getProfesor()
            turno = curso.getTurno()
            if profesor in choques_profesor[turno]:
                if curso.getProfesor().getDisponibilidad()[turno] == "1" and curso.getProfesor().getDisponibilidad()[turno + 7] == "1":
                    curso.setTurno(random.choice(turnos))

    def calcular_cant_clases_total(self):
        return len(self.asignaciones)
