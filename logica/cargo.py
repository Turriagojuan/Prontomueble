class Cargo:
    def __init__(self, id_cargo, nombre, descripcion):
        self.id_cargo = id_cargo
        self.nombre = nombre
        self.descripcion = descripcion
    
    # Getters
    def get_id_cargo(self):
        return self.id_cargo
    
    def get_nombre(self):
        return self.nombre
    
    def get_descripcion(self):
        return self.descripcion
    
    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_descripcion(self, descripcion):
        self.descripcion = descripcion
    
    # Métodos adicionales
    def actualizar_cargo(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
    
    def obtener_info(self):
        return {
            "id_cargo": self.id_cargo,
            "nombre": self.nombre,
            "descripcion": self.descripcion
        }