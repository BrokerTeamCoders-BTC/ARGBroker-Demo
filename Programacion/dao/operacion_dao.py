class OperacionDAO:
    def __init__(self, db_conexion):
        self.db = db_conexion

    def registrar_operacion(self, id_portafolio, id_tipo, id_accion, fecha_operacion, precio, cantidad, total_accion, comision):
        try:
            with self.db.conexion.cursor() as cursor: 
                sql = """INSERT INTO Operacion (id_portafolio, id_tipo, id_accion, fecha_operacion, precio, cantidad, total_accion, comision)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                values = (id_portafolio, id_tipo, id_accion, fecha_operacion, precio, cantidad, total_accion, comision)
                cursor.execute(sql, values)
                self.db.conexion.commit()  
        except Exception as e:
            print(f"Error al registrar operación: {e}")
        self.db.conexion.rollback()

    def obtener_operaciones_accion(self, id_portafolio, id_accion, fecha_desde):
        try:
            with self.db.conexion.cursor(dictionary=True) as cursor: 
                sql = """
                SELECT *
                FROM Operacion
                WHERE id_portafolio = %s AND id_accion = %s AND fecha_operacion >= %s
                ORDER BY fecha_operacion
                """
                cursor.execute(sql, (id_portafolio, id_accion, fecha_desde))
                operaciones = cursor.fetchall()
            return [
                {**op, 'tipo': 'compra' if op['id_tipo'] == 1 else 'venta'}
                for op in operaciones
            ]   
        except Exception as e:
            print(f"Error al obtener las operaciones hechas en una acción: {e}")
            return None
        