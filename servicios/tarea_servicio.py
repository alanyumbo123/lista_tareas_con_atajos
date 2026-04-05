from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        if descripcion.strip() != "":
            tarea = Tarea(descripcion)
            self.tareas.append(tarea)

    def obtener_tareas(self):
        return self.tareas

    def completar_tarea(self, index):
        if 0 <= index < len(self.tareas):
            self.tareas[index].completada = True

    def eliminar_tarea(self, index):
        if 0 <= index < len(self.tareas):
            self.tareas.pop(index)
