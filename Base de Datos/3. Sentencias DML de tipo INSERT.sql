-- Conjunto de Sentencias DML tipo INSERT para insertar datos iniciales a la base de datos

INSERT INTO Inversor (nombre, apellido, cuil, correo, contrasenia) VALUES 
('Santiago', 'Lopez', '20412345678', 'santiago.lopez@mail.com', 'passSanti2024'),
('Camila', 'Fernandez', '27234567891', 'camila.fernandez@mail.com', 'camilaf_1234'),
('Diego', 'Martinez', '20387654321', 'diego.martinez@mail.com', 'martinezDiego2023');

INSERT INTO Portafolio (id_inversor, saldo, total_invertido, rendimiento) VALUES 
(1, 1100000.0, 600000.0, 0.07),
(2, 1250000.0, 400000.0, 0.03),
(3, 950000.0, 200000.0, 0.04);

INSERT INTO Accion (simbolo, nombre_empresa, precio_venta, precio_compra) VALUES 
('AAPL', 'Apple Inc.', 190.0, 185.0),
('MSFT', 'Microsoft Corp.', 260.0, 250.5),
('GOOGL', 'Alphabet Inc.', 2850.0, 2800.0);

INSERT INTO Operacion (id_portafolio, id_accion, id_tipo, fecha_operacion, precio, cantidad, total_accion, comision) VALUES 
(1, 1, 1, '2024-08-10', 185.0, 50, 9250.0, 22.5), -- compra
(1, 2, 0, '2024-09-15', 260.0, 15, 3900.0, 12.5), -- venta
(2, 1, 1, '2024-07-05', 185.0, 40, 7400.0, 18.0), -- compra
(3, 3, 1, '2024-08-21', 2800.0, 6, 16800.0, 35.0); -- compra

INSERT INTO PortafolioAccion (id_portafolio, id_accion, cantidad) VALUES 
(1, 1, 50),
(1, 2, 15),
(2, 1, 40),
(3, 3, 6);

