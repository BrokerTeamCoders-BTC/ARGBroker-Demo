class Inversor:
    def __init__(self, id_inversor, nombre, apellido, cuil, correo, contrasenia):
        self.__id_inversor = id_inversor
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cuil = cuil
        self.__correo = correo
        self.__contrasenia = contrasenia 

    def __str__(self):
        return f"Inversor(ID: {self.__id_inversor}, Nombre: {self.__nombre}, Apellido: {self.__apellido}, CUIL: {self.__cuil}, Correo: {self.__correo})"
    
    def get_id_inversor(self):
        return self.__id_inversor
   
    def get_nombre(self):
        return self.__nombre
   
    def get_apellido(self):
        return self.__apellido
   
    def get_cuil(self):
        return self.__cuil
   
    def get_correo(self):
        return self.__correo
   
    def get_contrasenia(self):
        return self.__contrasenia
    
    
    def get_datos_cuenta(self):
        inversor = {
            "id_inversor": self.__id_inversor,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "cuil": self.__cuil,
            "correo": self.__correo,
        }