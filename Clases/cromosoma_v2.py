import random

turnos=[
        "l-x 09-11", "l-x 11-13", "l-x 13-15", "l-x 15-17",
        "m-j 09-11", "m-j 11-13", "m-j 13-15", "m-j 15-17",
        "x-v 09-11", "x-v 11-13", "x-v 13-15", "x-v 15-17",
        ] 
info_turnos = {}
for turno in turnos:
    dias, horas = turno.split(" ")
    dia_inicio, dia_fin = dias.split("-")
    hora_inicio, hora_fin = horas.split("-")

    info_turnos[turno]=({
        "dia_inicio": dia_inicio,
        "dia_fin": dia_fin,
        "hora_inicio": hora_inicio,
        "hora_fin": hora_fin,
    })
class Cromosoma:
    def __init__(self, cursos_disponibles, N):
        """
        Constructor de la clase cromosoma \n
        llama a una funcion para generar asignaciones aleatorias\n
        se crean N asignaciones por materia \n
        parametros: \n
        cursos_disponibles: cursos disponibles para asignar al cromosoma tipo diccionario (ejem: {"Programacion": [curso1, curso2]})
        cantidad_cursos_materia: cantidad de cursos a generar
        generara un cromosoma con asignaciones aleatorias, N asignaciones por materia\n
        
        """
        # Inicializar el cromosoma con asignaciones aleatorias
        self.asignaciones = []  # Inicializar como una lista
        self.generar_asignaciones_aleatorias(cursos_disponibles, N)

    def generar_asignaciones_aleatorias(self, cursos, cantidad_cursos_materia):
        """
        Genera asignaciones aleatorias para el cromosoma\n
        parametros: \n
        cursos: cursos disponibles para asignar al cromosoma tipo diccionario (ejem: {"Programacion": [curso1, curso2]})
        cantidad_cursos_materia: cantidad de cursos a generar
        """
        if len(cursos) == 0:
            return
        for lista_cursos in cursos.keys():
            cursos_seleccionados = random.sample(cursos[lista_cursos], cantidad_cursos_materia)
            for curso in cursos_seleccionados:
                self.asignaciones.append(curso)
                

    def contar_choques_prof(self): #regresa diccionario de forma {turno: {profesor: [cursos]}}
        """
        Cuenta los choques de profesores\n
        Regresa un diccionario con los choques de profesores por turno tipo  {turno: {profesor: [cursos]}}\n
        y tambien regresa el numero total de choques de profesores\n"""
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
        """
        Cuenta los choques de salon\n
        Regresa un diccionario con los choques de salon por turno tipo  {turno: {salon: [cursos]}}\n
        y tambien regresa el numero total de choques de salon\n"""
        choques_salon = {}
        choques = 0
        for curso in self.asignaciones:
            salon = curso.getSalon()
            turno = info_turnos[curso.getTurno()]["hora_inicio"]+"-"+info_turnos[curso.getTurno()]["hora_fin"]
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
        """funcion aptitud\n
        regresa el numero de choques de profesores y salones\n
        """
        choques_p, _=self.contar_choques_prof()
        choques_s, _=self.choques_salon_v2()
        fitness=choques_p + choques_s  
        return fitness
    def crossover(self, otro):
        """funcion crossover\n
        Esta funcion recibe dos cromosomas y regresa dos hijos de la cruza de los cromosomas\n
        parametros:\n
        otro: cromosoma con el que se va a cruzar el cromosoma actual\n
        se realiza un corte aleatorio y se intercambian las asignaciones de los cromosomas\n
        regresa dos hijos de la cruza de los cromosomas\n
        """
        corte=random.randint(1, len(self.asignaciones)-1)
        hijo1=Cromosoma([], 0) 
        hijo2=Cromosoma([], 0)
        hijo1.asignaciones=self.asignaciones[:corte] + otro.asignaciones[corte:]
        hijo2.asignaciones=otro.asignaciones[:corte] + self.asignaciones[corte:] 
        return hijo1, hijo2

    def mutacion(self, salones):
        """
        FUNCION MUTACION\n
        recibe una lista de turnos\n
        realiza una cambio aleatori0 de turno a un curso que tenga choques de salon \n
        se utiliza la funcion choques_salon para obtener los choques de salon\n
        verifica internamente que el profesor este disponible en el nuevo turno\n
        Parametros: \n
        turnos: lista de turnos disponibles para asignar\n
        """
        _, choque_salon=self.choques_salon_v2()
        
        dia=random.choice(list(choque_salon.keys()))
        turno=random.choice(list(choque_salon[dia].keys()))
        salon=random.choice(list(choque_salon[dia][turno].keys()))
        curso=random.choice(choque_salon[dia][turno][salon])
        aula=curso.getSalon()
        index=salones.index(aula)
        attempts=5
        while attempts>0:
            if index == len(salones)-1:
                index=0
            salon_random=salones[index+1]
            if(salon_random not in choque_salon[dia][turno]):
                curso.setSalon(salon_random)
                return 
            index+=1
            attempts-=1
    
    def choques_salon_v2(self):
        """
        Cuenta los choques de salon\n
        Regresa un diccionario con los choques de salon por día tipo {dia: {turno: {salon: [cursos]}}}\n
        y también regresa el número total de choques de salon\n
        """
        choques_salon = {dia: {} for dia in ["l", "m", "x", "j", "v"]}
        choques = 0

        for curso in self.asignaciones:
            salon = curso.getSalon()
            turno = info_turnos[curso.getTurno()]["hora_inicio"]+"-"+info_turnos[curso.getTurno()]["hora_fin"]
            dia = info_turnos[curso.getTurno()]["dia_inicio"]
            dia_2 = info_turnos[curso.getTurno()]["dia_fin"]
            if turno not in choques_salon[dia]:
                choques_salon[dia][turno] = {}

            if turno not in choques_salon[dia_2]:
                choques_salon[dia_2][turno] = {}


            if salon in choques_salon[dia][turno]:
                choques_salon[dia][turno][salon].append(curso)
                choques += 1
            else:
                choques_salon[dia][turno][salon] = []
                choques_salon[dia][turno][salon].append(curso)

            if salon in choques_salon[dia_2][turno]:
                choques_salon[dia_2][turno][salon].append(curso)
                choques += 1
            else:
                choques_salon[dia_2][turno][salon] = []
                choques_salon[dia_2][turno][salon].append(curso)

        return choques, choques_salon
    def mostrar (self,lista_materia):
        """
        Funcion mostrar\n
        Muestra todas las asignaciones del cromosoma\n
        """
        
        for asignacion in self.asignaciones:
            print(asignacion.mostrar())
    