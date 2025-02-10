class Proveedor:
    def __init__(self, id_proveedor, nombre, direccion, telefono):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Proveedor: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"
