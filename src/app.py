from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect
from flask_paginate import Pagination, get_page_args
from datetime import datetime, date, time
from config import config

#Models
from models.UsuarioManager import UsuarioManager
from models.PacienteManager import PacienteManager
from models.TurnoManager import TurnoManager

#Entities
from models.entities.User import UsuarioVal
from models.entities.Paciente import PacienteVal
from models.entities.Turno import TurnoVal
from models.entities.Turno import TurnoFil

app=Flask(__name__)

csrf=CSRFProtect()
db=MySQL(app)

login_manager_app=LoginManager(app)
   
@login_manager_app.user_loader
def load_user(id):
    return UsuarioManager.get_by_id(db,id)


@app.route('/')
def index():
    return redirect(url_for('inicio'))

# FUNCION IR A PAGINA PRINCIPAL
@app.route('/inicio')
def inicio():
    '''
    fecha=datetime.strftime(datetime.now(),'%d/%m/%Y')
    print(fecha)
    hora=datetime.strftime(datetime.now(),'%H:%M')
    print (hora)
    '''
    #fecha = datetime.now().strftime('%Y-%m-%d')
    #print(fecha)
    
    return render_template('inicio.html')
    #return render_template('aaa.html')


@app.route('/logueo')
def logueo():
    return redirect(url_for('login'))


####################################
### INICIO FUNCIONES LOGIN Y LOGOUT

# INICIAR SESION
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        #print(request.form['usuario'])
        #print(request.form['clave'])
        user=UsuarioVal(0,"",request.form['usuario'],request.form['clave'],1,"")
        UsuLog=UsuarioManager.login(db,user)
        
        if UsuLog != None:
            #flash("Usuario encontrado...")
            if user.clave == UsuLog.clave:
                 login_user(UsuLog)
                 return redirect(url_for("principal"))
            else:
                flash("Clave incorrecta...")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

# CERRAR SESION
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('inicio'))


      

### FIN FUNCIONES LOGIN Y LOGOUT
####################################

# FUNCION IR A PAGINA PRINCIPAL
@app.route('/principal')
@login_required
def principal():

    #actualizar estado "En Agenda" de turnos pasados ( menores a fecha actual) a "Ausente"
    fecha = datetime.now().strftime('%Y-%m-%d')
    Tur=TurnoVal(0,fecha,"","", "", "", "", "", "")
    
    NewTur=TurnoManager.actausentes(db,Tur)    

    return render_template('principal.html')


#########################################
### INICIO FUNCIONES PAGINA USUARIOS.HTML

# FUNCION IR A PAGINA USUARIOS.HTML (la llamo desde el menú item Usuarios y carga la tabla con los usuarios de la BD)
@app.route('/usuarios', methods=['GET', 'POST'])
@login_required
def usuarios():
    paginated_data = []
    data = []
    pagination = None
    page, per_page, offset=get_page_args(page_parameter='page', per_page_parameter='per_page')
    
    idusu = 0
    if request.method=='POST':
        idusu = request.form['ususel']
        user=UsuarioVal(idusu,"","","",1,"")
    else:
        user=UsuarioVal(0,"","","",1,"")

    TodUsu=UsuarioManager.BuscarTodos(db,user)
    
    total=len(TodUsu)   
    paginated_data=TodUsu[offset: offset + per_page]
    pagination=Pagination(page=page, per_page=per_page,total=total, css_framework='bootstrap5')

    return render_template('usuarios.html',Lista = paginated_data, Pagination=pagination)

@app.route('/AltaUsuario', methods=['POST'])
@login_required
def AltaUsuario():
    if request.method=='POST':
        if request.form.get('chkprof')=='SI':
            prof="SI"
        else:
            prof="NO"

        user=UsuarioVal(0,request.form['nombre'],request.form['mail'],request.form['clave'],request.form['telefono'],prof)
        NewUsu=UsuarioManager.AgregarUsu(db,user)
        
        return redirect(url_for("usuarios"))
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request


@app.route('/EditarUsuario/<id>', methods=['POST'])
@login_required
def EditarUsuario(id):
    print(id)
    if request.method=='POST':
       
        if request.form.get('chkprof')=='SI':
            prof="SI"
        else:
            prof="NO"

        user=UsuarioVal(id,request.form['nombre'],request.form['mail'],request.form['clave'],request.form['telefono'],prof)
        NewUsu=UsuarioManager.EditarUsu(db,user)
        
        return redirect(url_for("usuarios"))
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request


@app.route('/BorrarUsuario/<id>')
@login_required
def BorrarUsuario(id):
    
    DelUsu=UsuarioManager.BorrarUsu(db,id)
    if DelUsu=='Borrado':
        return redirect(url_for("usuarios"))
        
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request



