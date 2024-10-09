import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        # Inicializa la conexión como None (no conectada).
        self.connection = None

    def connect(self):
        """Establece una conexión con la base de datos."""
        try:
            # Intenta conectarse a la base de datos usando las credenciales proporcionadas.
            self.connection = mysql.connector.connect(
                host="localhost",
                user="your_username",  # Nombre de usuario de la db.
                password="your_password",  # Contraseña de usuario de la db.
                database="database_name"  # Nombre de la base de datos.
            )
            if self.connection.is_connected():
                # Si la conexión es exitosa, imprime un mensaje.
                print("Connection established successfully")
        except Error as e:
            # Si hay un error durante la conexión, se imprime el error.
            print(f"Error connecting to the database: {e}")
            return False
        return True

    def commit(self):
        """Confirma la transacción actual."""
        if self.connection:
            # Confirma la transacción si la conexión está activa.
            self.connection.commit()
            print("Transaction committed")

    def rollback(self):
        """Revierte la transacción actual."""
        if self.connection:
            # Revierte la transacción si ocurre un error o si es necesario.
            self.connection.rollback()
            print("Transaction rolled back")

    def close(self):
        """Cierra la conexión a la base de datos."""
        if self.connection.is_connected():
            # Cierra la conexión si aún está activa.
            self.connection.close()
            print("Connection closed")