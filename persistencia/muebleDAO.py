from .conexion import Conexion

class MuebleDAO:
    @classmethod
    def obtener_todos(cls):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
        SELECT *
        FROM vista_catalogo_muebles
                        """)
        muebles = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return muebles

    @classmethod
    def obtener_por_id(cls, id_mueble):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM mueble WHERE id_mueble = %s", (id_mueble,))
        mueble = cursor.fetchone()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return mueble

    @classmethod
    def agregar(cls, nombre, alto, largo, ancho, id_material, id_color, id_tipo):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
                INSERT INTO mueble (nombre, alto, largo, ancho, id_material, id_color, id_tipo) 
                VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id_mueble
        """, (nombre, alto, largo, ancho, id_material, id_color, id_tipo))
        id_mueble = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return id_mueble

    @classmethod
    def actualizar(cls, id_mueble, nombre, alto, largo, ancho, id_material, id_color, id_tipo):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE mueble SET nombre = %s, alto = %s, largo = %s, ancho = %s, id_material = %s, id_color = %s, id_tipo = %s WHERE id_mueble = %s", 
                       (nombre, alto, largo, ancho, id_material, id_color, id_tipo, id_mueble))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id_mueble):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM mueble WHERE id_mueble = %s", (id_mueble,))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion) 
    @classmethod
    def obtener_ultimo_id(cls):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT LAST_INSERT_ID()")
        ultimo_id = cursor.fetchone()[0]
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return ultimo_id