### FIN FUNCIONES PAGINA USUARIOS.HTML
######################################





#########################################
### INICIO FUNCIONES PAGINA PACIENTES.HTML


@app.route('/pacientes', methods=['GET', 'POST'])
@login_required
def pacientes():
    paginated_data = []
    data = []
    pagination = None
    page, per_page, offset=get_page_args(page_parameter='page', per_page_parameter='per_page')
    
    idpac = 0
    if request.method=='POST':
        idpac = request.form['pacsel']
        Pac=PacienteVal(idpac,"","","","")
    else:
        Pac=PacienteVal(0,"","","","")
    
    TodPac=PacienteManager.BuscarTodos(db,Pac)
    
    total=len(TodPac)   
    paginated_data=TodPac[offset: offset + per_page]
    pagination=Pagination(page=page, per_page=per_page,total=total, css_framework='bootstrap5')

    #buscar todos los pacientes y pasarlos para llenar los combos 
    Pac=PacienteVal(0,"","","","")
    TodPac=PacienteManager.BuscarTodos(db,Pac)

    return render_template('pacientes.html',Lista = paginated_data, TodPac = TodPac, idpac = idpac, Pagination=pagination)

@app.route('/AltaPaciente', methods=['POST'])
@login_required
def AltaPaciente():
    if request.method=='POST':
       
        Pac=PacienteVal(0,request.form['nombre'],request.form['dni'],request.form['telefono'], request.form['mail'])
        NewPac=PacienteManager.AgregarPac(db,Pac)
        
        return redirect(url_for("pacientes"))
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request


@app.route('/EditarPaciente/<id>', methods=['POST'])
@login_required
def EditarPaciente(id):
    
    if request.method=='POST':
       Pac=PacienteVal(id,request.form['nombre'],request.form['dni'],request.form['telefono'], request.form['mail'])
       NewPac=PacienteManager.EditarPac(db,Pac)
        
       return redirect(url_for("pacientes"))
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request


@app.route('/BorrarPaciente/<id>')
@login_required
def BorrarPaciente(id):
    
    DelPac=PacienteManager.BorrarPac(db,id)
    if DelPac=='Borrado':
        return redirect(url_for("pacientes"))
        
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request



### FIN FUNCIONES PAGINA PACIENTES.HTML
######################################



#########################################
### INICIO FUNCIONES PAGINA TURNOS.HTML


@app.route('/turnos', methods=['GET', 'POST'])
@login_required
def turnos():
    paginated_data = []
    data = []
    pagination = None
    page, per_page, offset=get_page_args(page_parameter='page', per_page_parameter='per_page')
    
    idprof=0
    idpac=0
    fechad = datetime.now().strftime('%Y-%m-%d')
    fechah = datetime.now().strftime('%Y-%m-%d')
    
    if request.method=='POST':
        idprof = request.form['professel']
        idpac = request.form['pacsel']
        fechad = request.form['fechad']
        fechah = request.form['fechah']
        #crear un Turno filtro con prof, pac, fecdes, fechas
        TurFil=TurnoFil(request.form['fechad'],request.form['fechah'],request.form['professel'],request.form['pacsel'])
    else:
        TurFil=TurnoFil(None,None,None,None)

    #print (TurFil.idprofesional)
    TodTur=TurnoManager.BuscarTodos(db,TurFil)
    total=len(TodTur)   
    paginated_data=TodTur[offset: offset + per_page]
    pagination=Pagination(page=page, per_page=per_page,total=total, css_framework='bootstrap5')

    #buscar los usuarios profesionales y pasarlos para llenar los combos 
    user=UsuarioVal(0,"","","",1,"")
    TodUsuProf=UsuarioManager.BuscarTodosProf(db,user)
    
    #buscar todos los pacientes y pasarlos para llenar los combos 
    Pac=PacienteVal(0,"","","","")
    TodPac=PacienteManager.BuscarTodos(db,Pac)

    #crear lista de estados
    Estados = ["En Agenda", "En Espera", "Atendido", "Ausente", "Cancelado"]
    #crear lista de actividades
    Actividades = ["Consulta", "Control"]

    #print (TodPac)
    return render_template('turnos.html',Lista = paginated_data, Lacti = Actividades, Lesta = Estados, ListaProf = TodUsuProf, ListaPac = TodPac, idprof = idprof, idpac = idpac, fechad = fechad, fechah = fechah, Pagination=pagination)
    


@app.route('/AltaTurno', methods=['POST'])
@login_required
def AltaTurno():
    if request.method=='POST':
        #print(request.form['reg_fecha'])
        #print(request.form['reg_prof'])
        #print(request.form['reg_pac'])
        
        Tur=TurnoVal(0, request.form['reg_fecha'], request.form['hora'], request.form['reg_prof'], request.form['reg_pac'], request.form['reg_act'], "En Agenda", "", "")
        print (Tur)
        NewTur=TurnoManager.AgregarTur(db,Tur)
        
        return redirect(url_for("turnos"))
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request


