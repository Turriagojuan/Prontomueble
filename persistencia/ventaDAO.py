from datetime import date
from .conexion import Conexion

class VentaDAO:
    @classmethod
    def obtener_todos(cls):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM venta")
        ventas = cursor.fetchall()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return ventas

    @classmethod
    def obtener_por_id(cls, id_venta):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM venta WHERE id_venta = %s", (id_venta,))
        venta = cursor.fetchone()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return venta

    @classmethod
    def agregar(cls, fecha, total_venta, id_empleado, id_cliente, estado, id_medio):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO venta (fecha, total_venta, id_empleado, id_cliente, estado, id_medio) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_venta", 
                       (fecha, total_venta, id_empleado, id_cliente, estado, id_medio))
        id_venta = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return id_venta

    @classmethod
    def actualizar(cls, id_venta, fecha, total_venta, id_empleado, id_cliente, estado, id_medio):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE venta SET fecha = %s, total_venta = %s, id_empleado = %s, id_cliente = %s, estado = %s, id_medio = %s WHERE id_venta = %s", 
                       (fecha, total_venta, id_empleado, id_cliente, estado, id_medio, id_venta))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, id_venta):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM venta WHERE id_venta = %s", (id_venta,))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
    @classmethod
    def registrar_venta(cls, id_empleado, id_cliente, total_venta, id_medio):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO venta (fecha, total_venta, id_empleado, id_cliente, estado, id_medio)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_venta
        """, (date.today(), total_venta, id_empleado, id_cliente, 'Completado', id_medio))
        id_venta = cursor.fetchone()[0]
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return id_venta

    @classmethod
    def registrar_detalle_venta(cls, id_venta, id_mueble, cantidad, subtotal):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO incluye (id_mueble, id_venta, cantidad, subtotal)
            VALUES (%s, %s, %s, %s)
        """, (id_mueble, id_venta, cantidad, subtotal))
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)

    @staticmethod
    def crear_venta(id_cliente, id_empleado, id_medio):
        """
        Crea una nueva venta en la base de datos y retorna el ID de la venta creada.
        """
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        
        query = """
            INSERT INTO venta (fecha, total_venta, id_empleado, id_cliente, estado, id_medio)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id_venta;
        """
        cursor.execute(query, (date.today(), 0, id_empleado, id_cliente, 'Pendiente', id_medio))
        id_venta = cursor.fetchone()[0]
        
        conexion.commit()
        cursor.close()
        Conexion.liberar_conexion(conexion)
        
        return id_venta
    @staticmethod
    def insertar_detalle_venta(id_venta, id_mueble, cantidad):
            """
            Inserta un detalle de venta en la tabla `incluye`.
            """
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            
            # Obtener el precio del mueble
            query_precio = "SELECT precioU FROM suministra WHERE id_mueble = %s LIMIT 1;"
            cursor.execute(query_precio, (id_mueble,))
            precio = cursor.fetchone()[0]
            
            cantidad = int(cantidad)
            precio = float(precio)
        
            total = precio * cantidad
            
             # Actualizar el total de la venta
            query_update_total = """
                UPDATE venta SET total_venta = total_venta + %s WHERE id_venta = %s;
            """
            cursor.execute(query_update_total, (total, id_venta))


            query = """
                INSERT INTO incluye (id_mueble, id_venta, cantidad)
                VALUES (%s, %s, %s);
            """
            cursor.execute(query, (id_mueble, id_venta, cantidad))
            
           
            
            conexion.commit()
            cursor.close()
            Conexion.liberar_conexion(conexion)

    @staticmethod
    def obtener_detalles_venta(id_venta):
        """
        Obtiene los detalles de una venta específica, incluyendo los muebles vendidos,
        sus cantidades y subtotales.
        """
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        
        query = """
SELECT 
    v.id_venta,
    v.fecha,
    v.total_venta AS total,
    m.medio_de_pago AS metodo_pago,
    i.cantidad,
    mu.nombre AS nombre_mueble,
    s.precioU AS precio_unitario,
    (i.cantidad * s.precioU) AS subtotal
FROM venta v
JOIN medio m ON v.id_medio = m.id_medio
JOIN incluye i ON v.id_venta = i.id_venta
JOIN mueble mu ON i.id_mueble = mu.id_mueble
JOIN suministra s ON mu.id_mueble = s.id_mueble
WHERE v.id_venta = %s;


        """
        
        cursor.execute(query, (id_venta,))
        detalles = cursor.fetchall()
        
        cursor.close()
        Conexion.liberar_conexion(conexion)
        return detalles

