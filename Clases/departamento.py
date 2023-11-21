class Departamento:
    def __init__(self, nombre, cursos):
        self._nombre = nombre
        self._cursos = cursos
    '''#setters
    def setNombre(self, nombre):
        self._nombre = nombre
    def setDepartamento(self, departamento):
        self._departamento = departamento
    def setAcademia(self, academia):
        self._academia = academia
    def setClave(self, clave):
        self._clave = clave'''
    #getters
    def get_nombre(self): return self._nombre

    def get_cursos(self): return self._cursos
    
    '''#metodos
    def mostrarMateria(self):
        return "Nombre: " + self._nombre + "\nDepartamento: " + self._departamento + "\nAcademia: " + self._academia + "\nClave: " + self._clave + "\n"'''