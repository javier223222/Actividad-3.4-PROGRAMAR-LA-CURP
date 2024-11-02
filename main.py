from tkinter import *
from tkinter import messagebox as MessageBox
from curpgenerate.curp import CurpGenerator
import re

class CurpApplication:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Calculadora CURP")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f4f8")

        # Título
        title_label = Label(root, text="Generador de CURP", font=("Arial", 16, "bold"), bg="#f0f4f8", fg="#333")
        title_label.pack(pady=10)

        # Estados y géneros
        self.states = ["AS", "BC", "BS", "CC", "CL", "CM", "CS", "CH", "DF", "DG", "GT", "GR", "HG",
                       "JC", "MC", "MN", "MS", "NT", "NL", "OC", "PL", "QT", "QR", "SP", "SL", "SR",
                       "TC", "TS", "TL", "VZ", "YN", "ZS"]
        self.gener = ["H", "M"]

        # Nombre
        self.create_label_entry("Nombre:", "entradanombre")
        self.create_label_entry("Apellido Paterno:", "entradapellidop")
        self.create_label_entry("Apellido Materno:", "entradapellidom")
        self.create_label_entry("Fecha de Nacimiento (dd-mm-yyyy):", "entradanacimineto")

        # Género
        self.clickedgnero = StringVar()
        self.clickedgnero.set("H")
        self.create_dropdown("Género:", self.clickedgnero, self.gener)

        # Estado de nacimiento
        self.clicked = StringVar()
        self.clicked.set("AS")
        self.create_dropdown("Estado de Nacimiento:", self.clicked, self.states)

        # Botón Calcular CURP
        self.button_ejecutar = Button(root, text="Calcular CURP", command=self.calculate,
                                      bg="#007bff", fg="white", font=("Arial", 12, "bold"), width=20)
        self.button_ejecutar.pack(pady=15)

        # Etiqueta de Resultado
        self.etiqueta_resultado = Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f4f8", fg="#007bff")
        self.etiqueta_resultado.pack(pady=10)

    def create_label_entry(self, label_text, entry_name):
        label = Label(self.root, text=label_text, font=("Arial", 10), bg="#f0f4f8", fg="#333")
        label.pack(pady=5)
        entry = Entry(self.root, width=30, font=("Arial", 12))
        entry.pack()
        setattr(self, entry_name, entry)

    def create_dropdown(self, label_text, variable, options):
        label = Label(self.root, text=label_text, font=("Arial", 10), bg="#f0f4f8", fg="#333")
        label.pack(pady=5)
        dropdown = OptionMenu(self.root, variable, *options)
        dropdown.config(width=25, font=("Arial", 10))
        dropdown.pack()

    def calculate(self):
        try:
            x=re.search("^0[1-9]|[10-31]-0[1-9]|[10-12]-\d\d\d\d$",self.entradanacimineto.get())
            print(x)
            if x is None:
                MessageBox.showerror("Error", "Por favor, ingrese un formato de fecha correcta")

            curp = CurpGenerator(
                self.entradanombre.get(),
                self.entradapellidop.get(),
                self.entradapellidom.get(),
                self.entradanacimineto.get(),
                self.clickedgnero.get(),
                self.clicked.get()
            )
            result = curp.calculateCurp()
           
            self.etiqueta_resultado.config(text=f"CURP: {result}")
        except:
            MessageBox.showerror("Error", "Por favor, completa todos los campos correctamente")

        



      
  
       

        





if __name__== "__main__":
    root=Tk()
    app=CurpApplication(root)
    root.mainloop()
        