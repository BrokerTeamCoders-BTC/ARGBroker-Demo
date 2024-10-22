from dao.operacion_dao import OperacionDAO
from dao.portafolio_dao import PortafolioDAO
from dao.accion_dao import AccionDAO
from datetime import date


class OperacionService:
    def __init__(self, db_conexion):
        self.operacion_dao = OperacionDAO(db_conexion)
        self.portafolio_dao = PortafolioDAO(db_conexion)
        self.accion_dao = AccionDAO(db_conexion)


    def realizar_compra(self, id_inversor, id_accion, cantidad):
        portafolio = self.portafolio_dao.obtener_portafolio(id_inversor)
        accion = self.accion_dao.obtener_accion(id_accion)
       
        operacion = self._crear_operacion_compra(portafolio, accion, cantidad)
       
        self._validar_saldo_suficiente(portafolio, operacion)

    def _crear_operacion_compra(self, portafolio, accion, cantidad):
        costo_total = accion.get_precio_compra() * cantidad
        comision = costo_total * 0.015
        return {
            "id_portafolio": portafolio.get_id_portafolio(),
            "id_tipo": 1,
            "id_accion": accion.get_id_accion(),
            "fecha_operacion": date.today(),
            "precio": accion.get_precio_compra(),
            "cantidad": cantidad,
            "total_accion": costo_total,
            "comision": comision
        }

    def _validar_saldo_suficiente(self, portafolio, operacion):
        costo_total_con_comision = operacion["total_accion"] + operacion["comision"]
        if portafolio.get_saldo() < costo_total_con_comision:
            raise ValueError("Saldo insuficiente para realizar la compra")


    

