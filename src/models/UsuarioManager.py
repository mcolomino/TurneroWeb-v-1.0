from .entities.User import UsuarioVal

class UsuarioManager():

    @classmethod
    def login(self,db, usuario):
        try:
            
            cursor=db.connection.cursor()
            sql="SELECT idusu, nombre, mail, clave, telefono, profesional FROM usuario WHERE mail = '{}'" .format(usuario.mail) 
            
            cursor.execute(sql)
            row=cursor.fetchone()
            
            if row != None:
                UsuVal=UsuarioVal(row[0],row[1],row[2],row[3],row[4],row[5])
                return UsuVal
            else:
                return None

        except Exception as ex:
            raise Exception (ex)
        
    
    @classmethod
    def get_by_id(self,db, id):
        try:
            
            cursor=db.connection.cursor()
            sql="SELECT idusu, nombre, mail, clave, telefono, profesional FROM usuario WHERE idusu = '{}'" .format(id) 
            
            cursor.execute(sql)
            row=cursor.fetchone()
            
            if row != None:
                UsuVal=UsuarioVal(row[0],row[1],row[2],row[3],row[4],row[5])
                return UsuVal
            
            else:
                return None

        except Exception as ex:
            raise Exception (ex)
    

    @classmethod
    def BuscarTodos(self,db, usuario):
        try:
            
            cursor=db.connection.cursor()
            sql="SELECT idusu, nombre, mail, clave, telefono, profesional FROM usuario ORDER BY nombre" 
            
            cursor.execute(sql)
            datos=cursor.fetchall()
            
            if datos != None:
                return datos
            
            else:
                return None

        except Exception as ex:
            raise Exception (ex)
    

    @classmethod
    def BuscarTodosProf(self,db, usuario):
        try:
            
            cursor=db.connection.cursor()
            sql="SELECT idusu, nombre, mail, clave, telefono, profesional FROM usuario WHERE profesional = 'SI' ORDER BY nombre" 
            
            cursor.execute(sql)
            datos=cursor.fetchall()
            
            if datos != None:
                return datos
            
            else:
                return None

        except Exception as ex:
            raise Exception (ex)
        

    @classmethod
    def AgregarUsu(self,db, usuario):
        try:
            
            cursor=db.connection.cursor()
            sql="INSERT INTO usuario (nombre, mail, clave, telefono, profesional)  VALUES (%s,%s,%s,%s,%s)" 
            datos=(usuario.nombre, usuario.mail, usuario.clave,usuario.telefono,usuario.profesional)
                   
            cursor.execute(sql,datos)
            db.connection.commit()

            return 'perfecto'

        except Exception as ex:
            raise Exception (ex)
   

    @classmethod
    def EditarUsu(self,db, usuario):
        try:
            
            cursor=db.connection.cursor()
            sql="UPDATE usuario SET nombre=%s, mail=%s, clave=%s, telefono=%s, profesional=%s WHERE idusu =%s"

            datos=(usuario.nombre, usuario.mail, usuario.clave,usuario.telefono,usuario.profesional,usuario.id)
            cursor.execute(sql,datos)
            db.connection.commit() 
            
            return 'Actualizado'
            
            
        except Exception as ex:
            raise Exception (ex)
        
    
    @classmethod
    def BorrarUsu(self,db, id):
        try:
            
            cursor=db.connection.cursor()
            sql="DELETE FROM usuario WHERE idusu = '{}'" .format(id) 
            
            cursor.execute(sql)
            db.connection.commit()

            return "Borrado"
            

        except Exception as ex:
            raise Exception (ex)