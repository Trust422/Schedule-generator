import profesor as pf
import materia as mt
class Curso:
    def __init__(self, profe: pf, mate: mt, salon, turno):
        self._profesor= profe
        self._materia=mate
        self._NRC=0
        self._salon=salon
        self._turno=turno

    def setProfesor(self, profesor: pf):
        self._profesor=profesor

    def setMateria(self, materia):
        self._materia=materia

    def setNRC(self, NRC: int):
        self._NRC=NRC

    #getters

    def getProfesor(self) -> pf:
        return self._profesor

    def getMateria(self) -> mt:
        return self._materia
    
    def getNRC(self) -> int:
        return self._NRC
    
    def getSalon(self) -> str:
        return self._salon
    
    def getTurno(self) -> str:
        return self._turno
    #metodos
    def mostrar(self):
        return self._profesor.getNombre() + "\n" +self._materia.getNombre() + "\n" +self.getSalon() +"\n" + self.getTurno()+ "\n\n" 
    