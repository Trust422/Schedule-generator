cantidad_aulas=20
class Oferta:
    def __init__(self):
        self._edificio = [[[None] * cantidad_aulas for _ in range(5)] for _ in range(4)]

    #setters

    #getters

    #metodos
    def obtener_clase(self, salon, dia, hora):
        clase_actual = self._edificio[hora][dia][salon]

        if clase_actual is not None:
            return clase_actual.getNRC()
        else:
            return None
    
    def asignar_clase(self, hora, dia, salon, clase):
        self._edificio[hora][dia][salon] = clase

    def mostrar_horario_clases(self):
        dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
        horas = ["9-11", "11-13", "13-15", "15-17"]
        cadena = ""
        for i in range (len(dias)):
            for j in range (len(horas)):
                cadena += f"\nHorario para el día {dias[i]} a la hora {horas[j]}:\n"
                for salon in range(cantidad_aulas):
                    clase_actual = self.obtener_clase(salon, i, j)
                    cadena += f"Salón {salon + 1}: {clase_actual}\n"
        return cadena



