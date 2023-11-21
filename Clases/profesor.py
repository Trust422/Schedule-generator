class Profesor:
    def __init__(self, id, nombre):
        self._nombre = nombre
        self._id = id
        
    '''#setters
    def setNombre(self, nombre):
        self._nombre = nombre
    def setDisponibilidad(self, disponibilidad):
        self._disponibilidad = disponibilidad
    def setAreas(self, areas):
        self._areas = areas
    def setNumClases(self, num_clases):
        self._num_clases = num_clases
    def setCursosAsignados(self, cursosAsignados):
        self._cursosAsignados = cursosAsignados'''
    
    #getters
    def get_id(self): return self._id

    def get_nombre(self): return self._nombre

    def __str__(self): return self._nombre

    '''#metodos
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
        return disponibilidad'''
    
    