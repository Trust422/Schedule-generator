class Aula:
    def __init__(self, numero, capacidad):
        self._num_salon = numero
        self._capacidad = capacidad

    '''#setters
    def setNumSalon(self, num_salon):
        self._num_salon = num_salon
    def setCurso(self, curso):
        self._curso = curso
    def setHorario(self, horario):
        self._horario = horario'''
    
    #getters
    def get_numero(self): return self._num_salon
    
    def get_capacidad(self): return self._capacidad