from .conexion import Conexion

class VentaDAO:
    @classmethod
    def obtener_todos(cls):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM venta")
        ventas = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return ventas

    @classmethod
    def obtener_por_id(cls, id_venta):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM venta WHERE id_venta = %s", (id_venta,))
        venta = cursor.fetchone()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return venta

    @classmethod
    def agregar(cls, fecha, total_venta, id_empleado, id_cliente, estado, id_medio):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO venta (fecha, total_venta, id_empleado, id_cliente, estado, id_medio) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_venta", 
                       (fecha, total_venta, id_empleado, id_cliente, estado, id_medio))
        id_venta = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return id_venta

    @classmethod
    def actualizar(cls, id_venta, fecha, total_venta, id_empleado, id_cliente, estado, id_medio):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE venta SET fecha = %s, total_venta = %s, id_empleado = %s, id_cliente = %s, estado = %s, id_medio = %s WHERE id_venta = %s", 
                       (fecha, total_venta, id_empleado, id_cliente, estado, id_medio, id_venta))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id_venta):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM venta WHERE id_venta = %s", (id_venta,))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
