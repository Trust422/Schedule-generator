#from tkinter import *
from tkinter import filedialog
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
import ttkbootstrap as tb
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
        self.ventana_raiz.resizable(0,0)
        self.ventana_raiz.iconbitmap("imagenes\icono.ico")

        #Creamos un frame para encapsular los elementos de la interfaz
        self.frame_cargar_datos=tb.Frame(self.ventana_raiz, bootstyle="secondary")
        self.frame_cargar_datos.pack(side="right",expand=True,fill=Y,padx=30,pady=30)
        
        #Se agrega una imagen para comenzar a estilizar nuestra interfaz
        self.imagen=tk.PhotoImage(file="imagenes\cuceiLogo.png")
        self.imagen_cucei= tk.Label(self.ventana_raiz,image=self.imagen).pack(side="left")
        


        #Esta parte es la encargada de todo lo relacionado con los profesores
        self.label_profesores=self.crearEtiquetasIdentificadoras("Archivo profesores",0,0,1)
        self.label_mostrar_profesores= self.crearEntryMostrarRuta(mostrar_nombre_archivo_prof,1,0)
        self.cargar_archivo_prof=self.crearBotonCargaArchivos(mostrar_nombre_archivo_prof, 'profesores',1,1)

        #Esta parte se encarga de mostrar lo relacionado a los cursos
        self.label_cursos=self.crearEtiquetasIdentificadoras("Archivo cursos",2,0,1)
        self.label_mostrar_cursos=self.crearEntryMostrarRuta(mostrar_nombre_archivo_cursos,3,0)
        self.cargar_archivo_cursos=self.crearBotonCargaArchivos(mostrar_nombre_archivo_cursos,'cursos',1,3)

        #Esta parte se encarga de mostrar lo relacionado a las aulas
        self.label_aula=self.crearEtiquetasIdentificadoras("Archivo aulas",4,0,1)
        self.label_mostrar_aulas=self.crearEntryMostrarRuta(mostrar_nombre_archivo_aulas,5,0)
        self.cargar_archivo_aulas=self.crearBotonCargaArchivos(mostrar_nombre_archivo_aulas,'aulas',1,5)
        
        #En este apartado es unicamente para capturar el turno preferido
        self.label_horario_preferido=self.crearEtiquetasIdentificadoras("Horario preferido",0,2,2)
        self.estilo=tb.Style()
        self.estilo.configure("info.TRadiobutton", background="#444444")
        self.vespertino=tb.Radiobutton(#Boton para seleccionar el turno vespertino 
            self.frame_cargar_datos,
            text="Vespertino(1-5)",
            value=1,
            variable=opcion,
            bootstyle="info",
            style="info.TRadiobutton"
        ).grid(row=1,column=2,padx=5,pady=5)
        self.matutino=tb.Radiobutton(#Boton para seleccionar el turno matutino
            self.frame_cargar_datos,
            text="Matutino(9-1)",
            value=2,
            variable=opcion,
            bootstyle="info",
            style="info.TRadiobutton"
        ).grid(row=1,column=3,padx=5,pady=5)

        #Este boton esta pensado para que ya realice toda la parte logica y que pase a la siguiente interfaz
        self.generar_resultados=tb.Button(
            self.frame_cargar_datos,
            text="Generar",
            state="disabled",
            command=self.generar,
            bootstyle="info"
        )
        self.generar_resultados.grid(row=5,column=2,columnspan=2,padx=5,pady=5)

        #Crear un pequeño menu para mostrar ayuda en caso de que se necesite y los creditos.
        self.menu_principal=tk.Menu(self.ventana_raiz)
        self.ventana_raiz.config(menu=self.menu_principal)

        self.menu_ayuda=tk.Menu(self.menu_principal, tearoff=0)
        self.menu_ayuda.add_command(label="Boton cargar archivos",command=self.mostrar_ayuda_cargar_archivos)
        self.menu_ayuda.add_command(label="Boton generar",command=self.mostrar_ayuda_generar)
        self.menu_ayuda.add_command(label="Segunda ventana",command=self.mostrar_ayuda_segunda_ventana)
        self.menu_ayuda.add_command(label="Otros",command=self.mostrar_ayuda_otros)

        self.menu_creditos=tk.Menu(self.menu_principal, tearoff=0)
        self.menu_creditos.add_command(label="Creditos",command=self.mostrar_creditos)

        self.menu_principal.add_cascade(label="Ayuda", menu=self.menu_ayuda)
        self.menu_principal.add_cascade(label="Creditos", menu=self.menu_creditos)
    
    #Boton para cargar el archivo
    def crearBotonCargaArchivos(self,mostrar_nombre_archivo,clave,colum,row):
        boton=tb.Button(
            self.frame_cargar_datos,
            text="Cargar Archivo",
            command=lambda: self.cargarArchivo(mostrar_nombre_archivo,clave),
            bootstyle="info"
        ).grid(row=row,column=colum,padx=5,pady=5)
        return boton
    
    #Se creo una funcion para encapsular las etiquetas que sirven para identificar la carga de los archivos
    def crearEtiquetasIdentificadoras(self,textoMostrado,row,colum,columsp):
        label=tb.Label(
            self.frame_cargar_datos,
            text=textoMostrado,
            font=("Tahoma",10),
            bootstyle="secondary, inverse"
        ).grid(row=row,column=colum,padx=5,pady=5,columnspan=columsp)
        return label
    
    #Se creo una funcion para encapsular los entrys, encargados de capturar la ruta de los archivos
    def crearEntryMostrarRuta(self,variableArchivo,row,colum):
        entry=tb.Entry(
            self.frame_cargar_datos,
            width=20,
            state="disabled",
            textvariable=variableArchivo,
            font=("Tahoma",10),
            bootstyle=INFO,
        ).grid(row=row,column=colum,padx=5,pady=5)
        return entry
    
    #Se declara una funcion para cargar los archivos
    def cargarArchivo(self,variableStringVar,ruta_archivo,):#Se establece un parametro para establecer el nombre de una unica variable y guardar la ruta de los archivos
        direccion_archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])#Encargada de abrir la ventana para seleccionar el archivo
        if direccion_archivo:
            rutas_archivos[ruta_archivo]=direccion_archivo
            nombre_archivo = os.path.basename(direccion_archivo)
            variableStringVar.set(nombre_archivo)
            self.verificar_ejecucion()#Ademas, se establece una funcion para verificar que si se carguen todos los archivos y activar el boton de generar
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
    
    #Funcion que se encarga de mostrar los credits, cuando es solicitada
    def mostrar_creditos(self):
        braulio="Administrador\nBraulio Emmanuel Hernandez Martin\nbraulio.hmartin@alumnos.udg.mx\n"
        Marcos="Desarrollador Backend\nMarcos Castellanos Villaseñor\nmarcos.castellanos7815@alumnos.udg.mx\n"
        Edgar="Desarrollador Frontend\nEdgar Antonio Sanchez Nuñez\nedgar.sanchez6029@alumnos.udg.mx\n"
        Luis="Tester\nLuis Felipe Aguiñiga Haro\nluis.aguiniga8889@alumnos.udg.mx\n"
        Separacion="--------------------------------------------------\n"
        Messagebox.show_info(braulio+Separacion+Marcos+Separacion+Edgar+Separacion+Luis)
    
    #Funciones encargadas de mostrar miniayudas para el usuario
    def mostrar_ayuda_cargar_archivos(self):
        Messagebox.ok("El boton tiene la funcionalidad de abrir el explorador de archivos para cargar el csv con datos."+
                      "\nEs indispensable que el archivo cargado sea csv.")
    def mostrar_ayuda_generar(self):
        Messagebox.ok("El boton generar, es el encargado de generarte un horario."+
                      "\nEste se activara hasta que todos los archivos hayan sido cargados.")
    def mostrar_ayuda_segunda_ventana(self):
        Messagebox.ok("La segunda ventana es la encargada de mostrarte el horario propuesto, segun los archivos cargados."+
                      "\nEsta no cerrara, a menos que presiones el boton 'Regresar'.")
    def mostrar_ayuda_otros(self):
        Messagebox.ok("Si desea reportar algun error de la aplicacion o tienes dudas al respecto, "+
                      "no dude comunicarse con cualquiera de nosotros mediante los correos que se muestran en 'Creditos'.")
        
root= tb.Window(themename="darkly")
rutas_archivos={'profesores' : '', 'cursos':'','aulas':''}
mostrar_nombre_archivo_prof=tk.StringVar()
mostrar_nombre_archivo_cursos=tk.StringVar()
mostrar_nombre_archivo_aulas=tk.StringVar()
turnoPreferido=tk.StringVar()
opcion=tk.IntVar()
app=Ventana_Principal(root)

root.mainloop()