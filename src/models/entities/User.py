from werkzeug.security import check_password_hash
from flask_login import UserMixin

class UsuarioVal(UserMixin):
    def __init__(self, idusu, nombre, mail, clave, telefono, profesional) -> None:
        self.id=idusu
        self.nombre=nombre
        self.mail=mail
        self.clave=clave
        self.telefono=telefono
        self.profesional=profesional


    @classmethod
    def check_password(self,clave_bd, clave_form):
        return check_password_hash(clave_bd,clave_form)
     
