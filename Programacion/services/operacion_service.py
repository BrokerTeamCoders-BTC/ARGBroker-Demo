from Programacion.dao.operacion_dao import OperacionDAO
from Programacion.dao.portafolio_dao import PortafolioDAO
from Programacion.dao.accion_dao import AccionDAO
from datetime import date


class OperacionService:
    def __init__(self, db_conexion):
        self.operacion_dao = OperacionDAO(db_conexion)
        self.portafolio_dao = PortafolioDAO(db_conexion)
        self.accion_dao = AccionDAO(db_conexion)


    def realizar_compra(self, id_inversor, id_accion, cantidad):
        # Obtener el portafolio y la acción
        portafolio = self.portafolio_dao.obtener_portafolio(id_inversor)
        accion = self.accion_dao.obtener_accion(id_accion)

        # Crear la operación de compra
        operacion = self._crear_operacion_compra(portafolio, accion, cantidad)

        # Validar que hay saldo suficiente
        self._validar_saldo_suficiente(portafolio, operacion)

        # Registrar la operación en la base de datos
        self.operacion_dao.registrar_operacion(
            id_portafolio=operacion["id_portafolio"],
            id_tipo=operacion["id_tipo"],
            id_accion=operacion["id_accion"],
            fecha_operacion=operacion["fecha_operacion"],
            precio=operacion["precio"],
            cantidad=operacion["cantidad"],
            total_accion=operacion["total_accion"],
            comision=operacion["comision"]
        )
        cantidad_acciones_anterior= self.portafolio_dao.obtener_cantidad_acciones(operacion["id_portafolio"], operacion["id_accion"])
        if cantidad_acciones_anterior:
            nueva_cantidad = cantidad_acciones_anterior + cantidad
            self.portafolio_dao.actualizar_portafolio_accion(operacion["id_portafolio"], operacion["id_accion"], nueva_cantidad)
        else:
            self.portafolio_dao.insertar_portafolio_accion(operacion["id_portafolio"], operacion["id_accion"], cantidad)
            
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


    def realizar_venta(self, id_inversor, id_accion, cantidad):
        portafolio = self.portafolio_dao.obtener_portafolio(id_inversor)
        accion = self.accion_dao.obtener_accion(id_accion)
        
        self._validar_acciones_suficientes(portafolio, id_accion, cantidad)
        
        operacion = self._crear_operacion_venta(portafolio, accion, cantidad)
        self._ejecutar_operacion(operacion, portafolio, -cantidad)


    def _crear_operacion_venta(self, portafolio, accion, cantidad):
        valor_venta = accion.get_precio_venta() * cantidad
        comision = valor_venta * 0.015
        return {
            "id_portafolio": portafolio.get_id_portafolio(),
            "id_tipo": 2,
            "id_accion": accion.get_id_accion(),
            "fecha_operacion": date.today(),
            "precio": accion.get_precio_venta(),
            "cantidad": cantidad,
            "total_accion": valor_venta,
            "comision": comision
        }

    def _validar_acciones_suficientes(self, portafolio, id_accion, cantidad):
        acciones_en_portafolio = self.portafolio_dao.obtener_cantidad_acciones(portafolio.get_id_portafolio(), id_accion)
        if acciones_en_portafolio < cantidad:
            raise ValueError("No tienes suficientes acciones para realizar esta venta")


    def _ejecutar_operacion(self, operacion, portafolio, cambio_cantidad):
        self._registrar_operacion(operacion)
        self._actualizar_portafolio(operacion, portafolio)
        self._actualizar_cantidad_acciones(portafolio.get_id_portafolio(), operacion["id_accion"], cambio_cantidad)


    def _registrar_operacion(self, operacion):
        self.operacion_dao.registrar_operacion(**operacion)


    def _actualizar_portafolio(self, operacion, portafolio):
        if operacion["id_tipo"] == 1:  # Compra
            nuevo_saldo = portafolio.get_saldo() - (operacion["total_accion"] + operacion["comision"])
            nuevo_total_invertido = portafolio.get_total_invertido() + operacion["total_accion"]
        else:  # Venta
            nuevo_saldo = portafolio.get_saldo() + (operacion["total_accion"] - operacion["comision"])
            costo_promedio = self._calcular_costo_promedio(portafolio.get_id_portafolio(), operacion["id_accion"])
            nuevo_total_invertido = portafolio.get_total_invertido() - (costo_promedio * operacion["cantidad"])

        portafolio.set_saldo(nuevo_saldo)
        portafolio.set_total_invertido(nuevo_total_invertido)
        # self.portafolio_dao.actualizar_portafolio(portafolio)


    def _actualizar_cantidad_acciones(self, id_portafolio, id_accion, cantidad):
        cantidad_actual = self.portafolio_dao.obtener_cantidad_acciones(id_portafolio, id_accion)
        nueva_cantidad = cantidad_actual + cantidad
        portafolio_accion = self.portafolio_dao.obtener_portafolio_accion(id_portafolio, id_accion)

        if portafolio_accion:
            self.portafolio_dao.actualizar_portafolio_accion(id_portafolio, id_accion, nueva_cantidad)
        else:
            self.portafolio_dao.insertar_portafolio_accion(id_portafolio, id_accion, cantidad)


    def _calcular_costo_promedio(self, id_portafolio, id_accion):
        operaciones = self.operacion_dao.obtener_operaciones_accion(id_portafolio, id_accion)
        total_costo = sum(op['precio'] * op['cantidad'] for op in operaciones if op['id_tipo'] == 1)
        total_cantidad = sum(op['cantidad'] for op in operaciones if op['id_tipo'] == 1)
        return total_costo / total_cantidad if total_cantidad > 0 else 0
    