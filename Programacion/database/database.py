# Conexión a base de datos
import mysql.connector

class ConexionBaseDeDatos:
    def __init__(self):
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host='bi201yksz8ubhfjv7dyb-mysql.services.clever-cloud.com',
                user='uihujxs4xmhkdvi3',
                password='tp5pvzvCEPOye6QVmYAQ',
                database='bi201yksz8ubhfjv7dyb',
                port='3306'
            )
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")

    def desconectar(self):
        if self.conexion:
            self.conexion.close()
