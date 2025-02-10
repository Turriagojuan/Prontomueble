class Color:
    def __init__(self, id_color, nombre):
        self._id_color = id_color
        self._nombre = nombre

    # Getters
    def get_id_color(self):
        return self._id_color

    def get_nombre(self):
        return self._nombre

    # Setters
    def set_id_color(self, id_color):
        self._id_color = id_color

    def set_nombre(self, nombre):
        self._nombre = nombre

    # Métodos adicionales
    def actualizar_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def obtener_info(self):
        return f"ID: {self._id_color}, Nombre: {self._nombre}"