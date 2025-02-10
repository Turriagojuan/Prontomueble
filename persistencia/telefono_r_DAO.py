from .conexion import Conexion

class TelefonoRepresentanteDAO:
    @classmethod
    def obtener_por_representante(cls, id_representante):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM telefono_r WHERE id_representante = %s", (id_representante,))
        telefonos = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return telefonos

    @classmethod
    def agregar(cls, id_telefono, id_representante):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO telefono_r (id_telefono, id_representante) VALUES (%s, %s)", 
                       (id_telefono, id_representante))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id_telefono, id_representante):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM telefono_r WHERE id_telefono = %s AND id_representante = %s", (id_telefono, id_representante))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
