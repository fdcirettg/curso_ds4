'''
Scrapper para Reddit
'''
import os
import argparse
from datetime import datetime
import requests
from bs4 import BeautifulSoup
 
def scrap(url:str):
    ''' Obtiene página desde Internet'''
    pagina = requests.get(url,timeout=10)
    if pagina.status_code != 200:
        raise Exception(f'Error {pagina.status_code} en la página {url}')
    return pagina

def guardar_pagina(pagina, nombre_archivo:str):
    ''' Guarda la página en un archivo '''
    with open(nombre_archivo, 'wb') as f:
        f.write(pagina.content)
    print(f'Página guardada en {nombre_archivo}')

def main(url:str, archivo_salida:str):
    ''' Función principal '''
    if not os.path.exists(archivo_salida):
        pagina = scrap(url)
        guardar_pagina(pagina, archivo_salida)
    else:
        print(f'El archivo {archivo_salida} ya existe. Leyendo de él.')
        with open(archivo_salida, 'rb') as f:
            pagina = f.read()
    pagina = scrap(url)
    soup = BeautifulSoup(pagina.content,"html.parser")
    result = soup.find('shreddit-feed')
    for articulo in result.find_all('article', class_='w-full m-0'):
        post = articulo.find('shreddit-post data-ks-item')
        titulo = articulo.contents[3]['post-title']
        #if titulo is not None:
        #    titulo = titulo.text.strip()
        #else:
        #    titulo = 'No hay título'        
        fecha = articulo.contents[3]['created-timestamp']
        if fecha is not None:
            fecha = datetime.strptime(fecha,'%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M')
        #else:
        #    fecha = 'No hay fecha'
        print(f'{fecha} : {titulo}')
        print('----------------------------------')

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrapper para Reddit')
    parser.add_argument('--url', type=str, help='URL de la página de Reddit')
    parser.add_argument('--output', type=str, default='reddit_sw.html')
    parser.add_argument('--force', action='store_true', help='Forzar la descarga de la página')
    args = parser.parse_args()
    url = args.url
    output = args.output
    if args.force:
        if os.path.exists(output):
            os.remove(output)
    if url is None:
        url = "https://www.reddit.com/r/StarWars/"
    
    main(url, output)