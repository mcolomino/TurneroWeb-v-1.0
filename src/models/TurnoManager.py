from .entities.Turno import TurnoVal
from datetime import datetime

class TurnoManager():
    
    @classmethod
    def get_by_id(cls, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT idturno, fecha, horaturno, idprofesional, idpaciente, actividad, estado, horallega, horaatiende FROM turnos WHERE idturno = %s"
            
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
            
            return TurnoVal(*row) if row else None

        except Exception as ex:
            raise Exception(ex)
    

    @classmethod

    #BUSCAR TODOS SEGUN FILTRO (PROFESIONAL, PACIENTE, FECHA)
    def BuscarTodos(self, db, filtro):
        try:
            cursor = db.connection.cursor()

            sql = """SELECT idturno, fecha, horaturno, idprofesional, idpaciente, actividad, estado, 
                    horallega, horaatiende, p.nombre AS nombre_pac, u.nombre AS nombre_prof 
                    FROM turnos t 
                    INNER JOIN pacientes p ON t.idpaciente = p.idpac 
                    INNER JOIN usuario u ON t.idprofesional = u.idusu"""

            conditions = []
            params = []

            if filtro.fechad is not None:
                conditions.append("t.fecha BETWEEN %s AND %s")
                params.extend([filtro.fechad, filtro.fechah])

            if filtro.idprofesional is not None and int(filtro.idprofesional) > 0:
                conditions.append("t.idprofesional = %s")
                params.append(filtro.idprofesional)

            if filtro.idpaciente is not None and int(filtro.idpaciente) > 0:
                conditions.append("t.idpaciente = %s")
                params.append(filtro.idpaciente)

            if conditions:
                sql += " WHERE " + " AND ".join(conditions)

            sql += " ORDER BY t.fecha, t.horaturno"

            cursor.execute(sql, params)
            datos = cursor.fetchall()

            return datos

        except Exception as ex:
            raise Exception(ex)
    

    @classmethod
    def AgregarTur(cls, db, turno):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO turnos (fecha, horaturno, idprofesional, idpaciente, actividad, estado, horallega, horaatiende) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            datos = (turno.fecha, turno.horaturno, turno.idprofesional, turno.idpaciente, turno.actividad, turno.estado, turno.horallega, turno.horaatiende)

            cursor.execute(sql, datos)
            db.connection.commit()

            return 'perfecto'

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def EditarTur(cls, db, turno):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE turnos SET fecha = %s, horaturno = %s, idprofesional = %s, idpaciente = %s, actividad = %s, estado = %s, horallega = %s, horaatiende = %s WHERE idturno = %s"
            datos = (turno.fecha, turno.horaturno, turno.idprofesional, turno.idpaciente, turno.actividad, turno.estado, turno.horallega, turno.horaatiende, turno.idturno)

            cursor.execute(sql, datos)
            db.connection.commit()

            return 'Actualizado'

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def actestado(cls, db, turno):
        try:
            cursor = db.connection.cursor()
            if turno.estado != "Atendido":
                sql = "UPDATE turnos SET estado = %s, horallega = %s, horaatiende = %s WHERE idturno = %s"
                datos = (turno.estado, turno.horallega, turno.horaatiende, turno.idturno)
            else:
                sql = "UPDATE turnos SET estado = %s, horaatiende = %s WHERE idturno = %s"
                datos = (turno.estado, turno.horaatiende, turno.idturno)

            cursor.execute(sql, datos)
            db.connection.commit()

            return 'Actualizado'

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def actausentes(cls, db, turno):
        try:
            cursor = db.connection.cursor()
            
            sql = "UPDATE turnos SET estado = 'Ausente'"

            conditions = []
            params = []

            conditions.append("estado = %s")
            params.append("En Agenda")

            if turno.fecha is not None:
                conditions.append("fecha < %s")
                params.extend([turno.fecha])

            if conditions:
                sql += " WHERE " + " AND ".join(conditions)

            cursor.execute(sql, params)
            db.connection.commit()

            return 'Actualizado'

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def BorrarTur(cls, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM turnos WHERE idturno = %s"
            
            cursor.execute(sql, (id,))
            db.connection.commit()

            return "Borrado"

        except Exception as ex:
            raise Exception(ex)