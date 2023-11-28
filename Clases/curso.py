import profesor as pf
import materia as mt
class Curso:
    def __init__(self, profe: pf, mate: mt, salon, turno):
        """
        Constructor de la clase curso \n
        parametros: \n
        profe: profesor del curso tipo profesor
        mate: materia del curso tipo materia
        salon: salon del curso tipo str (ejem: IL354)
        turno: turno del curso tipo str (ejem: l-x 11-13)
        """
        self._profesor= profe
        self._materia=mate
        self._NRC=0
        self._salon=salon
        self._turno=turno
        self.crearNRC()

    def setProfesor(self, profesor: pf):
        """
        Cambia el profesor del curso\n
        parametros:\n
        profesor: profesor a cambiar tipo profesor
        """
        self._profesor=profesor
    def crearNRC(self):
        """
        Crea un NRC para el curso de manera automatica tipo str (ejem:IL35419lx1113)\n
        el NRC se crea con la clave de la materia, los dos primeros digitos del salon, el primer digito del turno, los dos digitos del inicio del turno y los dos digitos del final del turno
        """
        self._NRC=self._materia.getClave()+self._salon[2:4]+self._turno[0:1]+self._turno[2:3] + self._turno[4:6] + self._turno[7:9]

    def setMateria(self, materia):
        """
        Cambia la materia del curso
        parametros:
        materia: materia a cambiar tipo materia
        """
        self._materia=materia

    def setNRC(self, NRC: int):
        """
        Cambia el NRC del curso\n
        parametros:\n
        NRC: NRC a cambiar tipo int
        """
        self._NRC=NRC
    def setTurno(self, turno):
        """
        Cambia el turno del curso\n
        parametros:\n
        turno: turno a cambiar tipo str (ejem: l-x 11-13)
        """
        self._turno=turno
    #getters

    def getProfesor(self) -> pf:
        """
        Regresa el profesor del curso\n
        Regresa un objeto de tipo profesor
        """

        return self._profesor

    def getMateria(self) -> mt:
        """
        Regresa la materia del curso \n
        Regresa un objeto de tipo materia
        """
        return self._materia
    
    def getNRC(self) -> int:
        """
        Regresa el NRC del curso\n
        regresa un numero entero
        """
        return self._NRC
    
    def getSalon(self) -> str:
        """
        Regresa el salon del curso\n
        regresa un string (ejem: x004)
        """
        return self._salon
    
    def getTurno(self) -> str:
        """
        Regresa el turno del curso\n
        regresa un string (ejem: l-x 11-13)
        """
        return self._turno
    #metodos
    def mostrar(self):
        """
        Regresa una cadena con la informacion del curso\n
        (materia, turno, profesor, aula, NRC)
        """
        return (f"Materia: {self._materia.getNombre()} + turno: {self.getTurno()} + Profesor: {self._profesor} + aula: {self._salon} + NRC: {self._NRC}")