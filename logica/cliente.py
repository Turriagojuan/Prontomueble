class Cliente:
    def __init__(self, id_cliente, nombre, apellido, correo, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono

    # Getters
    def get_id_cliente(self):
        return self.id_cliente

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_correo(self):
        return self.correo

    def get_telefono(self):
        return self.telefono

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_correo(self, correo):
        self.correo = correo

    def set_telefono(self, telefono):
        self.telefono = telefono

    # Métodos adicionales
    def actualizar_info(self, nombre, apellido, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono

    def obtener_info(self):
        return {
            "id_cliente": self.id_cliente,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo": self.correo,
            "telefono": self.telefono
        }
