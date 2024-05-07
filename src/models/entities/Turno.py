from flask_login import UserMixin

class TurnoVal(UserMixin):
    def __init__(self, idturno, fecha, horaturno, idprofesional, idpaciente,actividad, estado,horallega,horaatiende, nomprof, nompac) -> None:
        self.idturno=idturno
        self.fecha=fecha
        self.horaturno=horaturno
        self.idprofesional=idprofesional
        self.idpaciente=idpaciente
        self.actividad=actividad
        self.estado=estado
        self.horallega=horallega
        self.horaatiende=horaatiende
        self.nomprof=nomprof
        self.nompac=nompac


class TurnoFil(UserMixin):
    def __init__(self, fechad, fechah, idprofesional, idpaciente) -> None:
        self.fechad=fechad
        self.fechah=fechah
        self.idprofesional=idprofesional
        self.idpaciente=idpaciente
        
