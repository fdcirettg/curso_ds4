''' Programa principal de movieDatabase '''
from flask import Flask, render_template, request, redirect, url_for
import random
import os
import movie_clases as mc

app = Flask(__name__)
sistema = mc.SistemaCine()
ruta = 'datos/movies_db - '
actores_csv = ruta + 'actores.csv'
peliculas_csv = ruta + 'peliculas.csv'
relaciones_csv = ruta + 'relacion.csv'
users_csv = ruta + 'users.csv'
sistema.cargar_csv(actores_csv,mc.Actor)
sistema.cargar_csv(peliculas_csv,mc.Pelicula)
sistema.cargar_csv(relaciones_csv,mc.Relacion)
sistema.cargar_csv(users_csv,mc.User)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/actores')
def actores():
    ''' Muestra la lista de actores '''
    lista_actores = sistema.actores.values()
    return render_template('actores.html', actores=lista_actores)

@app.route('/peliculas')
def peliculas():
    ''' Muestra la lista de peliculas '''
    lista_peliculas = sistema.peliculas.values()
    return render_template('peliculas.html', peliculas=lista_peliculas)

@app.route('/actor/<int:id_actor>')
def actor(id_actor):
    ''' Muestra la información de un actor '''
    actor = sistema.actores[id_actor]
    personajes = sistema.obtener_personajes_por_estrella(id_actor)
    return render_template('actor.html', actor=actor,lista_peliculas=personajes)

@app.route('/pelicula/<int:id_pelicula>')
def pelicula(id_pelicula):
    ''' Muestra la información de una pelicula '''
    pelicula = sistema.peliculas[id_pelicula]
    actores = sistema.obtener_personajes_por_pelicula(id_pelicula)
    return render_template('pelicula.html', pelicula=pelicula, lista_actores=actores)

if __name__ == '__main__':
    app.run(debug=True)
