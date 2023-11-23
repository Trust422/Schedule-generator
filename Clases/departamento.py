class Departamento:
    def __init__(self, nombre, cursos):
        self._nombre = nombre
        self._cursos = cursos

    #getters
    def get_nombre(self): return self._nombre

    def get_cursos(self): return self._cursos
    