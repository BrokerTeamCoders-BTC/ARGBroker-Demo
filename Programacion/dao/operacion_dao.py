class OperacionDAO:
    def __init__(self, db_conexion):
        self.db = db_conexion

    def registrar_operacion(self, id_portafolio, id_tipo, id_accion, fecha_operacion, precio, cantidad, total_accion, comision):
        try:
            with self.db.connection.cursor() as cursor:
                sql = """INSERT INTO Operacion (id_portafolio, id_tipo, id_accion, fecha_operacion, precio, cantidad, total_accion, comision)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                values = (id_portafolio, id_tipo, id_accion, fecha_operacion, precio, cantidad, total_accion, comision)
                cursor.execute(sql, values)
                self.db.connection.commit()
        except Exception as e:
            print(f"Error al registrar operación: {e}")
            self.db.connection.rollback()