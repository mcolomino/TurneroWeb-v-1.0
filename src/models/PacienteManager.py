from .entities.Paciente import PacienteVal

class PacienteManager():
    
    
    @classmethod
    def get_by_id(self,db, id):
        try:
            
            cursor=db.connection.cursor()
            sql="SELECT idpac, nombre, dni, telefono, mail FROM pacientes WHERE idpac = '{}'" .format(id) 
            
            cursor.execute(sql)
            row=cursor.fetchone()
            
            if row != None:
                PacVal=PacienteVal(row[0],row[1],row[2],row[3],row[4])
                return PacVal
            
            else:
                return None

        except Exception as ex:
            raise Exception (ex)
    

    @classmethod
    def BuscarTodos(self,db, pac):
        try:
            
            cursor=db.connection.cursor()
            
            
            sql="SELECT idpac, nombre, dni, telefono, mail FROM pacientes"

            if pac.idpac is not None and int(pac.idpac) > 0:
                sql += " WHERE idpac = '{}'" .format(pac.idpac)
            
             # order del sql
            sql += " ORDER BY nombre"

            cursor.execute(sql)
            datos=cursor.fetchall()
            
            if datos != None:
                return datos
            
            else:
                return None

        except Exception as ex:
            raise Exception (ex)
    

    @classmethod
    def AgregarPac(self,db, paciente):
        try:
            
            cursor=db.connection.cursor()
            sql="INSERT INTO pacientes (nombre, dni, telefono, mail)  VALUES (%s,%s,%s,%s)" 
            datos=(paciente.nombre, paciente.dni, paciente.telefono, paciente.mail)

            cursor.execute(sql, datos)
            db.connection.commit()

            return 'perfecto'

        except Exception as ex:
            raise Exception (ex)
   

    @classmethod
    def EditarPac(self,db, paciente):
        try:
            
            cursor=db.connection.cursor()
            sql="UPDATE pacientes SET nombre=%s, dni=%s, telefono=%s, mail=%s WHERE idpac =%s"

            datos=(paciente.nombre, paciente.dni, paciente.telefono, paciente.mail,paciente.idpac)
            cursor.execute(sql,datos)
            db.connection.commit() 
            
            return 'Actualizado'
            
            
        except Exception as ex:
            raise Exception (ex)
        
    
    @classmethod
    def BorrarPac(self,db, id):
        try:
            
            cursor=db.connection.cursor()
            sql="DELETE FROM pacientes WHERE idpac = '{}'" .format(id) 
            
            cursor.execute(sql)
            db.connection.commit()

            return "Borrado"
            

        except Exception as ex:
            raise Exception (ex)