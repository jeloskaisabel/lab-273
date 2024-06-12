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

CREATE OR REPLACE TRIGGER Tr_historico_docente
AFTER UPDATE or DELETE ON DOCENTE
FOR EACH ROW
DECLARE
BEGIN
  -- AREA PARA LA EJECUCIÓN DE SENTENCIA RELACIONADAS A LA
  -- TABLA A MODIFICAR.
  Sentencias PLSQL y/o Update, Delete o Insert
END;


CREATE OR REPLACE TRIGGER trig_estudiante_actualizar
BEFORE UPDATE OR DELETE
ON estudiante e
FOR EACH ROW
DECLARE
  promedio NUMBER; 
BEGIN
  IF :OLD.promedio != :NEW.promedio THEN
    SELECT p.nombre INTO nombre_pais
    FROM pais p
    WHERE p.idpais = :OLD.idpais;

    INSERT INTO cliente_cambios (idcliente, nombre, apellido, fnacimiento, sexo, movimiento, ingreso_anterior, ingreso_nuevo, nombrePais)
    VALUES (:OLD.idcliente, :OLD.nombre, :OLD.apellido, :OLD.fnacimiento, :OLD.sexo,'Ingreso cambiado', :OLD.ingreso , :NEW.ingreso, nombre_pais);
  END IF;
END;



ALTER TABLE ESTUDIANTE
ADD promedio DECIMAL(5,2);

UPDATE ESTUDIANTE
SET promedio = 0;



CREATE TRIGGER actualizar_promedio_estudiante
AFTER UPDATE ON INSCRITO
FOR EACH ROW
BEGIN
  DECLARE promedio_temp DECIMAL(5,2);
  SET promedio_temp = (NEW.nota1 + NEW.nota2 + IFNULL(NEW.nota3, 0)) / (IF(NEW.nota3 IS NULL, 2, 3));
  UPDATE ESTUDIANTE
  SET promedio = promedio_temp
  WHERE idestu = NEW.idestu;
END;







