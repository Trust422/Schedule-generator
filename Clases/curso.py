import profesor as pf
import materia as mt
class Curso:
    def __init__(self, profe, mate):
        self._profesor= profe
        self._materia=mate
        self._NRC=0

    def setProfesor(self, profesor):
        self._profesor=profesor

    def setMateria(self, materia):
        self._materia=materia

    def setNRC(self, NRC):
        self._NRC=NRC

    #getters

    def getProfesor(self):
        return self._profesor

    def getMateria(self):
        return self._materia
    
    def getNRC(self):
        return self._NRC
    
    #metodos
    def mostrar(self):
        return self._profesor.pf.getNombre()