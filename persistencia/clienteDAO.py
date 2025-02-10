from .conexion import Conexion

class ClienteDAO:
    @classmethod
    def obtener_todos(cls):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cliente")
        clientes = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return clientes

    @classmethod
    def obtener_por_id(cls, id_cliente):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cliente WHERE id_cliente = %s", (id_cliente,))
        cliente = cursor.fetchone()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return cliente

    @classmethod
    def agregar(cls, nombre, apellido, direccion, correo, fecha_registro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO cliente (nombre, apellido, direccion, correo, fecha_registro) VALUES (%s, %s, %s, %s, %s) RETURNING id_cliente", 
                       (nombre, apellido, direccion, correo, fecha_registro))
        id_cliente = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return id_cliente

    @classmethod
    def actualizar(cls, id_cliente, nombre, apellido, direccion, correo, fecha_registro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE cliente SET nombre = %s, apellido = %s, direccion = %s, correo = %s, fecha_registro = %s WHERE id_cliente = %s", 
                       (nombre, apellido, direccion, correo, fecha_registro, id_cliente))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id_cliente):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id_cliente,))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
