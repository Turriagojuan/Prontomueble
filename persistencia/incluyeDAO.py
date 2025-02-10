from .conexion import Conexion

class IncluyeDAO:
    @classmethod
    def obtener_todos(cls):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM incluye")
        incluye = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return incluye

    @classmethod
    def obtener_por_id(cls, id_mueble, id_venta):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM incluye WHERE id_mueble = %s AND id_venta = %s", (id_mueble, id_venta))
        incluye = cursor.fetchone()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return incluye

    @classmethod
    def agregar(cls, id_mueble, id_venta, cantidad, subtotal):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO incluye (id_mueble, id_venta, cantidad, subtotal) VALUES (%s, %s, %s, %s)", (id_mueble, id_venta, cantidad, subtotal))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, id_mueble, id_venta, cantidad, subtotal):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE incluye SET cantidad = %s, subtotal = %s WHERE id_mueble = %s AND id_venta = %s", (cantidad, subtotal, id_mueble, id_venta))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id_mueble, id_venta):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM incluye WHERE id_mueble = %s AND id_venta = %s", (id_mueble, id_venta))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
