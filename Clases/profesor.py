class Profesor:
    def __init__(self, nombre, disponibilidad, areas):
        self._nombre = nombre
        self._disponibilidad = disponibilidad
        self._areas = areas
        self._horas_disponibles = 0
        self._num_clases=0
        self._cursosAsignados = []
    
    #setters
    def setNombre(self, nombre):
        self._nombre = nombre
    def setDisponibilidad(self, disponibilidad):
        self._disponibilidad = disponibilidad
    def setAreas(self, areas):
        self._areas = areas
    def setNumClases(self, num_clases):
        self._num_clases = num_clases
    def setCursosAsignados(self, cursosAsignados):
        self._cursosAsignados = cursosAsignados
    #getters
    def getNombre(self):
        return self._nombre
    def getDisponibilidad(self):
        return self._disponibilidad
    def getArea(self):
        return self._areas
    def getNumClases(self):
        return self._num_clases
    def getCursosAsignados(self):
        return self._cursosAsignados
    #metodos
    def agregarArea(self, area):
        self._areas.append(area)
    def agregarCurso(self, curso):
        self._cursosAsignados.append(curso)
        self._num_clases += 1
    def mostrarCursos(self):
        cursos = []
        if len(self._cursosAsignados) == 0:
            return "No tiene cursos asignados"
        for curso in self._cursosAsignados:
            cursos+=curso + " \n"
        return cursos
    def mostrarAreas(self):
        areas = ""
        for area in self._areas:
            areas+=area + " \n"
        return areas
    def mostrarDisponibilidad(self):
        disponibilidad = ""
        dias=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
        horas=["9:00 - 11:00", "11:00 - 13:00", "13:00 - 15:00", "15:00 - 17:00"]
        for dia in dias:
            for hora in horas:
                if self._disponibilidad[dias.index(dia)*4+horas.index(hora)] == "1":
                    disponibilidad+=dia + " " + hora + " \n"
        return disponibilidad
    def mostrar_profesor(self):
        return "Profesor :"+self._nombre + "\n --------------\n Disponibilidad:\n" + self.mostrarDisponibilidad() + "----------------\nAreas de enseñanza:  " +self.mostrarAreas()+  "Numero de clases asignadas:  " + str(self._num_clases) + "\nCursos asignados al profesor:  " + str(self.mostrarCursos()) + "\n"
    def perteneceArea(self, area):
        if self._area==area:
            return 1
        else:
            return -1
    def contarHoras(self):
        for i in range(len(self._disponibilidad)):
            if self._disponibilidad[i] == "1":
                self._horas_disponibles += 1
        return self._horas_disponibles
