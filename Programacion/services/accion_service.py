# import mysql.connector
# from datetime import date

# def vender_accion(id_portafolio, id_accion, cantidad):
#     conexion = mysql.connector.connect(
#         host="localhost",
#         user="usuario",
#         password="contraseña",
#         database="Base_datos"
#     )

#     cursor = conexion.cursor()

#     # Obtiene el precio de venta actual de la acción
#     cursor.execute("SELECT precio_venta FROM accion WHERE id_accion = %s", (id_accion,))
#     precio_venta = cursor.fetchone()[0]

#     # Calcula el total de la transacción y la comisión (ejemplo del 1%)
#     total_venta = precio_venta * cantidad
#     comision = total_venta * 0.01

#     # Registra la operación en la tabla 'operacion'
#     sql_operacion = """INSERT INTO operacion (id_portafolio, id_accion, id_tipo, fecha_operacion, precio, cantidad, total_accion, comision) 
#                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
#     valores_operacion = (id_portafolio, id_accion, 2, date.today(), precio_venta, cantidad, total_venta, comision)
#     cursor.execute(sql_operacion, valores_operacion)

#     # Actualiza la cantidad de acciones en la tabla 'portafolioaccion'
#     sql_actualizar = "UPDATE portafolioaccion SET cantidad = cantidad - %s WHERE id_portafolio = %s AND id_accion = %s"
#     cursor.execute(sql_actualizar, (cantidad, id_portafolio, id_accion))

#     # Confirma los cambios
#     conexion.commit()

#     # Cierra la conexión
#     cursor.close()
#     conexion.close()

#     print("Venta realizada con éxito. Total vendido:", total_venta, "Comisión:", comision)

# # Ejemplo de uso
# vender_accion(1, 101, 10)  # Vende 10 acciones con id 101 del portafolio con id 1

from Programacion.dao.accion_dao import AccionDAO

class AccionService:
    def __init__(self, db_conexion):
        self.accion_dao = AccionDAO(db_conexion)


    def armar_listado_acciones(self):
        lista_acciones = self.accion_dao.listar_acciones()
        for accion in lista_acciones:
            print(f"ID: {accion[0]} / Simbolo: {accion[1]} / Empresa: {accion[2]} / Precio de compra: {accion[4]}")
