import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class Ventana_Secundaria:
    def __init__(self,ventana):
        self.root=ventana
        self.root.withdraw()
        self.nueva_ventana=tk.Toplevel(self.root)
        self.nueva_ventana.title("Propuesta de horario")
        self.nueva_ventana.resizable(0,0)

        self.frame_mostrar_horario=tb.Frame(self.nueva_ventana,bootstyle="light")
        self.frame_mostrar_horario.grid(padx=20,pady=20,row=0,column=0,columnspan=2)
        self.etiqueta=tb.Label(self.frame_mostrar_horario,text="Horario propuesto",bootstyle="light-inverse").pack()
        self.nueva_ventana.protocol("WM_DELETE_WINDOW", self.bloquerCierre)

        self.tabla=ttk.Treeview(self.frame_mostrar_horario,columns=("Clave","NombreMateria","Profesor","L","M","I","J","V","Hora","Aula"), show="headings",bootstyle="secondary")
        self.tabla.heading("Clave",text="Clave")
        self.tabla.heading("NombreMateria",text="NombreMateria")
        self.tabla.heading("Profesor",text="Profesor")
        self.tabla.heading("L",text="L")
        self.tabla.heading("M",text="M")
        self.tabla.heading("I",text="I")
        self.tabla.heading("J",text="J")
        self.tabla.heading("V",text="V")
        self.tabla.heading("Hora",text="Hora")
        self.tabla.heading("Aula",text="Aula")

        self.tabla.column("Clave",width=100)
        self.tabla.column("NombreMateria",width=200)
        self.tabla.column("Profesor",width=150)
        self.tabla.column("L",width=50)
        self.tabla.column("M",width=50)
        self.tabla.column("I",width=50)
        self.tabla.column("J",width=50)
        self.tabla.column("V",width=50)
        self.tabla.column("Hora",width=70)
        self.tabla.column("Aula",width=70)

        self.barraVertical=ttk.Scrollbar(self.frame_mostrar_horario,orient="vertical",command=self.tabla.yview, bootstyle="dark-round")
        self.barraVertical.pack(side="right",fill="y")
        self.tabla.configure(yscrollcommand=self.barraVertical.set)
        
        self.cargar_datos_a_mostrar(self.tabla)
        self.tabla.pack()
        
        self.boton_exportar_horario=tb.Button(
            self.nueva_ventana,
            text="Exportar horario",
            bootstyle="info",
        ).grid(row=1,column=0,padx=10,pady=10)
        self.boton_regresar=tb.Button(
            self.nueva_ventana,
            text="Regresar",
            bootstyle="info",
            command=self.regresar_ventana_principal
        ).grid(row=1,column=1,padx=10,pady=10)
    def cargar_datos_a_mostrar(self,treeview):
        datos=[("218602962","Analisis de Algoritmos","Jorge Ernesto","","1","","1","","7-9","X14"),
               ("123456789", "Introducción a la Programación", "María González", "", "2", "", "3", "", "10-12", "X20"),
                ("987654321", "Desarrollo Web Avanzado", "Carlos Rodríguez", "", "1", "", "2", "", "14-16", "Y05"),
                ("111223344", "Estadística Aplicada", "Laura Pérez", "", "3", "", "2", "", "9-11", "Z10"),
                ("555666777", "Diseño de Interfaces", "Juan García", "", "4", "", "1", "", "13-15", "W18"),
                ("888999000", "Sistemas Operativos", "Roberto Martínez", "", "2", "", "4", "", "8-10", "V09"),
                ("218602962","Analisis de Algoritmos","Jorge Ernesto","","1","","1","","7-9","X14"),
               ("123456789", "Introducción a la Programación", "María González", "", "2", "", "3", "", "10-12", "X20"),
                ("987654321", "Desarrollo Web Avanzado", "Carlos Rodríguez", "", "1", "", "2", "", "14-16", "Y05"),
                ("111223344", "Estadística Aplicada", "Laura Pérez", "", "3", "", "2", "", "9-11", "Z10"),
                ("555666777", "Diseño de Interfaces", "Juan García", "", "4", "", "1", "", "13-15", "W18"),
                ("888999000", "Sistemas Operativos", "Roberto Martínez", "", "2", "", "4", "", "8-10", "V09"),
               ("218602962","Analisis de Algoritmos","Jorge Ernesto","","1","","1","","7-9","X14"),
               ("123456789", "Introducción a la Programación", "María González", "", "2", "", "3", "", "10-12", "X20"),
                ("987654321", "Desarrollo Web Avanzado", "Carlos Rodríguez", "", "1", "", "2", "", "14-16", "Y05"),
                ("111223344", "Estadística Aplicada", "Laura Pérez", "", "3", "", "2", "", "9-11", "Z10"),
                ("555666777", "Diseño de Interfaces", "Juan García", "", "4", "", "1", "", "13-15", "W18"),
                ("888999000", "Sistemas Operativos", "Roberto Martínez", "", "2", "", "4", "", "8-10", "V09"),
                ("218602962","Analisis de Algoritmos","Jorge Ernesto","","1","","1","","7-9","X14"),
               ("123456789", "Introducción a la Programación", "María González", "", "2", "", "3", "", "10-12", "X20"),
                ("987654321", "Desarrollo Web Avanzado", "Carlos Rodríguez", "", "1", "", "2", "", "14-16", "Y05"),
                ("111223344", "Estadística Aplicada", "Laura Pérez", "", "3", "", "2", "", "9-11", "Z10"),
                ("555666777", "Diseño de Interfaces", "Juan García", "", "4", "", "1", "", "13-15", "W18"),
                ("888999000", "Sistemas Operativos", "Roberto Martínez", "", "2", "", "4", "", "8-10", "V09"),
               ]
        treeview.delete(*treeview.get_children())
        
        for dato in datos:
            treeview.insert("","end", values=dato)

    def bloquerCierre(self):
        messagebox.showerror("Error de ventana", message="Por favor presione el boton de regresar...")

    def regresar_ventana_principal(self):
        self.nueva_ventana.destroy()
        self.root.deiconify()
        