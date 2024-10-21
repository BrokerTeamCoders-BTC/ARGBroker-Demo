from models.inversor import Inversor


class InversorDAO:
    def __init__(self, db_conexion):
        self.db = db_conexion


    def crear_inversor(self, inversor):
        try:
            with self.db.connection.cursor() as cursor:
                sql = """INSERT INTO Inversor (nombre, apellido, cuil, correo, contrasenia)
                        VALUES (%s, %s, %s, %s, %s)"""
                values = (inversor.get_nombre(), inversor.get_apellido(), inversor.get_cuil(), inversor.get_correo(), inversor.get_contrasenia())
                cursor.execute(sql, values)
                id_inversor = cursor.lastrowid #Devuelve el último valor autoincremental generado (id_inversor)
                self.db.connection.commit()
            return id_inversor
        except Exception as e:
            print(f"Error al crear el inversor: {e}")
            self.db.connection.rollback()
            return None
