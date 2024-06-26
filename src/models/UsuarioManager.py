from .entities.User import UsuarioVal

class UsuarioManager():

    @classmethod
    def login(cls, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT idusu, nombre, mail, clave, telefono, profesional FROM usuario WHERE mail = %s"
            cursor.execute(sql, (usuario.mail,))
            row = cursor.fetchone()
            
            return UsuarioVal(*row) if row else None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(cls, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT idusu, nombre, mail, clave, telefono, profesional FROM usuario WHERE idusu = %s"
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
            
            return UsuarioVal(*row) if row else None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def BuscarTodos(cls, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT idusu, nombre, mail, clave, telefono, profesional FROM usuario"
            
            conditions = []
            params = []
            if usuario.id is not None and int(usuario.id) > 0:
                conditions.append("idusu = %s")
                params.append(usuario.id)

            if conditions:
                sql += " WHERE " + " AND ".join(conditions)

            sql += " ORDER BY nombre"
            
            cursor.execute(sql, params)
            datos = cursor.fetchall()
            
             # Lista para almacenar las instancias de UsuarioVal
            lista_usu = []

            # Itera sobre los resultados de la consulta SQL
            for res in datos:
                # Crea una instancia de UsuarioVal para cada registro
                UsuV = UsuarioVal(
                    idusu=res[0],
                    nombre=res[1],
                    mail=res[2],
                    clave=res[3],
                    telefono=res[4],
                    profesional=res[5]
                )
                # Agrega la instancia a la lista de pacientes
               
                lista_usu.append(UsuV)

            # Ahora `lista_usu` contiene instancias de UsuarioVal que representan los registros de la consulta SQL
            
            return lista_usu if lista_usu else None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def BuscarTodosProf(cls, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT idusu, nombre, mail, clave, telefono, profesional FROM usuario WHERE profesional = 'SI' ORDER BY nombre"
            cursor.execute(sql)
            datos = cursor.fetchall()
            
             # Lista para almacenar las instancias de UsuarioVal
            lista_usu = []

            # Itera sobre los resultados de la consulta SQL
            for res in datos:
                # Crea una instancia de UsuarioVal para cada registro
                UsuV = UsuarioVal(
                    idusu=res[0],
                    nombre=res[1],
                    mail=res[2],
                    clave=res[3],
                    telefono=res[4],
                    profesional=res[5]
                )
                # Agrega la instancia a la lista de pacientes
                lista_usu.append(UsuV)

            # Ahora `lista_usu` contiene instancias de UsuarioVal que representan los registros de la consulta SQL
            
            return lista_usu if lista_usu else None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def AgregarUsu(cls, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO usuario (nombre, mail, clave, telefono, profesional) VALUES (%s, %s, %s, %s, %s)"
            datos = (usuario.nombre, usuario.mail, usuario.clave, usuario.telefono, usuario.profesional)
                   
            cursor.execute(sql, datos)
            db.connection.commit()

            return 'perfecto'

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def EditarUsu(cls, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = "UPDATE usuario SET nombre = %s, mail = %s, clave = %s, telefono = %s, profesional = %s WHERE idusu = %s"
            datos = (usuario.nombre, usuario.mail, usuario.clave, usuario.telefono, usuario.profesional, usuario.id)
            
            cursor.execute(sql, datos)
            db.connection.commit() 
            
            return 'Actualizado'

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def BorrarUsu(cls, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM usuario WHERE idusu = %s"
            cursor.execute(sql, (id,))
            db.connection.commit()

            return "Borrado"

        except Exception as ex:
            raise Exception(ex)