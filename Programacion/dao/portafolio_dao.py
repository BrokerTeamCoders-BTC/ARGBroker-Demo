from models.portafolio import Portafolio

class PortafolioDAO:
    def __init__(self, db_conexion):
        self.db = db_conexion


    def crear_portafolio(self, portafolio):
        try:
            with self.db.conexion.cursor() as cursor:
                sql = """INSERT INTO Portafolio (id_inversor, saldo, total_invertido, rendimiento)
                            VALUES (%s, %s, %s, %s)"""
                values = (portafolio.get_id_inversor(), portafolio.get_saldo(), portafolio.get_total_invertido(), portafolio.get_rendimiento())
                cursor.execute(sql, values)
                self.db.conexion.commit()
        except Exception as e:
            print(f"Error al crear portafolio: {e}")
            self.db.conexion.rollback()

    def obtener_portafolio(self, id_inversor):
        try:
            with self.db.conexion.cursor() as cursor:
                sql = "SELECT * FROM Portafolio WHERE id_inversor = %s"
                cursor.execute(sql, (id_inversor,))
                portafolio = cursor.fetchone()
            if portafolio:
                return Portafolio(*portafolio)
            return None
        except Exception as e:
            print(f"Error al obtener portafolio: {e}")
            return None

        def obtener_activos_portafolio(self, id_portafolio):
        try:
            with self.db.conexion.cursor(dictionary=True) as cursor:
                sql = """
                        SELECT a.id_accion, a.simbolo, a.nombre_empresa, pa.cantidad, a.precio_venta, a.precio_compra
                        FROM PortafolioAccion pa
                        JOIN Accion a ON pa.id_accion = a.id_accion
                        WHERE pa.id_portafolio = %s;
                        """
                cursor.execute(sql, (id_portafolio,))
                activos = cursor.fetchall()
            return activos
        except Exception as e:
            print(f"Error al obtener los activos en portafolio: {e}")
            return None