@app.route('/EditarTurno/<id>', methods=['POST'])
@login_required
def EditarTurno(id):
    
       
    if request.method=='POST':
       
        print(request.form.getlist('edit_prof'))
        print(request.form.getlist('edit_pac'))
        Tur=TurnoVal(id,request.form['edit_fecha'],request.form['edit_hora'],request.form.getlist('edit_prof'), request.form.getlist('edit_pac'), request.form['edit_act'], request.form['edit_estado'], request.form['edit_horallega'], request.form['edit_horaatiende'])
        
        NewTur=TurnoManager.EditarTur(db,Tur)
        
        return redirect(url_for("turnos"))
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request


@app.route('/BorrarTurno/<id>')
@login_required
def BorrarTurno(id):
    
    DelTur=TurnoManager.BorrarTur(db,id)
    if DelTur=='Borrado':
        return redirect(url_for("turnos"))
         
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request



### FIN FUNCIONES PAGINA TURNOS.HTML
######################################


#########################################
### INICIO FUNCIONES PAGINA TURNOS.HTML


@app.route('/sala', methods=['GET', 'POST'])
@login_required
def sala():
    paginated_data = []
    data = []
    pagination = None
    page, per_page, offset=get_page_args(page_parameter='page', per_page_parameter='per_page')
    
    #buscar los usuarios profesionales y pasarlos para llenar los combos 
    user=UsuarioVal(0,"","","",1,"")
    TodUsuProf=UsuarioManager.BuscarTodosProf(db,user)
    
    idprof=0
    for elemento in TodUsuProf:
        idprof = elemento[0]
        break


    #idpac=0
    fechad = datetime.now().strftime('%Y-%m-%d')
    fechah = datetime.now().strftime('%Y-%m-%d')
    if request.method=='POST':
        idprof = request.form['professel']
        #idpac = request.form['pacsel']
        fechad = request.form['fechad']
        #fechah = request.form['fechah']
        #crear un Turno filtro con prof, pac, fecdes, fechas
        TurFil=TurnoFil(fechad,fechad,request.form['professel'],0)
    else:
        TurFil=TurnoFil(fechad,fechah,idprof,None)


    TodTur=TurnoManager.BuscarTodos(db,TurFil)
    total=len(TodTur)   
    paginated_data=TodTur[offset: offset + per_page]
    pagination=Pagination(page=page, per_page=per_page,total=total, css_framework='bootstrap5')
    
    return render_template('sala.html',Lista = paginated_data, ListaProf = TodUsuProf, idprof = idprof, fechad = fechad, Pagination=pagination)

#actualiza estado de turnos

@app.route('/enagenda/<id>', methods=['POST'])
@login_required
def enagenda(id):
    
    if request.method=='POST':
       
        Tur=TurnoVal(id,"","","", "", "", "En Agenda", "", "")
       
        NewTur=TurnoManager.actestado(db,Tur)
        
        return redirect(url_for("sala"))
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request

@app.route('/enespera/<id>', methods=['POST'])
@login_required
def enespera(id):
    
    if request.method=='POST':
        horallega=hora=datetime.strftime(datetime.now(),'%H:%M')
    
        Tur=TurnoVal(id,"","","", "", "", "En Espera", horallega, "")
       
        NewTur=TurnoManager.actestado(db,Tur)
        
        return redirect(url_for("sala"))
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request

@app.route('/atendido/<id>', methods=['POST'])
@login_required
def atendido(id):
    
    if request.method=='POST':
        
        horaatiende=hora=datetime.strftime(datetime.now(),'%H:%M')

        Tur=TurnoVal(id,"","","", "", "", "Atendido", "", horaatiende)
       
        NewTur=TurnoManager.actestado(db,Tur)
        
        return redirect(url_for("sala"))
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request
    
@app.route('/ausente/<id>', methods=['POST'])
@login_required
def ausente(id):
    
    if request.method=='POST':
       
        Tur=TurnoVal(id,"","","", "", "", "Ausente", "", "")
       
        NewTur=TurnoManager.actestado(db,Tur)
        
        return redirect(url_for("sala"))
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request

@app.route('/cancelado/<id>', methods=['POST'])
@login_required
def cancelado(id):
    
    if request.method=='POST':
       
        Tur=TurnoVal(id,"","","", "", "", "Cancelado", "", "")
       
        NewTur=TurnoManager.actestado(db,Tur)
        
        return redirect(url_for("sala"))
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request




### FIN FUNCIONES PAGINA SALA.HTML
######################################





# gestor de errores
def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__=='__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(404,status_404)
    app.run()
    