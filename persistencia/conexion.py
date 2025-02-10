import psycopg2
from psycopg2 import pool

class Conexion:
    _DATABASE = "prontomueble"
    _USER = "postgres"
    _PASSWORD = "1234"
    _HOST = "localhost"
    _PORT = "5432"
    _pool = None

    @classmethod
    def iniciar_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(1, 10,
                    database=cls._DATABASE,
                    user=cls._USER,
                    password=cls._PASSWORD,
                    host=cls._HOST,
                    port=cls._PORT
                )
                print("Pool de conexiones creado exitosamente.")
            except Exception as e:
                print(f"Error al crear el pool de conexiones: {e}")

    @classmethod
    def obtener_conexion(cls):
        if cls._pool is None:
            cls.iniciar_pool()
        return cls._pool.getconn()

    @classmethod
    def liberar_conexion(cls, conexion):
        cls._pool.putconn(conexion)

    @classmethod
    def cerrar_pool(cls):
        if cls._pool:
            cls._pool.closeall()
            print("Pool de conexiones cerrado.")

    @classmethod
    def conectar(cls):
        if cls._pool is None:
            cls.iniciar_pool()
        return cls.obtener_conexion()

# Prueba de conexión
if __name__ == "__main__":
    Conexion.iniciar_pool()
    conexion = Conexion.obtener_conexion()
    if conexion:
        print("Conexión a la base de datos exitosa.")
        Conexion.liberar_conexion(conexion)
    Conexion.cerrar_pool()