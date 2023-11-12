max_alumnos = 40
class curso:
    def __init__(self, nombre, area):
        self._nombre = nombre
        self._area = area
        self._profesor = None
        self._horario = ""
        self._ID = ""
        self._salon = ""
        self._importancia = 0
    #setters
    def setNombre(self, nombre):
        self._nombre = nombre
    def setArea(self, area):
        self._area = area
    def setProfesor(self, profesor):
        self._profesor = profesor
    def setHorario(self, horario):
        self._horario = horario
    def setID(self, ID):
        self._ID = ID
    def setSalon(self, salon):
        self._salon = salon
    def setImportancia(self, importancia):
        self._importancia = importancia
    #getters
    def getNombre(self):
        return self._nombre
    def getArea(self):
        return self._area
    def getProfesor(self):
        return self._profesor
    def getHorario(self):
        return self._horario
    def getID(self):
        return self._ID
    def getSalon(self):
        return self._salon
    def getImportancia(self):
        return self._importancia
    #metodos
    