from .conexion import Conexion

class TelefonoEmpleadoDAO:
    @classmethod
    def obtener_por_empleado(cls, id_empleado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM telefono_e WHERE id_empleado = %s", (id_empleado,))
        telefonos = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return telefonos

    @classmethod
    def agregar(cls, id_telefono, id_empleado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO telefono_e (id_telefono, id_empleado) VALUES (%s, %s)", 
                       (id_telefono, id_empleado))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id_telefono, id_empleado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM telefono_e WHERE id_telefono = %s AND id_empleado = %s", (id_telefono, id_empleado))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
