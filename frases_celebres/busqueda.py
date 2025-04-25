''' Programa que busca una lista de palabras en las frases celebres de películas '''
import os
import csv
import argparse

# Función para leer el archivo CSV y devolver una lista de frases
def leer_csv(archivo):
    ''' Lee un archivo CSV y devuelve una lista de frases '''
    frases = []
    with open(archivo, 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        for fila in lector:
            frases.append(fila[0])
    return frases

# Función para buscar palabras en las frases
def buscar_palabras(frases, palabras):
    ''' Busca una lista de palabras en una lista de frases '''
    frases_encontradas = []
    for frase in frases:
        for palabra in palabras:
            if palabra.lower() in frase.lower():
                frases_encontradas.append(frase)
                break
    return frases_encontradas
# Función para mostrar las frases encontradas
def mostrar_frases(frases):
    ''' Muestra una lista de frases '''
    for frase in frases:
        print(frase)
# Función principal
def main(archivo:str,lista_palabras:list):
    ''' Función principal del programa '''
    # Leer el archivo CSV
    frases = leer_csv(archivo)
    # Buscar las palabras en las frases
    frases_encontradas = buscar_palabras(frases, lista_palabras)
    # Mostrar las frases encontradas
    mostrar_frases(frases_encontradas)

if __name__ == '__main__':
    #python busqueda.py fuerza
    #python busqueda.py todos vive fuerza
     # Crear el parser
    parser = argparse.ArgumentParser(description='Buscar palabras en frases célebres de películas.')
    # Añadir argumentos
    parser.add_argument('palabras', nargs='+', help='Lista de palabras a buscar')
    # Parsear los argumentos
    args = parser.parse_args()
    archivo_frases = os.path.join(os.path.dirname(__file__), 'frases_consolidadas.csv')
    # Llamar a la función principal
    main(archivo_frases, args.palabras)
