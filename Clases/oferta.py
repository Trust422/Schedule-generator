from Clases.data import Data
from Clases.clase import Clase

import random as rnd

class Oferta:
    def __init__(self, data:Data):
        self._data = data
        self._clases = []
        self._n_conflictos = None
        self._fitness = -1
        self._n_clase = 0
        self._cambio_fitness = True

    def inicializar(self):
        departamentos = self._data.get_departamentos()

        for i in range(0, len(departamentos)):
            cursos = departamentos[i].get_cursos()
            for j in range(0, len(cursos)):
                nueva_clase = Clase(self._n_clase, departamentos[i], cursos[j])
                self._n_clase += 1
                nueva_clase.set_tiempo(self._data.get_tiempos()[rnd.randrange(0, len(self._data.get_tiempos()))])
                nueva_clase.set_salon(self._data.get_salones()[rnd.randrange(0, len(self._data.get_salones()))])
                nueva_clase.set_profesor(cursos[j].get_profesores()[rnd.randrange(0, len(cursos[j].get_profesores()))])
                self._clases.append(nueva_clase)
        
        return self

    def get_clases(self):
        self._cambio_fitness = True
        return self._clases

    def get_n_conflictos(self): return self._n_conflictos

    def get_fitness(self):
        if(self._cambio_fitness):
            self._fitness = self.calcular_fitness()
            self._cambio_fitness = False
        return self._fitness

    def calcular_fitness(self):
        self._n_conflictos = 0 
        clases = self.get_clases()
        for i in range(0, len(clases)):
            if (clases[i].get_salon().get_capacidad() < clases[i].get_curso().get_max_n_alumnos()):
                self._n_conflictos += 1
            for j in range(0, len(clases)):
                if j >= i:
                    if (clases[i].get_tiempo().get_id() == clases[j].get_tiempo().get_id()) and (clases[i].get_id() != clases[j].get_id()):
                        if clases[i].get_salon().get_numero() == clases[j].get_salon().get_numero(): 
                            self._n_conflictos += 1
                        if clases[i].get_profesor().get_id() == clases[j].get_profesor().get_id(): 
                            self._n_conflictos += 1
                
        return 1 / ((1.0 * self._n_conflictos + 1))
    
    def __str__(self):
        mi_str = f'# CONFLICTOS -> {self._n_conflictos} \n FITNESS -> {self._fitness} \n'
        for i in range(0, len(self._clases)-1):
            mi_str += str(self._clases[i]) + ", \n"
        mi_str += str(self._clases[len(self._clases)-1])
        return mi_str
