from .conexion import Conexion

class ProveedorDAO:
    @classmethod
    def obtener_todos(cls):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM proveedor")
        proveedores = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return proveedores

    @classmethod
    def obtener_por_id(cls, id_proveedor):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM proveedor WHERE id_proveedor = %s", (id_proveedor,))
        proveedor = cursor.fetchone()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return proveedor

    @classmethod
    def agregar(cls, nombre, direccion, telefono):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO proveedor (nombre, direccion, telefono) VALUES (%s, %s, %s) RETURNING id_proveedor", 
                       (nombre, direccion, telefono))
        id_proveedor = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return id_proveedor

    @classmethod
    def actualizar(cls, id_proveedor, nombre, direccion, telefono):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE proveedor SET nombre = %s, direccion = %s, telefono = %s WHERE id_proveedor = %s", 
                       (nombre, direccion, telefono, id_proveedor))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id_proveedor):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM proveedor WHERE id_proveedor = %s", (id_proveedor,))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
