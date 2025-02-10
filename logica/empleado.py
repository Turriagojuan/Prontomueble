class Empleado:
    def __init__(self, id_empleado, nombre, apellido, correo, cargo):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.cargo = cargo
    
    # Getters
    def get_id_empleado(self):
        return self.id_empleado
    
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_correo(self):
        return self.correo
    
    def get_cargo(self):
        return self.cargo
    
    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_apellido(self, apellido):
        self.apellido = apellido
    
    def set_correo(self, correo):
        self.correo = correo
    
    def set_cargo(self, cargo):
        self.cargo = cargo
    
    # Métodos
    def actualizar_info(self, nombre, apellido, correo, cargo):
        """Actualiza la información del empleado."""
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.cargo = cargo
    
    def obtener_info(self):
        """Devuelve un diccionario con la información del empleado."""
        return {
            "id_empleado": self.id_empleado,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo": self.correo,
            "cargo": self.cargo
        }
