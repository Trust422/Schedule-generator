from Clases.aula import Aula as Salon
from Clases.tiempo import Tiempo
from Clases.profesor import Profesor
from Clases.curso import Curso
from Clases.departamento import Departamento

class Data:

    SALONES = [['X1', 25], ['X2', 30], ['X3', 45],
               ['X4', 25], ['X5', 35], ['X6', 40],
               ['X7', 20], ['X8', 30], ['X9', 45],
               ['X10', 20], ['X11', 30], ['X12', 40]
                ]

    TIEMPOS = [['t1', 'LX 09:00 - 11:00'],
               ['t2', 'LX 11:00 - 13:00'],
               ['t12', 'XV 15:00 - 17:00'],
               ['t3', 'LX 13:00 - 15:00'],
               ['t4', 'LX 15:00 - 17:00'],
               ['t5', 'MJ 09:00 - 11:00'],
               ['t6', 'MJ 11:00 - 13:00'],
               ['t7', 'MJ 13:00 - 15:00'],
               ['t8', 'MJ 15:00 - 17:00'],
               ['t9', 'XV 09:00 - 11:00'],
               ['t10', 'XV 11:00 - 13:00'],
               ['t11', 'XV 13:00 - 15:00'],
                ]
    
    PROFESORES = [['p1', 'Samuel Jackson'],
                  ['p2', 'John Smith'],
                  ['p12', 'Ava Thomas'],
                  ['p3', 'Maria Rodriguez'],
                  ['p4', 'Emily Davis'],
                  ['p5', 'Michael Johnson'],
                  ['p6', 'Sophia Brown'],
                  ['p7', 'Robert Lee'],
                  ['p8', 'Emma White'],
                  ['p9', 'Daniel Harris'],
                  ['p10', 'Olivia Wilson'],
                  ['p11', 'William Taylor']
                ]
    
    def __init__(self) -> None:
        
        self.TAMANIO_POBLACION = 10
        self.MEJORES_HORARIOS = 1
        self.TAMANIO_TORNEO = 3
        self.TASA_MUTACION = 0.1

        self._salones = []
        self._tiempos = []
        self._profesores = []
        for i in range(0, len(self.SALONES)):
            self._salones.append(Salon(self.SALONES[i][0], self.SALONES[i][1]))
        for i in range(0, len(self.TIEMPOS)):
            self._tiempos.append(Tiempo(self.TIEMPOS[i][0], self.TIEMPOS[i][1]))
        for i in range(0, len(self.PROFESORES)):
            self._profesores.append(Profesor(self.PROFESORES[i][0], self.PROFESORES[i][1]))

        curso1 = Curso('c1', 'Logica matematica', [self._profesores[0], self._profesores[1]], 30)
        curso2 = Curso('c2', 'Fundamentos de programacion', [self._profesores[2], self._profesores[3]], 40)
        curso3 = Curso('c3', 'Ecuaciones diferenciales', [self._profesores[5], self._profesores[4]], 30)
        curso4 = Curso('c4', 'Sistemas dgitales', [self._profesores[5], self._profesores[3]], 30)
        curso5 = Curso('c5', 'Estructura de datos', [self._profesores[7], self._profesores[6]], 30)
        curso6 = Curso('c6', 'Programación estructurada', [self._profesores[6], self._profesores[8]], 45)
        curso7 = Curso('c7', 'Fundamentos de física', [self._profesores[10], self._profesores[9]], 30)
        curso8 = Curso('c8', 'Fundamentos de programacion', [self._profesores[11], self._profesores[1]], 30)
        curso9 = Curso('c9', 'Logica matematica', [self._profesores[0], self._profesores[11]], 45)
        curso10 = Curso('c10', 'Programacion para internet', [self._profesores[2], self._profesores[4]], 25)

        self._cursos = [curso1, curso2, curso3, curso4, curso5, curso6, curso7, curso8, curso9, curso10]

        dep1 = Departamento("Programacion", [curso2, curso8, curso5, curso6, curso10])
        dep2 = Departamento("Matematicas", [curso1, curso3, curso9])
        dep3 = Departamento("Ciencias", [curso4, curso7])

        self._departamentos = [dep1, dep2, dep3]

        self._n_clases = 0
        for i in range(0, len(self._departamentos)):
            self._n_clases += len(self._departamentos[i].get_cursos())
    
    def get_salones(self): return self._salones
    def get_profesores(self): return self._profesores
    def get_cursos(self): return self._cursos
    def get_departamentos(self): return self._departamentos
    def get_tiempos(self): return self._tiempos
    def get_n_clases(self): return self._n_clases