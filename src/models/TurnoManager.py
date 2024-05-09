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
                    horallega, horaatiende, p.nombre AS nompac, u.nombre AS nomprof 
                    FROM turnos t 
                    INNER JOIN pacientes p ON t.idpaciente = p.idpac 
                    INNER JOIN usuario u ON t.idprofesional = u.idusu"""

            conditions = []
            params = []

            # No incluir los turnos cancelados
            conditions.append("estado <> 'Cancelado'")
    
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

             # Lista para almacenar las instancias de TurnoVal
            lista_tur = []

            # Itera sobre los resultados de la consulta SQL
            for res in datos:
                # Crea una instancia de TurnoVal para cada registro
                TurV = TurnoVal(
                    idturno=res[0],
                    fecha=res[1],
                    horaturno=res[2],
                    idprofesional=res[3],
                    idpaciente=res[4],
                    actividad=res[5],
                    estado=res[6],
                    horallega=res[7],
                    horaatiende=res[8],
                    nompac=res[9],
                    nomprof=res[10]              
                )
                # Agrega la instancia a la lista de turnos
                lista_tur.append(TurV)

            # Ahora `lista_tur` contiene instancias de TurnoVal que representan los registros de la consulta SQL
            
            return lista_tur if lista_tur else None

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