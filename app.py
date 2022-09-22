from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/Docente')
def docente():
    return render_template('vistaDocente.html')

@app.route('/Estudiante')
def estudiante():
    return render_template('vistaEstudiante.html')

@app.route('/Superadmin')
def superAdmin():
    return render_template('vistaSuperAdmin.html')