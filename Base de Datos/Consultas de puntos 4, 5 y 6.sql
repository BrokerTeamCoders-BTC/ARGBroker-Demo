-- 4) Consultas de tipo UPDATE para actualizar datos de los datos ya insertados 

-- 1. Actualiza el saldo de un portafolio después de una inversión.
UPDATE Portafolio
SET saldo = saldo - 10000.0, total_invertido = total_invertido + 10000.0
WHERE id_portafolio = 1;

-- 2. Modifica el precio de venta de una acción.
UPDATE Accion
SET precio_venta = 195.0
WHERE simbolo = 'AAPL';

-- 3. Actualiza el correo y contraseña de un inversor.
UPDATE Inversor
SET correo = 'santi.lopez.new@mail.com', contrasenia = 'nuevaPass2024'
WHERE id_inversor = 1;

-- 4. Modifica la cantidad de acciones en un portafolio específico.
UPDATE PortafolioAccion
SET cantidad = cantidad + 10
WHERE id_portafolio = 1 AND id_accion = 1;

-- 5. Actualiza el rendimiento de un portafolio.
UPDATE Portafolio
SET rendimiento = rendimiento + 0.02
WHERE id_portafolio = 2;

-- 6. Actualiza el precio de venta de una acción.
UPDATE Accion
SET precio_venta = 195.0
WHERE simbolo = 'AAPL';

-- 7. Reduce el precio de compra de una acción.
UPDATE Accion
SET precio_compra = 245.0
WHERE simbolo = 'MSFT';

-- 8. Cambia el nombre de la empresa asociada a una acción despues de una supuesta fusión.
UPDATE Accion
SET nombre_empresa = 'Alphabet Inc. - Nueva División'
WHERE simbolo = 'GOOGL';

-- 9. Incrementa el precio de venta y compra de una acción.
UPDATE Accion
SET precio_venta = precio_venta * 1.05, precio_compra = precio_compra * 1.05
WHERE simbolo = 'AAPL';

-- 10. Cambia el símbolo de una acción que hizo un rebranding.
UPDATE Accion
SET simbolo = 'META'
WHERE nombre_empresa = 'Facebook Inc.';

-- Falta agregar las consultas de los puntos 5 y 6