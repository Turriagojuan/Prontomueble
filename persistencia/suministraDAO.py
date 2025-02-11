from .conexion import Conexion

class SuministraDAO:
    @classmethod
    def agregar(cls, id_proveedor, id_mueble,cantidad , preciou ):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO suministra (id_proveedor, id_mueble, cantidad, preciou) VALUES (%s, %s, %s, %s)", 
                       (id_proveedor, id_mueble, cantidad, preciou ))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def obtener_todos(cls):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id_proveedor, id_mueble, preciou, cantidad FROM suministra")
        suministros = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return suministros

    @classmethod
    def obtener_por_id(cls, id_proveedor, id_mueble):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id_proveedor, id_mueble, preciou, cantidad FROM suministra WHERE id_proveedor = %s AND id_mueble = %s", 
                       (id_proveedor, id_mueble))
        suministro = cursor.fetchone()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return suministro

    @classmethod
    def actualizar(cls, id_proveedor, id_mueble, nuevo_id_proveedor, nuevo_id_mueble, nuevo_preciou, nueva_cantidad):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE suministra SET id_proveedor = %s, id_mueble = %s, preciou = %s, cantidad = %s WHERE id_proveedor = %s AND id_mueble = %s", 
                       (nuevo_id_proveedor, nuevo_id_mueble, nuevo_preciou, nueva_cantidad, id_proveedor, id_mueble))
        conexion.commit()
        cursor.close()
    @classmethod
    def eliminar(cls, id_proveedor, id_mueble):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM suministra WHERE id_proveedor = %s AND id_mueble = %s", (id_proveedor, id_mueble))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)