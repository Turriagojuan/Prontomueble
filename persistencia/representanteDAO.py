from .conexion import Conexion

class RepresentanteDAO:
    @classmethod
    def obtener_todos(cls):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM representante")
        representantes = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return representantes

    @classmethod
    def obtener_por_id(cls, id_representante):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM representante WHERE id_representante = %s", (id_representante,))
        representante = cursor.fetchone()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return representante

    @classmethod
    def agregar(cls, nombre, apellido, correo, id_proveedor):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO representante (nombre, apellido, correo, id_proveedor) VALUES (%s, %s, %s, %s)", 
                       (nombre, apellido, correo, id_proveedor))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, id_representante, nombre, apellido, correo, id_proveedor):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE representante SET nombre = %s, apellido = %s, correo = %s, id_proveedor = %s WHERE id_representante = %s", 
                       (nombre, apellido, correo, id_proveedor, id_representante))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id_representante):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM representante WHERE id_representante = %s", (id_representante,))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
