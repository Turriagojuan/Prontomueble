class Material:
    def __init__(self, id_material, nombre):
        self._id_material = id_material
        self._nombre = nombre

    # Getters
    def get_id_material(self):
        return self._id_material
    
    def get_nombre(self):
        return self._nombre

    # Setters
    def set_id_material(self, id_material):
        self._id_material = id_material
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    # Métodos adicionales
    def obtener_info(self):
        return f"Material ID: {self._id_material}, Nombre: {self._nombre}"