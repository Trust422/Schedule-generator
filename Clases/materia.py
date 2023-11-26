class Materia:
    def __init__(self, nombre, departamento, academia, clave ):
        """
        Constructor de la clase materia \n
        parametros: \n
        nombre: nombre de la materia tipo str (ejem: programacion estructurada)
        departamento: departamento de la materia tipo str (ejem: ciencias de la computacion)
        academia: academia de la materia tipo str (ejem: Programacion)
        clave: clave de la materia tipo str (ejem: IL345)"""
        self._nombre = nombre
        self._departamento = departamento
        self._academia = academia
        self._clave = clave
    #setters
    def setNombre(self, nombre):
        """
        Cambia el nombre de la materia\n
        parametros:\n
        nombre: nombre de la materia tipo str (ejem: programacion estructurada)
        """
        self._nombre = nombre
    def setDepartamento(self, departamento):
        """
        Cambia el departamento de la materia\n
        parametros:\n
        departamento: departamento de la materia tipo str (ejem: ciencias de la computacion)
        """
        self._departamento = departamento
    def setAcademia(self, academia):
        """
        Cambia la academia de la materia\n
        parametros:\n
        academia: academia de la materia tipo str (ejem: Programacion)
        """
        self._academia = academia
    def setClave(self, clave):
        """
        Cambia la clave de la materia\n
        parametros:\n
        clave: clave de la materia tipo str (ejem: IL345)
        """
        self._clave = clave
    #getters
    def getNombre(self) -> str:
        """
        Regresa el nombre de la materia\n
        regresa un string (ejem: programacion estructurada)
        """
        return self._nombre
    def getDepartamento(self) -> str:
        """
        Regresa el departamento de la materia\n
        regresa un string (ejem: ciencias de la computacion)
        """
        return self._departamento
    def getClave(self) -> str:
        """
        Regresa la clave de la materia\n
        regresa un string (ejem: IL345)
        """
        return self._clave
    def getAcademia(self) -> str:
        """
        Regresa la academia de la materia\n
        regresa un string (ejem: Programacion)
        """
        return self._academia
    #metodos
    def mostrarMateria(self):
        """
        Regresa un string con la informacion de la materia
        (Nombre, Departamento, Academia, Clave)
        """
        return "Nombre: " + self._nombre + "\nDepartamento: " + self._departamento + "\nAcademia: " + self._academia + "\nClave: " + self._clave + "\n"