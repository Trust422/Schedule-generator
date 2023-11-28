class Profesor:
    def __init__(self, nombre, disponibilidad, area):
        """
        Constructor de la clase profesor \n
        parametros: \n
        nombre: nombre del profesor tipo str (ejem: Juan Perez) \n
        disponibilidad: disponibilidad del pofesor una cadena binaria de 20 caracteres 5 grupos(dia) de 4 bits(hora) \n
        area: areas de enseñanza del profesor tipo lista (ejem: ["Programacion"]

        """
        self._nombre = nombre
        self._disponibilidad = disponibilidad
        self._area = area
        self._horas_disponibles = 0
        self._num_clases=0
        self._cursosAsignados = []
    
    #setters
    def setNombre(self, nombre):
        """
        Cambia el nombre del profesor\n
        parametros:\n
        nombre: nombre del profesor tipo str (ejem: Juan Perez)
        """
        self._nombre = nombre
    def setDisponibilidad(self, disponibilidad):
        """
        Cambia la disponibilidad del profesor\n
        parametros:\n
        disponibilidad: disponibilidad del pofesor una cadena binaria de 20 caracteres 5 grupos(dia) de 4 bits(hora)
        """
        self._disponibilidad = disponibilidad
    def setAreas(self, area):
        """
        Cambia el area de enseñanza del profesor\n
        parametros:\n
        areas: areas de enseñanza del profesor tipo lista (ejem: ["Programacion"]
        """
        self._areas = area
    def setNumClases(self, num_clases):
        """
        Cambia el numero de clases asignadas al profesor\n
        parametros:\n
        num_clases: numero de clases asignadas al profesor tipo int (ejem: 4)"""
        self._num_clases = num_clases
    def setCursosAsignados(self, cursosAsignados):
        """
        Cambia los cursos asignados al profesor\n
        parametros:\n
        cursosAsignados: cursos asignados al profesor tipo lista (ejem: [programacion, matematicas])"""
        self._cursosAsignados = cursosAsignados
    #getters
    def getNombre(self) -> str:
        """
        Regresa el nombre del profesor\n
        regresa un string (ejem: Juan Perez)
        """
        return self._nombre
    def getDisponibilidad(self) -> str:
        """
        Regresa la disponibilidad del profesor\n
        regresa una cadena binaria de 20 caracteres 5 grupos(dia) de 4 bits(hora)
        """
        return self._disponibilidad
    def getArea(self) -> str:
        """
        Regresa el area de enseñanza del profesor\n
        regresa una lista (ejem: ["Programacion"]
        """
        return self._area
    def getNumClases(self)  -> int:
        """
        Regresa el numero de clases asignadas al profesor\n
        regresa un int (ejem: 4)
        """
        return self._num_clases
    def getCursosAsignados(self) -> list:
        """
        Regresa los cursos asignados al profesor\n  
        regresa una lista (ejem: [programacion, matematicas])
        """
        return self._cursosAsignados
    #metodos
    def agregarArea(self, area):
        """
        Agrega un area de enseñanza al profesor\n
        parametros:\n
        area: area de enseñanza del profesor tipo str (ejem: Programacion) """
        self._areas.append(area)
    def agregarCurso(self, curso):
        """
        Agrega un curso al profesor\n
        parametros:\n
        curso: curso asignado al profesor tipo str (ejem: programacion) \n
        e incrementa el num_clases en 1
        """

        self._cursosAsignados.append(curso)
        self._num_clases += 1
    def mostrarCursos(self) -> list:
        """ 
        Regresa los cursos asignados al profesor\n
        regresa una lista (ejem: [programacion, matematicas])
        """
        cursos = []
        if len(self._cursosAsignados) == 0:
            return "No tiene cursos asignados"
        for curso in self._cursosAsignados:
            cursos+=curso + " \n"
        return cursos
    def mostrarAreas(self) -> list:
        """
        Regresa las areas de enseñanza del profesor\n
        regresa una string (ejem: Programacion)
        """
        return self._area
    def mostrarDisponibilidad(self) -> str:
        """
        Regresa la disponibilidad del profesor de manera mas facil de leer\n
        EJEMPLO: \n
        Lunes 9:00 - 11:00 \n
        Lunes 11:00 - 13:00 \n
        Lunes 13:00 - 15:00 \n
        Lunes 15:00 - 17:00 \n
        Miércoles 9:00 - 11:00 \n
        Miércoles 11:00 - 13:00 \n
        etc... \n
        """
        disponibilidad = ""
        dias=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
        horas=["9:00 - 11:00", "11:00 - 13:00", "13:00 - 15:00", "15:00 - 17:00"]
        for dia in dias:
            for hora in horas:
                if self._disponibilidad[dias.index(dia)*4+horas.index(hora)] == "1":
                    disponibilidad+=dia + " " + hora + " \n"
        return disponibilidad
    def mostrar_profesor(self) -> str:
        """
        Regresa los datos del profesor de manera mas facil de leer\n
        EJEMPLO: \n
        Profesor :Juan Perez \n
        -------------- \n
        Disponibilidad: \n
        Lunes 9:00 - 11:00 \n
        Lunes 11:00 - 13:00 \n
        Lunes 13:00 - 15:00 \n
        Lunes 15:00 - 17:00 \n
        ---------------- \n
        Areas de enseñanza:  Programacion \n
        Numero de clases asignadas:  2 \n
        Cursos asignados al profesor:  Programacion \n

        """
        return "Profesor :"+self._nombre + "\n --------------\n Disponibilidad:\n" + self.mostrarDisponibilidad() + "----------------\nAreas de enseñanza:  " +self.mostrarAreas()+  "\n---------------------\n-Numero de clases asignadas:  " + str(self._num_clases) + "\n---------------------\nCursos asignados al profesor:  " + str(self.mostrarCursos()) + "\n"
    def perteneceArea(self, area)-> int:
        """
        Verifica si el profesor pertenece al area de enseñanza\n
        parametros:\n
        area: area de enseñanza del profesor tipo str (ejem: Programacion) \n
        regresa 1 si pertenece al area y -1 si no pertenece"""
        if self._area==area:
            return 1
        else:
            return -1
    def contarHoras(self) -> int:
        """
        Cuenta las horas disponibles del profesor\n
        regresa un int (ejem: 20)
        """
        for i in range(len(self._disponibilidad)):
            if self._disponibilidad[i] == "1":
                self._horas_disponibles += 1
        return self._horas_disponibles
