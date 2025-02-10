class Incluye:
    def __init__(self, id_mueble, id_material, cantidad, subtotal):
        self._id_mueble = id_mueble
        self._id_material = id_material
        self._cantidad = cantidad
        self._subtotal = subtotal

    # Getters
    def get_id_mueble(self):
        return self._id_mueble
    
    def get_id_material(self):
        return self._id_material
    
    def get_cantidad(self):
        return self._cantidad
    
    def get_subtotal(self):
        return self._subtotal

    # Setters
    def set_id_mueble(self, id_mueble):
        self._id_mueble = id_mueble
    
    def set_id_material(self, id_material):
        self._id_material = id_material
    
    def set_cantidad(self, cantidad):
        self._cantidad = cantidad
    
    def set_subtotal(self, subtotal):
        self._subtotal = subtotal
    
    # Métodos adicionales
    def actualizar_cantidad(self, nueva_cantidad):
        self._cantidad = nueva_cantidad
    
    def calcular_subtotal(self, precio_material):
        self._subtotal = self._cantidad * precio_material
    
    def obtener_info(self):
        return f"Mueble ID: {self._id_mueble}, Material ID: {self._id_material}, Cantidad: {self._cantidad}, Subtotal: {self._subtotal}"
