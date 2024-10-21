# Clase Portafolio

class Portafolio:
    def __init__(self, id_portafolio, id_inversor, saldo, total_invertido, rendimiento):
        self.__id_portafolio = id_portafolio
        self.__id_inversor = id_inversor
        self.__saldo = saldo
        self.__total_invertido = total_invertido
        self.__rendimiento = rendimiento


    def get_id_portafolio(self):
        return self.__id_portafolio
   
    def get_id_inversor(self):
        return self.__id_inversor
   
    def get_saldo(self):
        return self.__saldo
   
    def get_total_invertido(self):
        return self.__total_invertido
   
    def get_rendimiento(self):
        return self.__rendimiento
