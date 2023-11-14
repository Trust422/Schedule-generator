import tkinter as tk
from tkinter import filedialog
import os

ventana_raiz= tk.Tk()
ventana_raiz.title("Penasando")
ventana_raiz.geometry("500x200")
ventana_raiz.iconbitmap("imagenes/icono.ico")
mostrar_nombre_archivo_prof=tk.StringVar()
mostrar_nombre_archivo_cursos=tk.StringVar()
mostrar_nombre_archivo_aulas=tk.StringVar()
turnoPreferido=tk.StringVar()
opcion=tk.IntVar()

#Se declara una funcion para cargar los archivos
def cargarArchivo(variableStringVar):#Se establece un parametro para establecer el nombre de una unica variable
    direccion_archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])#Encargada de abrir la ventana para seleccionar el archivo
    
    if direccion_archivo:
        nombre_archivo = os.path.basename(direccion_archivo)
        variableStringVar.set(nombre_archivo)

#Por el momento solo establece el turno de preferencia
def generar():
    if opcion.get()==1:
        turnoPreferido.set("v")
    elif opcion.get()==2:
        turnoPreferido.set("m")
    else:
        turnoPreferido.set("valio")
    print(opcion.get())
    print(turnoPreferido.get())

#Comienza la declaracion de los botones y la parte que vera el usuario en la primera interfaz

#Esta parte es la encargada de todo lo relacionado con los profesores
label_profesores=tk.Label(#Etiqueta para señalar lo correspondiente a los profesores
    ventana_raiz,
    text="Archivo profesores"
).grid(row=0,column=0,padx=5,pady=5)
label_mostrar_profesores=tk.Entry(#Se encarga de mostrar el nombre del archivo cargado para profesores
    ventana_raiz,
    bg="white",
    width=20,
    state="disabled",
    textvariable=mostrar_nombre_archivo_prof
).grid(row=1,column=0,padx=5,pady=5)
cargar_archivo_prof=tk.Button(#Boton para cargar el archivo
    ventana_raiz,
    text="Cargar Archivo",
    font=("Calibri",10),
    command=lambda: cargarArchivo(mostrar_nombre_archivo_prof)
).grid(row=1,column=1,padx=5,pady=5)

#Esta parte se encarga de mostrar lo relacionado a los cursos
label_cursos=tk.Label(#Etiqueta para identificar a los cursos
    ventana_raiz,
    text="Archivo cursos"
).grid(row=2,column=0,padx=5,pady=5)
label_mostrar_cursos=tk.Entry(#Se encarga de mostrar el nombre del archivo cargado para cursos
    ventana_raiz,
    bg="white",
    width=20,
    state="disabled",
    textvariable=mostrar_nombre_archivo_cursos
).grid(row=3,column=0,padx=5,pady=5)
cargar_archivo_cursos=tk.Button(#Boton para cargar el archivo
    ventana_raiz,
    text="Cargar Archivo",
    font=("Calibri",10),
    command=lambda: cargarArchivo(mostrar_nombre_archivo_cursos)
).grid(row=3,column=1,padx=5,pady=5)

#Esta parte se encarga de mostrar lo relacionado a las aulas
label_aula=tk.Label(#Etiqueta para identificar lo relacionado a las aulas
    ventana_raiz,
    text="Archivo aula"
).grid(row=4,column=0,padx=5,pady=5)
label_mostrar_aulas=tk.Entry(#Un entry que nos ayuda a mostrar el nombre del archivo cargado
    ventana_raiz,
    bg="white",
    width=20,
    state="disabled",
    textvariable=mostrar_nombre_archivo_aulas
).grid(row=5,column=0,padx=5,pady=5)
cargar_archivo_aulas=tk.Button(#Boton para cargar archivo
    ventana_raiz,
    text="Cargar Archivo",
    font=("Calibri",10),
    command=lambda: cargarArchivo(mostrar_nombre_archivo_aulas)
).grid(row=5,column=1,padx=5,pady=5)

#En este apartado es unicamente para capturar el turno preferido
label_horario_preferido=tk.Label(#Con esta label identifico lo anterior
    ventana_raiz,
    text="Horario preferido"
).grid(row=0,column=2,columnspan=2,padx=5,pady=5)
vespertino=tk.Radiobutton(#Boton para seleccionar el turno vespertino 
    ventana_raiz,
    text="Vespertino(1-5)",
    value=1,
    variable=opcion
).grid(row=1,column=2,padx=5,pady=5)
vespertino=tk.Radiobutton(#Boton para seleccionar el turno matutino
    ventana_raiz,
    text="Matutino(9-1)",
    value=2,
    variable=opcion
).grid(row=1,column=3,padx=5,pady=5)

#Este boton esta pensado para que ya realice toda la parte logica y que pase a la siguiente interfaz
generar_resultados=tk.Button(
    ventana_raiz,
    text="Generar",
    font=("Calibri",10),
    command=generar
).grid(row=5,column=2,columnspan=2,padx=5,pady=5)
ventana_raiz.mainloop()