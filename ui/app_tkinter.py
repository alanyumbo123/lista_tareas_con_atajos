import tkinter as tk
from servicios.tarea_servicio import TareaServicio

class AppTkinter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lista de Tareas")
        self.geometry("400x400")

        self.servicio = TareaServicio()

        # Entrada
        self.entry = tk.Entry(self)
        self.entry.pack(pady=10)

        # Botones
        tk.Button(self, text="Añadir", command=self.agregar).pack()
        tk.Button(self, text="Completar", command=self.completar).pack()
        tk.Button(self, text="Eliminar", command=self.eliminar).pack()

        # Lista
        self.lista = tk.Listbox(self)
        self.lista.pack(fill="both", expand=True, pady=10)

        # EVENTOS DE TECLADO 🔥
        self.entry.bind("<Return>", lambda e: self.agregar())
        self.bind("c", lambda e: self.completar())
        self.bind("<Delete>", lambda e: self.eliminar())
        self.bind("<Escape>", lambda e: self.destroy())

    def agregar(self):
        texto = self.entry.get()
        self.servicio.agregar_tarea(texto)
        self.entry.delete(0, tk.END)
        self.actualizar_lista()

    def completar(self):
        seleccion = self.lista.curselection()
        if seleccion:
            self.servicio.completar_tarea(seleccion[0])
            self.actualizar_lista()

    def eliminar(self):
        seleccion = self.lista.curselection()
        if seleccion:
            self.servicio.eliminar_tarea(seleccion[0])
            self.actualizar_lista()

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for tarea in self.servicio.obtener_tareas():
            texto = tarea.descripcion
            if tarea.completada:
                texto += " ✔"
            self.lista.insert(tk.END, texto)
