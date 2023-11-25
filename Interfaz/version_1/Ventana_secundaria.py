import tkinter as tk
from tkinter import ttk

class Ventana_Secundaria:
    def __init__(self,ventana):
        self.root=ventana
        self.root.withdraw()
        self.nueva_ventana=tk.Toplevel(self.root)
        self.nueva_ventana.title("Propuesta de horario")
        self.nueva_ventana.config(bg="red")
        #self.nueva_ventana.geometry("500x230")
        
        self.frame_mostrar_horario=tk.Frame(self.nueva_ventana,padx=50,pady=50)
        self.frame_mostrar_horario.grid(padx=20,pady=20,row=0,column=0,columnspan=2)
        self.etiqueta=tk.Label(self.frame_mostrar_horario,text="Horario propuesto").pack()

        self.tabla=ttk.Treeview(self.frame_mostrar_horario,columns=("Clave","NombreMateria","Profesor","L","M","I","J","V","Hora","Aula"), show="headings")
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

        self.barraVertical=ttk.Scrollbar(self.frame_mostrar_horario,orient="vertical",command=self.tabla.yview)
        self.barraVertical.pack(side="right",fill="y")
        self.tabla.configure(yscrollcommand=self.barraVertical.set)
        
        self.barraHorizontal=ttk.Scrollbar(self.frame_mostrar_horario,orient="horizontal",command=self.tabla.xview)
        self.barraHorizontal.pack(side="bottom",fill="x")
        self.tabla.configure(yscrollcommand=self.barraHorizontal.set)

        self.cargar_datos_a_mostrar(self.tabla)
        self.tabla.pack()
        
        self.boton_exportar_horario=tk.Button(
            self.nueva_ventana,
            text="Exportar horario",
            font=("Calibri",10),
        ).grid(row=1,column=0,padx=10,pady=10)
        self.boton_regresar=tk.Button(
            self.nueva_ventana,
            text="Regresar",
            font=("Calibri",10),
            command=self.regresar_ventana_principal
        ).grid(row=1,column=1,padx=10,pady=10)
    def cargar_datos_a_mostrar(self,treeview):
        datos=[("218602962","Analisis de Algoritmos","Jorge Ernesto","","1","","1","","7-9","X14")]
        
        treeview.delete(*treeview.get_children())

        for dato in datos:
            treeview.insert("","end", values=dato)

    def regresar_ventana_principal(self):
        self.nueva_ventana.destroy()
        self.root.deiconify()
        