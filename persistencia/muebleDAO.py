from .conexion import Conexion

class MuebleDAO:
    @classmethod
    def obtener_todos(cls):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
        SELECT 
            m.id_mueble, 
            m.nombre, 
            m.alto, 
            m.largo, 
            m.ancho, 
            ma.nombre_mat AS material, 
            c.nombre_color AS color, 
            t.nombre AS tipo,
            s.preciou
        FROM 
            mueble m
        JOIN 
            material ma ON m.id_material = ma.id_material
        JOIN 
            color c ON m.id_color = c.id_color
        JOIN 
            tipo t ON m.id_tipo = t.id_tipo
        JOIN 
            suministra s ON m.id_mueble = s.id_mueble
        GROUP BY 
            m.id_mueble, ma.nombre_mat, c.nombre_color, t.nombre, s.preciou
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
        cursor.execute("INSERT INTO mueble (nombre, alto, largo, ancho, id_material, id_color, id_tipo) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id_mueble", 
                       (nombre, alto, largo, ancho, id_material, id_color, id_tipo))
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
