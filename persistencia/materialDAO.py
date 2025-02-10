from .conexion import Conexion

class MaterialDAO:
    @classmethod
    def obtener_todos(cls):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM material")
        materiales = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return materiales

    @classmethod
    def obtener_por_id(cls, id_material):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM material WHERE id_material = %s", (id_material,))
        material = cursor.fetchone()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return material

    @classmethod
    def agregar(cls, nombre_mat):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO material (nombre_mat) VALUES (%s)", (nombre_mat,))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, id_material, nombre_mat):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE material SET nombre_mat = %s WHERE id_material = %s", (nombre_mat, id_material))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id_material):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM material WHERE id_material = %s", (id_material,))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
