# Lógica relacionada al portafolio.
from Programacion.dao.portafolio_dao import PortafolioDAO
from Programacion.dao.accion_dao import AccionDAO


class PortafolioService:
    def __init__(self, db_conexion):
        self.portafolio_dao = PortafolioDAO(db_conexion)
        self.accion_dao = AccionDAO(db_conexion)


    def listar_activos(self, id_inversor):
        portafolio = self.portafolio_dao.obtener_portafolio(id_inversor)
        activos = self.portafolio_dao.obtener_activos_portafolio(portafolio.get_id_portafolio())
        resultados = []


        for activo in activos:

            cantidad = activo['cantidad']
            precio_compra = activo['precio_compra']
            precio_actual = activo['precio_venta']  # Asumimos que el precio de venta es el precio actual
            valor_total = cantidad * precio_actual
            costo_total = cantidad * precio_compra
            rendimiento = round(((valor_total - costo_total) / costo_total) * 100 if costo_total else 0.0, 2)


            resultados.append({
                'id_accion': activo['id_accion'],
                'nombre_empresa': activo['nombre_empresa'],
                'simbolo': activo['simbolo'],
                'cantidad': cantidad,
                'precio_compra': precio_compra,
                'precio_actual': precio_actual,
                'valor_total': valor_total,
                'rendimiento': rendimiento
            })
        return resultados
