class Profesor:
    def __init__(self, id, nombre, disponibilidad):
        self._nombre = nombre
        self._id = id
        self._disponibilidad = disponibilidad
    
    #getters
    def get_id(self): return self._id

    def get_nombre(self): return self._nombre

    def get_disponibilidad(self): return self._disponibilidad

    def __str__(self): return self._nombre
    