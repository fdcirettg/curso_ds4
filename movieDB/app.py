''' Programa principal de MovieDB '''
from flask import Flask, request, url_for, render_template, redirect
import os
import random
import movie_classes as mc

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Clave secreta para la sesión
sistema = mc.SistemaCine()
archivo_actores    = "datos/movies_db - actores.csv"
archivo_peliculas  = "datos/movies_db - peliculas.csv"
archivo_relaciones = "datos/movies_db - relacion.csv"
archivo_usuarios   = "datos/movies_db - users_hashed.csv"
sistema.cargar_csv(archivo_actores, mc.Actor)
sistema.cargar_csv(archivo_peliculas, mc.Pelicula)
sistema.cargar_csv(archivo_relaciones, mc.Relacion)
sistema.cargar_csv(archivo_usuarios, mc.User)

@app.route('/')
def index():
    ''' Página principal de la aplicación '''
    return render_template('index.html')

@app.route('/actores')
def actores():
    ''' Muestra la lista de actores '''
    actores = sistema.actores.values()
    return render_template('actores.html', actores=actores)

@app.route('/peliculas')
def peliculas():
    ''' Muestra la lista de películas '''
    peliculas = sistema.peliculas.values()
    return render_template('peliculas.html', peliculas=peliculas)

@app.route('/actor/<int:id_actor>')
def actor(id_actor):
    ''' Muestra la información de un actor '''
    actor = sistema.actores[id_actor]
    personajes = sistema.obtener_personajes_por_estrella(id_actor)
    return render_template('actor.html', actor=actor, lista_peliculas=personajes)

@app.route('/login', methods=['GET', 'POST'])
def login():
    ''' Muestra el formulario de login '''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        exito = sistema.login(username, password)
        if exito:
            session['logged_in'] = True
            session['username'] = sistema.usuario_actual.nombre_completo
            return redirect(url_for('index'))
        else:
            error = 'Usuario o contraseña incorrectos'
            return render_template('login.html'))
    return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=True)
