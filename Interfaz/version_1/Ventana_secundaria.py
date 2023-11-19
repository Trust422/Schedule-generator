import tkinter as tk
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
        self.etiqueta=tk.Label(self.frame_mostrar_horario,text="Aqui va ir el horario propuesto").pack()

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
    def regresar_ventana_principal(self):
        self.nueva_ventana.destroy()
        self.root.deiconify()
        