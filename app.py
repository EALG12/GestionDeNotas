from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/iniciarSesion')
def registro():
    return render_template('vistaInicioSesion.html')

@app.route('/Registro')
def registro():
    return render_template('vistaRegistro.html')

@app.route('/recuperarContrasena')
def recuperarContrasena():
    return render_template('vistaRecuperarContrasena.html')

@app.route('/cambiarContrasena')
def cambiarContrasena():
    return render_template('vistaCambiarContrasena.html')

@app.route('/enviarMensaje')
def enviarMensaje():
    return render_template('vistaEnviarMensaje.html')

@app.route('/leerMensajes')
def leerMensaje():
    return render_template('vistaLeerMensajes.html')
