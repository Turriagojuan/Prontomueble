from .conexion import Conexion

class CargoDAO:
    @classmethod
    def obtener_todos(cls):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cargo")
        cargos = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return cargos

    @classmethod
    def obtener_por_id(cls, id_cargo):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cargo WHERE id_cargo = %s", (id_cargo,))
        cargo = cursor.fetchone()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return cargo

    @classmethod
    def agregar(cls, cargo):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO cargo (cargo) VALUES (%s) RETURNING id_cargo", (cargo,))
        id_cargo = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return id_cargo

    @classmethod
    def actualizar(cls, id_cargo, cargo):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE cargo SET cargo = %s WHERE id_cargo = %s", (cargo, id_cargo))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id_cargo):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM cargo WHERE id_cargo = %s", (id_cargo,))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
