class materia:
    def __init__(self, nombre, departamento, academia, clave ):
        self._nombre = nombre
        self._departamento = departamento
        self._academia = academia
        self._clave = clave
    #setters
    def setNombre(self, nombre):
        self._nombre = nombre
    def setDepartamento(self, departamento):
        self._departamento = departamento
    def setAcademia(self, academia):
        self._academia = academia
    def setClave(self, clave):
        self._clave = clave
    #getters
    def getNombre(self):
        return self._nombre
    def getDepartamento(self):
        return self._departamento
    def getClave(self):
        return self._clave
    #metodos
    def mostrarMateria(self):
        return "Nombre: " + self._nombre + "\nDepartamento: " + self._departamento + "\nAcademia: " + self._academia + "\nClave: " + self._clave + "\n"