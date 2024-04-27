from flask_login import UserMixin

class PacienteVal(UserMixin):
    def __init__(self, idpac, nombre, dni, telefono, mail) -> None:
        self.idpac=idpac
        self.nombre=nombre
        self.dni=dni
        self.telefono=telefono
        self.mail=mail
        
