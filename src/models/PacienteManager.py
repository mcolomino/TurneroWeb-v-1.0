from .entities.Paciente import PacienteVal

class PacienteManager():
    
    @classmethod
    def get_by_id(cls, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT idpac, nombre, dni, telefono, mail FROM pacientes WHERE idpac = %s"
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
            
            return PacienteVal(*row) if row else None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def BuscarTodos(cls, db, pac):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT idpac, nombre, dni, telefono, mail FROM pacientes"
            
            conditions = []
            params = []

            if pac.idpac is not None and int(pac.idpac) > 0:
                conditions.append("idpac = %s")
                params.append(pac.idpac)

            if conditions:
                sql += " WHERE " + " AND ".join(conditions)

            sql += " ORDER BY nombre"
            
            cursor.execute(sql, params)
            datos = cursor.fetchall()
            
            return datos if datos else None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def AgregarPac(cls, db, paciente):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO pacientes (nombre, dni, telefono, mail) VALUES (%s, %s, %s, %s)"
            datos = (paciente.nombre, paciente.dni, paciente.telefono, paciente.mail)
                   
            cursor.execute(sql, datos)
            db.connection.commit()

            return 'perfecto'

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def EditarPac(cls, db, paciente):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE pacientes SET nombre = %s, dni = %s, telefono = %s, mail = %s WHERE idpac = %s"
            datos = (paciente.nombre, paciente.dni, paciente.telefono, paciente.mail, paciente.idpac)
            
            cursor.execute(sql, datos)
            db.connection.commit() 
            
            return 'Actualizado'

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def BorrarPac(cls, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM pacientes WHERE idpac = %s"
            cursor.execute(sql, (id,))
            db.connection.commit()

            return "Borrado"

        except Exception as ex:
            raise Exception(ex)