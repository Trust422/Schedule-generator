#from tkinter import *
from tkinter import filedialog, PhotoImage, messagebox
import tkinter as tk
import Ventana_secundaria as ves
import os

#Intrucciones para dirigirnos al directorio del script que se esta ejecutando
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

#Creacion de la ventana principal
class Ventana_Principal:
    def __init__(self, raiz):
        #Comienza la declaracion de los botones y la parte que vera el usuario en la primera interfaz
        self.ventana_raiz=raiz
        self.ventana_raiz.title("Generador de horarios")
        #self.ventana_raiz.geometry("500x230")
        self.ventana_raiz.iconbitmap("imagenes\icono.ico")
        self.frame_cargar_datos=tk.Frame(self.ventana_raiz)
        self.frame_cargar_datos.pack(side="right")
        self.imagen=tk.PhotoImage(file="imagenes\cuceiLogo2.png")
        self.imagen_cucei= tk.Label(self.ventana_raiz,image=self.imagen).pack(side="left")
        #Esta parte es la encargada de todo lo relacionado con los profesores
        self.label_profesores=tk.Label(#Etiqueta para señalar lo correspondiente a los profesores
            #self.ventana_raiz,
            self.frame_cargar_datos,
            text="Archivo profesores"
        ).grid(row=0,column=0,padx=5,pady=5)
        self.label_mostrar_profesores=tk.Entry(#Se encarga de mostrar el nombre del archivo cargado para profesores
            #self.ventana_raiz,
            self.frame_cargar_datos,
            bg="white",
            width=20,
            state="disabled",
            textvariable=mostrar_nombre_archivo_prof
        ).grid(row=1,column=0,padx=5,pady=5)
        self.cargar_archivo_prof=tk.Button(#Boton para cargar el archivo
            #self.ventana_raiz,
            self.frame_cargar_datos,
            text="Cargar Archivo",
            font=("Calibri",10),
            command=lambda: self.cargarArchivo(mostrar_nombre_archivo_prof, 'profesores')
        ).grid(row=1,column=1,padx=5,pady=5)

        #Esta parte se encarga de mostrar lo relacionado a los cursos
        self.label_cursos=tk.Label(#Etiqueta para identificar a los cursos
            #self.ventana_raiz,
            self.frame_cargar_datos,
            text="Archivo cursos"
        ).grid(row=2,column=0,padx=5,pady=5)
        self.label_mostrar_cursos=tk.Entry(#Se encarga de mostrar el nombre del archivo cargado para cursos
            #self.ventana_raiz,
            self.frame_cargar_datos,
            bg="white",
            width=20,
            state="disabled",
            textvariable=mostrar_nombre_archivo_cursos
        ).grid(row=3,column=0,padx=5,pady=5)
        self.cargar_archivo_cursos=tk.Button(#Boton para cargar el archivo
            #self.ventana_raiz,
            self.frame_cargar_datos,
            text="Cargar Archivo",
            font=("Calibri",10),
            command=lambda: self.cargarArchivo(mostrar_nombre_archivo_cursos,'cursos')
        ).grid(row=3,column=1,padx=5,pady=5)

        #Esta parte se encarga de mostrar lo relacionado a las aulas
        self.label_aula=tk.Label(#Etiqueta para identificar lo relacionado a las aulas
            #self.ventana_raiz,
            self.frame_cargar_datos,
            text="Archivo aula"
        ).grid(row=4,column=0,padx=5,pady=5)
        self.label_mostrar_aulas=tk.Entry(#Un entry que nos ayuda a mostrar el nombre del archivo cargado
            #self.ventana_raiz,
            self.frame_cargar_datos,
            bg="white",
            width=20,
            state="disabled",
            textvariable=mostrar_nombre_archivo_aulas
        ).grid(row=5,column=0,padx=5,pady=5)
        self.cargar_archivo_aulas=tk.Button(#Boton para cargar archivo
            #self.ventana_raiz,
            self.frame_cargar_datos,
            text="Cargar Archivo",
            font=("Calibri",10),
            command=lambda: self.cargarArchivo(mostrar_nombre_archivo_aulas,'aulas')
        ).grid(row=5,column=1,padx=5,pady=5)

        #En este apartado es unicamente para capturar el turno preferido
        self.label_horario_preferido=tk.Label(#Con esta label identifico lo anterior
            #self.ventana_raiz,
            self.frame_cargar_datos,
            text="Horario preferido"
        ).grid(row=0,column=2,columnspan=2,padx=5,pady=5)
        self.vespertino=tk.Radiobutton(#Boton para seleccionar el turno vespertino 
            #self.ventana_raiz,
            self.frame_cargar_datos,
            text="Vespertino(1-5)",
            value=1,
            variable=opcion
        ).grid(row=1,column=2,padx=5,pady=5)
        self.matutino=tk.Radiobutton(#Boton para seleccionar el turno matutino
            #self.ventana_raiz,
            self.frame_cargar_datos,
            text="Matutino(9-1)",
            value=2,
            variable=opcion
        ).grid(row=1,column=3,padx=5,pady=5)

        #Este boton esta pensado para que ya realice toda la parte logica y que pase a la siguiente interfaz
        self.generar_resultados=tk.Button(
            #self.ventana_raiz,
            self.frame_cargar_datos,
            text="Generar",
            font=("Calibri",10),
            #state="disabled",
            state="normal",
            command=self.generar
        )
        self.generar_resultados.grid(row=5,column=2,columnspan=2,padx=5,pady=5)

        #Crear un pequeño menu para mostrar algunas cosas
        self.menu_principal=tk.Menu(self.ventana_raiz)
        self.ventana_raiz.config(menu=self.menu_principal)

        self.menu_ayuda=tk.Menu(self.menu_principal, tearoff=0)
        self.menu_ayuda.add_command(label="Agregar Archivos")
        self.menu_ayuda.add_command(label="Agregar ")
        self.menu_ayuda.add_command(label="Archivos")

        self.menu_creditos=tk.Menu(self.menu_principal, tearoff=0)
        self.menu_creditos.add_command(label="Creditos",command=self.mostrar_creditos)

        self.menu_principal.add_cascade(label="Ayuda", menu=self.menu_ayuda)
        self.menu_principal.add_cascade(label="Creditos", menu=self.menu_creditos)

    #Se declara una funcion para cargar los archivos
    def cargarArchivo(self,variableStringVar,ruta_archivo):#Se establece un parametro para establecer el nombre de una unica variable y guardar la ruta de los archivos
        direccion_archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])#Encargada de abrir la ventana para seleccionar el archivo
        if direccion_archivo:
            rutas_archivos[ruta_archivo]=direccion_archivo
            nombre_archivo = os.path.basename(direccion_archivo)
            variableStringVar.set(nombre_archivo)
            self.verificar_ejecucion()
            print(rutas_archivos[ruta_archivo])
    #Por el momento solo establece el turno de preferencia
    def generar(self):
        if opcion.get()==1:
            turnoPreferido.set("v")
        elif opcion.get()==2:
            turnoPreferido.set("m")
        else:
            turnoPreferido.set("no se asigno ningun valor")
        self.abrir_ventana_secundaria()
        print(opcion.get())
        print(turnoPreferido.get())
    
    #Se agrego una funcion para crear la segunda interfaz
    def abrir_ventana_secundaria(self):
        ventana_secu=ves.Ventana_Secundaria(self.ventana_raiz)
    
    #Se creo una funcion que se encarga de verificar que si se hayan cargado archivos a la interfaz
    def verificar_ejecucion(self):
        if rutas_archivos["profesores"] !="" and rutas_archivos["cursos"] !="" and rutas_archivos["aulas"] !="":
            self.generar_resultados.configure(state="normal")
        else:
            self.generar_resultados.configure(state="disabled")
    
    def mostrar_creditos(self):
        messagebox.showinfo("Creditos",message="Administrador\nBraulio Emmanuel Hernandez Martin\nbraulio.hmartin@alumnos.udg.mx\nDesarrollador Backend\nMarcos Castellanos Villaseñor\nmarcos.castellanos7815@alumnos.udg.mx\nDesarrollador Frontend\nEdgar Antonio Sanchez Nuñez\nedgar.sanchez6029@alumnos.udg.mx\nTester\nLuis Felipe Aguiñiga Haro\nluis.aguiniga8889@alumnos.udg.mx")
        
root= tk.Tk()
rutas_archivos={'profesores' : '', 'cursos':'','aulas':''}
mostrar_nombre_archivo_prof=tk.StringVar()
mostrar_nombre_archivo_cursos=tk.StringVar()
mostrar_nombre_archivo_aulas=tk.StringVar()
turnoPreferido=tk.StringVar()
opcion=tk.IntVar()
app=Ventana_Principal(root)

root.mainloop()