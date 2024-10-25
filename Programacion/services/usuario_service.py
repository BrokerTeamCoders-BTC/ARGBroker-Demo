from Programacion.dao.inversor_dao import InversorDAO
from Programacion.models.inversor import Inversor
from Programacion.dao.portafolio_dao import PortafolioDAO
from Programacion.models.portafolio import Portafolio
		
class UsuarioService:
    def __init__(self, db_conexion):
        self.inversor_dao = InversorDAO(db_conexion)
        self.portafolio_dao = PortafolioDAO(db_conexion)
        self.usuario = None

    def registrar_inversor(self, nombre, apellido, cuil, correo, contrasenia):
        nuevo_inversor = Inversor(None, nombre, apellido, cuil, correo, contrasenia)
        id_inversor = self.inversor_dao.crear_inversor(nuevo_inversor)
    # Creación del portafolio para el nuevo inversor.
        nuevo_portafolio = Portafolio(id_portafolio=None, id_inversor=id_inversor, saldo=1000000.0, total_invertido=0, rendimiento=0)
        self.portafolio_dao.crear_portafolio(nuevo_portafolio)
        self.usuario = Inversor.get_datos_cuenta()

    def iniciar_sesion(self, correo, contrasenia):
            inversor = self.inversor_dao.obtener_inversor_por_correo_y_contrasenia(correo, contrasenia)
            self.usuario = inversor
            return inversor
    
    def obtener_datos_cuenta(self):
            return self.usuario
