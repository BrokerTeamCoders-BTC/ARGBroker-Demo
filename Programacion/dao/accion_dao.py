from models.accion import Accion


class AccionDAO:
    def __init__(self, db_conexion):
        self.db = db_conexion


    def obtener_accion(self, id_accion):
        try:
            with self.db.conexion.cursor() as cursor:
                sql = "SELECT * FROM Accion WHERE id_accion = %s"
                cursor.execute(sql, (id_accion,))
                accion = cursor.fetchone()
            if accion:
                return Accion(*accion)
            return None
        except Exception as e:
            print(f"Error al obtener la acción: {e}")
            return None
