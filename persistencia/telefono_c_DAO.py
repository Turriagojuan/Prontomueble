from .conexion import Conexion

class TelefonoClienteDAO:
    @classmethod
    def obtener_por_cliente(cls, id_cliente):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM telefono_c WHERE id_cliente = %s", (id_cliente,))
        telefonos = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return telefonos

    @classmethod
    def agregar(cls, id_telefono, id_cliente):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO telefono_c (id_telefono, id_cliente) VALUES (%s, %s)", 
                       (id_telefono, id_cliente))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id_telefono, id_cliente):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM telefono_c WHERE id_telefono = %s AND id_cliente = %s", (id_telefono, id_cliente))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)