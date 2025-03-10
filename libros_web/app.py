''' Programa principal de Libros Web '''
from flask import Flask, render_template, request 
import funciones as fn

app = Flask(__name__)

archivo_csv = 'booklist2000.csv'
lista_libros = fn.lee_archivo_csv(archivo_csv)
diccionario_id = fn.crea_diccionario(lista_libros,'id')
diccionario_titulos = fn.crea_diccionario(lista_libros,'title')
diccionario_autores = fn.crea_diccionario(lista_libros,'author')

@app.route('/')
def inicio():
    ''' Página de inicio de la aplicación '''
    return render_template('index.html')

@app.route('/titulo', methods =['GET','POST'])
def busqueda_titulo():
    ''' Página de búsqueda por título '''
    resultado = []
    if request.method == 'POST':
        titulo = request.form['titulo']
        resultado = fn.busca_en_diccionario(diccionario_titulos, titulo)
        print(titulo)
        print(resultado)
    return render_template('titulo.html', lista_libros=resultado)

@app.route('/libro/<id>', methods =['GET'])
def libro(id:str):
    ''' Página de información de un libro '''
    if id in diccionario_id:
        libro = diccionario_id[id]
        return render_template('libro.html', libro=libro)
    else:
        return render_template('libro.html', libro=None)
    
if __name__ == '__main__':
    app.run(debug=True)
