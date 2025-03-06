''' Archivo con las funciones necesarias de la Aplicación Libro Web'''
import csv

def lee_archivo_csv(archivo:str)->list:
    ''' Lee un archivo CSV y lo convierte en una lista de diccionarios '''
    with open(archivo, "r", encoding='utf8') as f:
        return [x for x in csv.DictReader(f)]

def crea_diccionario(lista:list, llave:str)->dict:
    ''' Crea un diccionario con la palabra "llave" como clave y el resto de los datos como valores '''
    return {x[llave].lower(): x for x in lista}

def busca_en_diccionario(diccionario:dict, palabra:str)->list:
    ''' Busca palabra en llave de la lista de diccionarios '''
    lista = []
    palabra = palabra.lower()
    for llave, libro in diccionario.items():
        if palabra in llave.lower():
            lista.append(libro)
    return lista

def libros_empiezan_con(lista:list, letra:str)->list:
    ''' Busca libros que empiecen con letra '''
    return [x for x in lista if x['title'].lower().startswith(letra.lower())]

if __name__ == '__main__':
    archivo_csv = 'booklist2000.csv'
    lista_libros = lee_archivo_csv(archivo_csv)
    diccionario_libros = crea_diccionario(lista_libros,'title')
    resultado = busca_en_diccionario(diccionario_libros, 'rebels')
    print(resultado)
    diccionario_autores = crea_diccionario(lista_libros,'author')
    resultado = busca_en_diccionario(diccionario_autores, 'Sandra')
    print(resultado)
    resultado = libros_empiezan_con(lista_libros, 'a')
    print(f'Libros que empiezan con "A": {len(resultado)}')