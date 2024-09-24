BEGIN;
-- crear un savepoint antes de realizar una tranferencia
SAVEPOINT tranfer_savepoint;

-- punto 3: debitar 300 pesos a anna 
UPDATE cuentas
set saldo = saldo -300
WHERE cuenta_id = 1

-- punto 4: abonar 300 pesos a carlos
UPDATE cuentas
set saldo = saldo + 300
WHERE cuenta_id = 2

-- punto 5: registrar las transacciones en la tabla transacciones
INSERT INTO transacciones(desde_cuenta_id,hacia_cuenta_id,monto)
VALUES(1,2,300)

ROLLBACK TO tranfer_savepoint

COMMIT;