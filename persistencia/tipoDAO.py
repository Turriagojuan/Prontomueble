from persistencia.conexion import Conexion
from logica.tipo import Tipo

class TipoDAO:
    def __init__(self):
        self.conexion = Conexion()

    def crear_tipo(self, tipo: Tipo):
        sql = """
        INSERT INTO tipo (nombre)
        VALUES (%s)
        """
        parametros = (tipo.nombre,)
        return self.conexion.ejecutar_actualizacion(sql, parametros)

    def obtener_tipo(self, id_tipo):
        sql = "SELECT * FROM tipo WHERE id_tipo = %s"
        resultado = self.conexion.ejecutar_consulta(sql, (id_tipo,))
        if resultado:
            return Tipo(*resultado[0])
        return None

    def obtener_todos(self):
        sql = "SELECT * FROM tipo"
        resultados = self.conexion.ejecutar_consulta(sql)
        return [Tipo(*fila) for fila in resultados]

    def actualizar_tipo(self, tipo: Tipo):
        sql = """
        UPDATE tipo SET nombre = %s WHERE id_tipo = %s
        """
        parametros = (tipo.nombre, tipo.id_tipo)
        return self.conexion.ejecutar_actualizacion(sql, parametros)

    def eliminar_tipo(self, id_tipo):
        sql = "DELETE FROM tipo WHERE id_tipo = %s"
        return self.conexion.ejecutar_actualizacion(sql, (id_tipo,))
