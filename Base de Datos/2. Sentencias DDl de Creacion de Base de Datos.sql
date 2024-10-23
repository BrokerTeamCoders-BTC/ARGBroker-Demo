create database argbroker;
use argbroker;

CREATE TABLE Inversor (
    id_inversor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    cuil VARCHAR(13) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    contrasenia VARCHAR(50) NOT NULL
);

CREATE TABLE Portafolio (
    id_portafolio INT AUTO_INCREMENT PRIMARY KEY,
    id_inversor INT NOT NULL,
    saldo FLOAT DEFAULT 1000000.0,
    total_invertido FLOAT,
    rendimiento FLOAT,
    FOREIGN KEY (id_inversor) REFERENCES Inversor(id_inversor)
);

CREATE TABLE Accion (
    id_accion INT AUTO_INCREMENT PRIMARY KEY,
    simbolo VARCHAR(10) NOT NULL,
    nombre_empresa VARCHAR(100) NOT NULL,
    precio_venta FLOAT,
    precio_compra FLOAT
);

CREATE TABLE Operacion (
    id_operacion INT AUTO_INCREMENT PRIMARY KEY,
    id_portafolio INT NOT NULL,
    id_accion INT NOT NULL,
	id_tipo BOOLEAN,
    fecha_operacion DATE NOT NULL,
    precio FLOAT,
    cantidad INT,
    total_accion FLOAT,
    comision FLOAT,
    FOREIGN KEY (id_portafolio) REFERENCES Portafolio(id_portafolio),
    FOREIGN KEY (id_accion) REFERENCES Accion(id_accion)
);

CREATE TABLE PortafolioAccion (
    id_portafolio INT NOT NULL,
    id_accion INT NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (id_portafolio) REFERENCES Portafolio(id_portafolio),
    FOREIGN KEY (id_accion) REFERENCES Accion(id_accion)
);