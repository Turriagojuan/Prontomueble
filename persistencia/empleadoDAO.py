from .conexion import Conexion

class EmpleadoDAO:
    @classmethod
    def obtener_todos(cls):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM empleado")
        empleados = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return empleados

    @classmethod
    def obtener_por_id(cls, id_empleado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM empleado WHERE id_empleado = %s", (id_empleado,))
        empleado = cursor.fetchone()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return empleado

    @classmethod
    def agregar(cls,id ,nombre, apellido, correo, id_cargo):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO empleado (id_empleado,nombre, apellido, correo, id_cargo) VALUES (%s, %s, %s, %s, %s) RETURNING id_empleado", 
                       (id, nombre, apellido, correo, id_cargo))
        id_empleado = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return id_empleado

    @classmethod
    def actualizar(cls, id_empleado, nombre, apellido, correo, id_cargo):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE empleado SET nombre = %s, apellido = %s, correo = %s, id_cargo = %s WHERE id_empleado = %s", 
                       (nombre, apellido, correo, id_cargo, id_empleado))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id_empleado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM empleado WHERE id_empleado = %s", (id_empleado,))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def autenticar(cls, id_empleado):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id_cargo FROM empleado WHERE id_empleado = %s", (id_empleado,))
        empleado = cursor.fetchone()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return empleado

    @classmethod
    def obtener_todos_con_cargo(cls):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT * FROM vista_empleados
        """)
        empleados = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return empleados

