from flask_login import UserMixin

class TurnoVal(UserMixin):
    def __init__(self, idturno, fecha, horaturno, idprofesional, idpaciente,actividad, estado,horallega,horaatiende) -> None:
        self.idturno=idturno
        self.fecha=fecha
        self.horaturno=horaturno
        self.idprofesional=idprofesional
        self.idpaciente=idpaciente
        self.actividad=actividad
        self.estado=estado
        self.horallega=horallega
        self.horaatiende=horaatiende

        
