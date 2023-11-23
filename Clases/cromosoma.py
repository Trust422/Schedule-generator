import random

class Cromosoma:
    def __init__(self, materias, salones, turnos):
        # Inicializar el cromosoma con asignaciones aleatorias
        self.asignaciones = {}
        self.generar_asignaciones_aleatorias(materias, salones, turnos)

    def generar_asignaciones_aleatorias(self, cursos, salones, turnos):
        for materia, lista_cursos in cursos.items():
                cursos_seleccionados = random.sample(lista_cursos, min(4, len(lista_cursos)))
                for curso in cursos_seleccionados:
                    # Utilizar los valores de turno y salon del objeto curso
                    turno = curso.getTurno()
                    salon = curso.getSalon()
                    profesor = curso.getProfesor()
                    # Verificar si la asignación ya existe
                    while (materia, turno) in self.asignaciones:
                        # Si ya existe, seleccionar otro curso
                        curso = random.choice(lista_cursos)
                        turno = curso.getTurno()
                        salon = curso.getSalon()
                        profesor = curso.getProfesor()

                    self.asignaciones[(materia, turno)] = {"salon": salon, "profesor": profesor}


    def __str__(self):
        # Método para imprimir el cromosoma de manera legible
        return str(self.asignaciones)
    def getKeys(self):
        return list(((self.asignaciones.keys())))

    def mostrar(self):
        # Método para mostrar cada asignación en una línea separada
        for (materia, turno), info in self.asignaciones.items():
            print(f"{materia} - {turno}: salon: {info['salon']} - profesor:  {info['profesor'].getNombre()}")

    def fitness(self):
        def contar_choques_prof(self):
            choques_profesor = {}
            choques=0
            for asignacion, detalles in self.asignaciones.items():
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
        def contar_choques_salon(self):
            choques_salon={}
            choques=0
            for asignacion, detalles in self.asignaciones.items():
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
        choques_prof=contar_choques_prof(self)
        choques_sal=contar_choques_salon(self)
        return(choques_prof+ choques_sal) #cantidad de cursos por materia y distribucion 
    def crossover(self, otro):
        punto_corte = random.randint(0, len(self.asignaciones))
        hijo = Cromosoma({}, 0, 0)
        hijo.asignaciones = dict(list(self.asignaciones.items())[:punto_corte])
        for asignacion, detalles in otro.asignaciones.items():
            if asignacion not in hijo.asignaciones:
                hijo.asignaciones[asignacion] = detalles
        return hijo