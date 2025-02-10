from .conexion import Conexion

class MedioDAO:
    @classmethod
    def obtener_todos(cls):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM medio")
        medios = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return medios

    @classmethod
    def obtener_por_id(cls, id_medio):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM medio WHERE id_medio = %s", (id_medio,))
        medio = cursor.fetchone()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return medio

    @classmethod
    def agregar(cls, medio_de_pago):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO medio (medio_de_pago) VALUES (%s) RETURNING id_medio", (medio_de_pago,))
        id_medio = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return id_medio

    @classmethod
    def actualizar(cls, id_medio, medio_de_pago):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE medio SET medio_de_pago = %s WHERE id_medio = %s", (medio_de_pago, id_medio))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id_medio):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM medio WHERE id_medio = %s", (id_medio,))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
