'''
Scrapper para wikipedia
'''
import os
import argparse
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
        pagina = pagina.content
        pagina= str(pagina, 'utf-8')
    else:
        print(f'El archivo {archivo_salida} ya existe. Leyendo de él.')
        with open(archivo_salida, 'rb') as f:
            pagina = f.read()
        pagina= str(pagina, 'utf-8')
    soup = BeautifulSoup(pagina,"html.parser")
    #main_content = soup.find('div', class_='mw-body-content')
    main_content = soup.find('div', id='mw-pages')
    if main_content:
        lis = main_content.find_all('li')
        diccionario_lis = {}
        print(f"Encontré {len(lis)} elementos <li> en la página")
        for li in lis:
            #print(f"{li.a.get('href')} : {li.a.text.strip()}")
            if li.a is not None:
                diccionario_lis[li.a.text.strip()] = li.a.get('href')
        lista = [{'pelicula':k,'link:':v} for k,v in diccionario_lis.items()]
        print(lista)
        archivo_salida = archivo_salida.replace('.html', '.json')
        with open(archivo_salida, 'w', encoding='utf8') as f:
            f.write(str(lista))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrapper para Wikipedia')
    parser.add_argument('--url', type=str, help='URL de la página de Wikipedia')
    parser.add_argument('--output', type=str, default='wiki.html')
    args = parser.parse_args()
    url = args.url
    output = args.output
    if not url:
        #url = "https://es.wikipedia.org/wiki/Anexo:Pel%C3%ADculas_de_ciencia_ficci%C3%B3n"
        url = "https://es.wikipedia.org/wiki/Categor%C3%ADa:Pel%C3%ADculas_de_terror_sobrenatural"
    if not output:
        output = 'wiki.html'

    main(url, output)