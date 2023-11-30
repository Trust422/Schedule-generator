import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import pandas as pd

x = pd.DataFrame({'A': [1, 2, 3, 10, 11,], 'B': [4, 5, 6, 12, 13], 'C': [7, 8, 9, 14, 15]})
y = pd.DataFrame({'A': [1, 2, 3, 10, 11,], 'B': [4, 5, 6, 12, 13], 'C': [7, 8, 9, 14, 15],'D': ['a','b','c','d','e']})

class Ventana_Secundaria:
    def __init__(self,ventana,data,flagProfesores,listaAreas):
        self.root=ventana
        self.root.withdraw()
        self.nueva_ventana=tk.Toplevel(self.root)
        self.nueva_ventana.title("Propuesta de horario")
        self.nueva_ventana.resizable(0,0)
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.bloquerCierre)
        self.frame_busqueda=tb.Frame(self.nueva_ventana)
        self.frame_busqueda.grid(row=1,column=2,padx=10,pady=10)
        self.item_buscar=tk.StringVar()
        self.datafr=data
        self.crear_tabla(self.nueva_ventana,self.datafr,"Horario propuesto")
        
        self.list_areas=listaAreas

        if flagProfesores == 1:
            messagebox.showwarning("Profesores insuficientes","Advertencia"+
                                   f"\nAl parecer no existen los suficientes profesores para las siguientes areas:\n {self.extraer_areas}")
            flagProfesores = 0
        self.boton_buscar=tb.Button(
            self.frame_busqueda,
            text="Buscar",
            bootstyle="info",
            command=self.buscar_item
        ).pack(side="left")

        self.entrada_busqueda=tb.Entry(
            self.frame_busqueda,
            width=20,
            textvariable=self.item_buscar,
            font=("Tahoma",10),
            bootstyle="info",
        ).pack(side="right",padx=10)

        self.boton_exportar_horario=tb.Button(
            self.nueva_ventana,
            text="Exportar horario",
            bootstyle="info",
            command=self.exportar_archivo
        ).grid(row=1,column=0,padx=10,pady=10)
        self.boton_regresar=tb.Button(
            self.nueva_ventana,
            text="Regresar",
            bootstyle="info",
            command=self.regresar_ventana_principal
        ).grid(row=1,column=1,padx=10,pady=10)

    def extraer_areas(self):
        for i in self.list_areas:
            messaje=i+"\n"
        return messaje
    
    def cargar_datos_a_mostrar(self,treeview,dataframe):
        columns=list(dataframe.columns)
        treeview.delete(*treeview.get_children())
        
        for index, row in dataframe.iterrows():
            treeview.insert("",index,values=list(row))
    
    def exportar_archivo(self):
        self.datafr.to_csv("Archivos de salida/salida.csv", encoding='latin-1')
        messagebox.showinfo("Exportacion","Se realizo la exportacion con exito")

    def buscar_item(self):
        df_filtrado=self.datafr[(self.datafr['Materia']==self.item_buscar.get()) | (self.datafr['Curso']==self.item_buscar.get()) | (self.datafr['Profesor']==self.item_buscar.get()) | (self.datafr['Salon']==self.item_buscar.get()) | (self.datafr['Turno']==self.item_buscar.get())]
        mostrar_busqueda=tk.Toplevel(self.nueva_ventana)
        mostrar_busqueda.title("Materias encontradas")
        mostrar_busqueda.resizable(0,0)
        self.crear_tabla(mostrar_busqueda,df_filtrado,"Resultado de la busqueda")

    def crear_tabla(self,localizacion,datos,NombreTabla):
        frame_mostrar_horario=tb.Frame(localizacion,bootstyle="light")
        frame_mostrar_horario.grid(padx=20,pady=20,row=0,column=0,columnspan=3)
        etiqueta=tb.Label(frame_mostrar_horario,text=NombreTabla,bootstyle="light-inverse").pack()
        
        tabla=ttk.Treeview(frame_mostrar_horario,columns=("NombreMateria","Curso","Profesor","Salon","Turno"), show="headings",bootstyle="secondary")
        tabla.heading("NombreMateria",text="Materia")
        tabla.heading("Curso", text="Curso")
        tabla.heading("Profesor",text="Profesor")
        tabla.heading("Salon",text="Salon")
        tabla.heading("Turno",text="Turno")

        tabla.column("NombreMateria",width=250,anchor="center")
        tabla.column("Curso",width=150,anchor="center")
        tabla.column("Profesor",width=250,anchor="center")
        tabla.column("Salon",width=70,anchor="center")
        tabla.column("Turno",width=150,anchor="center")

        barraVertical=ttk.Scrollbar(frame_mostrar_horario,orient="vertical",command=tabla.yview, bootstyle="dark-round")
        barraVertical.pack(side="right",fill="y")
        tabla.configure(yscrollcommand=barraVertical.set)
        
        self.cargar_datos_a_mostrar(tabla,datos)
        tabla.pack()


    def bloquerCierre(self):
        messagebox.showerror("Error de ventana", message="Por favor presione el boton de regresar...")

    def regresar_ventana_principal(self):
        self.nueva_ventana.destroy()
        self.root.deiconify()
        