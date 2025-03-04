''' Hola mundo de Flask'''
from flask import Flask
app = Flask(__name__)

@app.route('/') #Home page o raíz o índice
def index():
    return '''<html>
                    <head>
                        <title>Hello world</title>
                    </head>
                    <body><h1>Hola mundo</h1>
                        <p>Ir a la página de <a href="/about">Acerca de</a></p>
                    </body>
            </html>'''

@app.route('/about') #Acerca de
def about():
    return '''<html>
                    <head>
                        <title>Acerca de</title>
                    </head>
                    <body><h1>Acerca de</h1>
                        <p>Ir a la página de <a href="/">Inicio</a></p>
                    </body>
            </html>'''

if __name__ == '__main__':
    app.run(debug=True) #Activar el modo de depuración
