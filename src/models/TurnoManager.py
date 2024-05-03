from .entities.Turno import TurnoVal

class TurnoManager():
    
    
    @classmethod
    def get_by_id(self,db, id):
        try:
            
            cursor=db.connection.cursor()
            sql="SELECT idturno, DATE_FORMAT(fecha, '%d/%m/%Y') AS fecha, horaturno, idprofesional, idpaciente, actividad, estado, horallega, horaatiende FROM turnos WHERE idturno = '{}'" .format(id) 
            
            cursor.execute(sql)
            row=cursor.fetchone()
            
            if row != None:
                TurVal=TurnoVal(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                return TurVal
            
            else:
                return None

        except Exception as ex:
            raise Exception (ex)
    

    @classmethod

    #BUSCAR TODOS SEGUN FILTRO (PROFESIONAL, PACIENTE, FECHA)
    def BuscarTodos(self,db, filtro):
        try:
            #DATE_FORMAT(fecha, '%d/%m/%Y') AS fecha
            cursor=db.connection.cursor()
            
            # Iniciar la cadena SQL 
            sql="""SELECT idturno, fecha, horaturno, idprofesional, idpaciente, actividad, estado, 
                horallega, horaatiende, p.nombre AS nombre_pac, u.nombre AS nombre_prof 
                FROM turnos t INNER JOIN pacientes p ON t.idpaciente = p.idpac INNER JOIN usuario u ON t.idprofesional = u.idusu"""
            
            #armar WHERE segun filtro
            # Iniciar la cadena WHERE con la condición FECHA DESDE-HASTA
            if filtro.fechad is not None:
                sql += " WHERE t.fecha BETWEEN '{}' AND '{}'".format(filtro.fechad, filtro.fechah)

            # Si idprof no es None, agregar la condición de idprof
            if filtro.idprofesional is not None and int(filtro.idprofesional) > 0:
                sql += " AND t.idprofesional = '{}'" .format(filtro.idprofesional)

            # Si idpaciente no es None, agregar la condición de idpaciente
            if filtro.idpaciente is not None and int(filtro.idpaciente) > 0:
                sql += " AND t.idpaciente = '{}'" .format(filtro.idpaciente)

            # order del sql
            sql += " ORDER BY t.fecha, t.horaturno"
            
            cursor.execute(sql)
            datos=cursor.fetchall()
            
            if datos != None:
                return datos
            
            else:
                return None

        except Exception as ex:
            raise Exception (ex)
    

    @classmethod
    def AgregarTur(self,db, turno):
        try:
            
            cursor=db.connection.cursor()
            sql="INSERT INTO turnos (fecha, horaturno, idprofesional, idpaciente, actividad, estado, horallega, horaatiende)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s)" 
            datos=(turno.fecha, turno.horaturno, turno.idprofesional, turno.idpaciente, turno.actividad, turno.estado, turno.horallega, turno.horaatiende)

            cursor.execute(sql, datos)
            db.connection.commit()

            return 'perfecto'

        except Exception as ex:
            raise Exception (ex)
   

    @classmethod
    def EditarTur(self,db, turno):
        try:
            
            cursor=db.connection.cursor()
            sql="UPDATE turnos SET fecha=%s, horaturno=%s, idprofesional=%s, idpaciente=%s, actividad=%s, estado=%s, horallega=%s, horaatiende=%s WHERE idturno =%s"

            datos=(turno.fecha, turno.horaturno, turno.idprofesional, turno.idpaciente, turno.actividad, turno.estado, turno.horallega, turno.horaatiende, turno.idturno)
            cursor.execute(sql,datos)
            db.connection.commit() 
            
            return 'Actualizado'
            
            
        except Exception as ex:
            raise Exception (ex)
    
    #ACTUALIZAR ESTADOS TURNO
    
    @classmethod
    def actestado(self,db, turno):
        try:
            
            cursor=db.connection.cursor()
            if turno.estado != "Atendido":
                sql="UPDATE turnos SET estado=%s, horallega=%s, horaatiende=%s WHERE idturno =%s"
                datos=(turno.estado, turno.horallega, turno.horaatiende, turno.idturno)
            else:
                sql="UPDATE turnos SET estado=%s, horaatiende=%s WHERE idturno =%s"
                datos=(turno.estado, turno.horaatiende, turno.idturno)

            cursor.execute(sql,datos)
            db.connection.commit() 
            
            return 'Actualizado'
        
        except Exception as ex:
            raise Exception (ex)

    #----------------
    
    @classmethod
    def BorrarTur(self,db, id):
        try:
            
            cursor=db.connection.cursor()
            sql="DELETE FROM turnos WHERE idturno = '{}'" .format(id) 
            
            cursor.execute(sql)
            db.connection.commit()

            return "Borrado"
            

        except Exception as ex:
            raise Exception (ex)