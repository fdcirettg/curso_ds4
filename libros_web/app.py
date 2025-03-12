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
    return render_template('inicio.html')

@app.route('/titulos', methods =['GET','POST'])
def busqueda_titulo():
    ''' Página de búsqueda por título '''
    resultado = []
    if request.method == 'POST':
        titulo = request.form['titulo']
        resultado = fn.busca_en_diccionario(diccionario_titulos, titulo)
        print(titulo)
        print(resultado)
    return render_template('titulos.html', lista_libros=resultado)

@app.route('/libro/<id_libro>', methods =['GET'])
def libro(id_libro:str):
    ''' Página de información de un libro '''
    if id_libro in diccionario_id:
        book = diccionario_id[id_libro]
        return render_template('libros.html', libro=book)
    else:
        return render_template('libros.html', libro=None)
    
@app.route('/letra/', methods =['GET'])
def plantilla_letra():
    ''' Página de búsqueda por letra '''
    return render_template('por_letra.html', lista_libros=[])

@app.route('/letra/<letra>', methods =['GET'])
def busqueda_letra(letra:str):
    ''' Página de búsqueda por letra '''
    resultado = fn.libros_empiezan_con(lista_libros, letra)
    return render_template('por_letra.html', lista_libros=resultado)

@app.route('/titulo',  methods =['GET','POST'])
def title():
    ''' Página de búsqueda por título '''
    print(request.method)
    resultado = []
    if request.method == 'POST':
        titulo = request.form.get('searchInput', '')
        resultado = fn.busca_en_diccionario(diccionario_titulos, titulo)
    return render_template('titulos.html', lista_libros=resultado)

if __name__ == '__main__':
    app.run(debug=True)
