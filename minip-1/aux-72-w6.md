## TABLA PARA CAMBIOS TRIGGER

``` sql
CREATE TABLE cliente_cambios (
  idcliente NUMBER NOT NULL,
  nombre VARCHAR2(75),
  apellido VARCHAR2(75),
  fnacimiento DATE,
  sexo VARCHAR2(15) CONSTRAINT CK_cliente_cambios_sexo CHECK (sexo IN ('MASCULINO', 'FEMENINO')),
  movimiento VARCHAR2(50),
  ingreso_anterior NUMBER,
  ingreso_nuevo NUMBER,
  nombrepais VARCHAR2(75),
  fecha_cambio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT FK_cliente_cambios_idcliente FOREIGN KEY (idcliente) REFERENCES cliente (idcliente)
);

```
## TRIGGER 
``` sql
CREATE OR REPLACE TRIGGER trig_cliente_actualizar
BEFORE UPDATE OR INSERT 
ON cliente
FOR EACH ROW
DECLARE
  nombre_pais VARCHAR2(75); 
BEGIN
  IF :OLD.ingreso != :NEW.ingreso THEN
    SELECT p.nombre INTO nombre_pais
    FROM pais p
    WHERE p.idpais = :OLD.idpais;

    INSERT INTO cliente_cambios (idcliente, nombre, apellido, fnacimiento, sexo, movimiento, ingreso_anterior, ingreso_nuevo, nombrePais)
    VALUES (:OLD.idcliente, :OLD.nombre, :OLD.apellido, :OLD.fnacimiento, :OLD.sexo,'Ingreso cambiado', :OLD.ingreso , :NEW.ingreso, nombre_pais);
  END IF;
END;
```