import random

class Cromosoma:
    def __init__(self, materias):
        # Inicializar el cromosoma con asignaciones aleatorias
        self.asignaciones = []  # Inicializar como una lista
        self.generar_asignaciones_aleatorias(materias)

    def generar_asignaciones_aleatorias(self, cursos):
        if len(cursos) == 0:
            return
        for lista_cursos in cursos.keys():
            cursos_seleccionados = random.sample(cursos[lista_cursos], 4)
            for curso in cursos_seleccionados:
                self.asignaciones.append(curso)
                

    def contar_choques_prof(self): #regresa diccionario de forma {turno: {profesor: [cursos]}}
        choques_profesor = {}
        choques = 0
        for curso in self.asignaciones:
            profesor = curso.getProfesor()
            turno = curso.getTurno()
            if turno not in choques_profesor:
                choques_profesor[turno] = {}

            if profesor in choques_profesor[turno]:
                choques_profesor[turno][profesor].append(curso)
                choques += 1
            else:
                choques_profesor[turno][profesor] =[]
                choques_profesor[turno][profesor].append(curso)
        return choques, choques_profesor
    def choques_salon(self):
        choques_salon = {}
        choques = 0
        for curso in self.asignaciones:
            salon = curso.getSalon()
            turno = curso.getTurno()
            if turno not in choques_salon:
                choques_salon[turno] = {}

            if salon in choques_salon[turno]:
                choques_salon[turno][salon].append(curso)
                choques += 1
            else:
                choques_salon[turno][salon] =[]
                choques_salon[turno][salon].append(curso)
        return choques, choques_salon
    def fitness(self):
        choques_p, choques_prof=self.contar_choques_prof()
        choques_s, choques_salon=self.choques_salon()
        fitness=choques_p 
        return fitness
                    
    def crossover(self, otro):
        corte=random.randint(1, len(self.asignaciones)-1)
        hijo1=Cromosoma([]) 
        hijo2=Cromosoma([])
        hijo1.asignaciones=self.asignaciones[:corte] + otro.asignaciones[corte:]
        hijo2.asignaciones=otro.asignaciones[:corte] + self.asignaciones[corte:] 
        return hijo1, hijo2
    def mostrar (self,lista_materia):
        dic={}
        asigna=self.asignaciones[0].getMateria()
        for asignacion in self.asignaciones:
            print(asignacion.mostrar())
            if asignacion.getMateria().getNombre() not in dic:
                dic[asignacion.getMateria().getNombre()]=1
            else:
                dic[asignacion.getMateria().getNombre()]=dic[asignacion.getMateria().getNombre()]+1
        print(len(self.asignaciones))     
        return dic     