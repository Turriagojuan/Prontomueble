from .conexion import Conexion

class ReporteDAO:
    @classmethod
    def vendedor_mas_ventas(cls, mes, anio):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT e.id_empleado, e.nombre, e.apellido, COUNT(v.id_venta) AS total_ventas
            FROM empleado e
            JOIN venta v ON e.id_empleado = v.id_empleado
            WHERE EXTRACT(MONTH FROM v.fecha) = %s AND EXTRACT(YEAR FROM v.fecha) = %s
            GROUP BY e.id_empleado, e.nombre, e.apellido
            ORDER BY total_ventas DESC
            LIMIT 5;
        """, (mes, anio))
        resultado = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return resultado

    @classmethod
    def clientes_nuevos(cls, mes, anio):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id_cliente, nombre, apellido, fecha_registro
            FROM cliente
            WHERE EXTRACT(MONTH FROM fecha_registro) = %s AND EXTRACT(YEAR FROM fecha_registro) = %s
            ORDER BY fecha_registro DESC;
        """, (mes, anio))
        resultado = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return resultado
    
    @classmethod
    def clientes_mayores_compras(cls, mes, anio):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT c.id_cliente, c.nombre, c.apellido, SUM(v.total_venta) AS total_gastado
            FROM cliente c
            JOIN venta v ON c.id_cliente = v.id_cliente
            WHERE EXTRACT(MONTH FROM v.fecha) = %s AND EXTRACT(YEAR FROM v.fecha) = %s
            GROUP BY c.id_cliente, c.nombre, c.apellido
            ORDER BY total_gastado DESC
            LIMIT 5;
        """, (mes, anio))
        resultado = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return resultado

    @classmethod
    def muebles_mas_vendidos(cls, mes, anio):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT m.id_mueble, m.nombre, SUM(i.cantidad) AS total_vendido
            FROM mueble m
            JOIN incluye i ON m.id_mueble = i.id_mueble
            JOIN venta v ON i.id_venta = v.id_venta
            WHERE EXTRACT(MONTH FROM v.fecha) = %s AND EXTRACT(YEAR FROM v.fecha) = %s
            GROUP BY m.id_mueble, m.nombre
            ORDER BY total_vendido DESC
            LIMIT 5;
        """, (mes, anio))
        resultado = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return resultado
