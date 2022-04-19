from os import path
from flask import Flask, render_template, request
from Procesos import *

app = Flask(__name__)

titulos = ("Documento", "Nombre", "Apellido",
           "Telefono", "Email", "Password", "Tipo")
titulosTablaUsuarios = ("Documento", "Nombre", "Apellido",
                        "Telefono", "Email", "Password", "Tipo")
datos = []

listaDatosPerfil = ["Documento", "Nombre", "Apellido",
                    "Telefono", "Email", "Password", "Tipo"]
misProcesos = Procesos()
#misProcesos.llenarListaUsuarios()


@app.route("/")
def registro_usuario():
    return render_template('index.html')


@app.route("/consultar")
def consulta():
    informacion = misProcesos.obtenerListaUsuarios()
    return render_template('consulta.html', titulos_tabla=titulosTablaUsuarios, data=informacion, user=Procesos.usuarioGlobal)


@app.route("/valida_usuarios", methods=['GET', 'POST'])
def valida_usuarios():
    resultado = ""
    if request.method == 'POST':

        usuario = None
        documento = request.form['documento']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        email = request.form['email']
        password = request.form['password']
        tipo = request.form['tipo']

        if ('buscar' in request.form):
            usuario = misProcesos.consultarUsuario(documento)
            if(usuario == None):
                resultado = "El usuario no se encuentra registrado!"
        elif('registrar' in request.form):
            print("Registrar")
            usuario = misProcesos.consultarUsuario(documento)
            if usuario == None:
                usuario = Usuario(documento, nombre, apellido,
                                  telefono, email, password, tipo)

                resultado = misProcesos.registrarUsuarios(usuario)
            else:
                resultado = f"El documento ya se encuentra registrado y corresponde a {usuario.nombre}"
        elif('actualizar' in request.form):
            print("actualizar")
            usuario = Usuario(documento, nombre, apellido,
                              telefono, email, password, tipo)
            resultado = misProcesos.actualizarUsuario(usuario)
        elif('eliminar' in request.form):
            print("eliminar")
            usuario = None
            resultado = misProcesos.eliminarUsuario(documento)

        print("**********************")
        print("DATOS DE USUARIO", usuario)
        if(usuario != None):
            datos = {
                "documento": usuario.documento,
                "nombre": usuario.nombre,
                "apellido": usuario.apellido,
                "telefono": usuario.telefono,
                "email": usuario.email,
                "password": usuario.password,
                "tipo": usuario.tipo,
            }
        else:
            datos = {
                "documento": "",
                "nombre": "",
                "apellido": "",
                "edad": "",
                "telefono": "",
                "email": "",
                "password": "",
                "tipo": "",
            }

            print(datos)
    return render_template('gestionUsuario.html', usuario=datos, user=Procesos.usuarioGlobal)


@app.route("/login", methods=['POST'])
def inicio_sesion():
    if (request.method == 'POST'):
        usuario = request.form['usuario']
        password = request.form['password']
        Procesos.usuarioGlobal = misProcesos.consultarUsuario(usuario)
        print(f"usuario Ingresado:{usuario}, pass:{password}")
        print(f"usuario encontrado:{Procesos.usuarioGlobal}")
        if Procesos.usuarioGlobal != None:
            if(usuario == Procesos.usuarioGlobal.documento and password == Procesos.usuarioGlobal.password):
                return render_template('bienvenidad.html', user=Procesos.usuarioGlobal)

            print("¨*********************S****************")
            perfil = []
            perfil.append(usuario.documento)
            perfil.append(usuario.nombre)
            perfil.append(usuario.apellido)
            perfil.append(usuario.telefono)
            perfil.append(usuario.email)
            perfil.append(usuario.password)
            perfil.append(usuario.tipo)
            print(perfil)
            listaDatosPerfil.append(perfil)

        return render_template('login.html', user=None)


@app.route("/ya_tienes_cuenta")
def ya_tienes_cuenta():
    return render_template('login.html', user=Procesos.usuarioGlobal)


@app.route("/inicio")
def inicio():
    return render_template('index.html', user=Procesos.usuarioGlobal)


@app.route("/registro")
def registro():
    return render_template('registro.html', user=Procesos.usuarioGlobal)


@app.route("/ayudaUsuario")
def ayuda():
    return render_template('ayudaUsuario.html')

@app.route("/gestionUsuario")
def gestion_usuario():
    return render_template('gestionUsuario.html', user=Procesos.usuarioGlobal)

@app.route("/login2")
def ventanaBienvenidad():
    return render_template('bienvenidad.html', user=Procesos.usuarioGlobal)

@app.route("/perfil", methods=['GET', 'POST'])
def perfil():
    print("*******************")
    print("*******************")
    print("*******************")
    print("*******************")
    print("*******************")
    datPeronal = listaDatosPerfil
    print(datPeronal)
    return render_template('perfil.html',titulos_tabla=titulosTablaUsuarios, yoo=datPeronal)


@app.route("/registrar_persona", methods=['GET', 'POST'])
def registrar_persona():
    resultado = None
    documento, nombre, apellido, telefono, email, password, tipo = "", "", "", "", "", "", ""

    if (request.method == 'POST'):
        documento = request.form['documento']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        password = request.form['password']
        telefono = request.form['telefono']
        tipo = int(request.form['tipo'])

        print("Registrar")

        usuario = misProcesos.consultarUsuario(documento)
        if usuario == None:
            usuario = Usuario(documento, nombre, apellido,
                              telefono, email, password, tipo)
            resultado = misProcesos.registrarUsuarios(usuario)
        else:
            resultado = f"¿Lo sentimos! El documento ya se encuentra registrado y corresponde a {usuario.nombre}"

        datos2 = {
            "resultado": resultado
        }

        print("¨*********************S****************")

        
        for i in range(len(listaDatosPerfil)):
            
            print("perfil")
            if listaDatosPerfil[0] != usuario.documento:
                listaDatosPerfil[0] = usuario.documento
            if listaDatosPerfil[1] != usuario.nombre:
                listaDatosPerfil[1] = usuario.nombre
            if listaDatosPerfil[2] != usuario.apellido:
                listaDatosPerfil[2] = usuario.apellido
            if listaDatosPerfil[3] != usuario.telefono:
                listaDatosPerfil[3] = usuario.telefono
            if listaDatosPerfil[4] != usuario.email:
                listaDatosPerfil[4] = usuario.email
            if listaDatosPerfil[5] != usuario.password:
                listaDatosPerfil[5] = usuario.password
            if listaDatosPerfil[6] != usuario.tipo:
                listaDatosPerfil[6] = usuario.tipo
            
        print(listaDatosPerfil)
        print("¨*********************S****************")
        print("¨*********************S****************")
        print("¨*********************S****************")

    return render_template('registro.html', data=datos2)


if(__name__ == '__main__'):
    app.run(debug=True, port=5000)
