import pandas as pd

if __name__ == '__main__':
    aulas = pd.read_csv('Archivos de entrada/aulas.csv').values.tolist()
    cursos = pd.read_csv('Archivos de entrada/cursos.csv').values.tolist()
    profesores = pd.read_csv('Archivos de entrada/profesores.csv').values.tolist()
    tiempos = pd.read_csv('Archivos de entrada/tiempos.csv').values.tolist()

    f_tiempos = list()
    for i in range(0, len(tiempos)):
        aux = []
        aux.append(tiempos[i][0])
        aux.append(str(tiempos[i][1]+' '+tiempos[i][2]))
        f_tiempos.append(aux)

    departamentos = list()
    for i in range(0, len(cursos)):
        if cursos[i][2] not in departamentos:
            departamentos.append(cursos[i][2])

    print(aulas)
    print(cursos)
    print(profesores)
    print(f_tiempos)
    print(departamentos)