class aula:
    def __init__(self, num):
        self._num_salon = num
        self._curso = None
        self._horario= ""
    #setters
    def setNumSalon(self, num_salon):
        self._num_salon = num_salon
    def setCurso(self, curso):
        self._curso = curso
    def setHorario(self, horario):
        self._horario = horario
    #getters
    def getNumSalon(self):
        return self._num_salon
    def getCurso(self):
        return self._curso
    def getHorario(self):
        return self._horario
    