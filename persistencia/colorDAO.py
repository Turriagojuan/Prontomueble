from .conexion import Conexion

class ColorDAO:
    @classmethod
    def obtener_todos(cls):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM color")
        colores = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return colores

    @classmethod
    def obtener_por_id(cls, id_color):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM color WHERE id_color = %s", (id_color,))
        color = cursor.fetchone()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return color

    @classmethod
    def agregar(cls, nombre_color):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO color (nombre_color) VALUES (%s) RETURNING id_color", (nombre_color,))
        id_color = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return id_color

    @classmethod
    def actualizar(cls, id_color, nombre_color):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE color SET nombre_color = %s WHERE id_color = %s", (nombre_color, id_color))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id_color):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM color WHERE id_color = %s", (id_color,))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)