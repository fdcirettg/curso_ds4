'''
funciones auxiliares del juego Ahorcado
'''

def carga_archivo_texto(archivo:str)->list:
    '''
    Carga un archivo de texto y devuelve una lista con las oraciones del archivo
    '''
    with open(archivo, 'r') as file:
        oraciones = file.readlines()
    return oraciones

if __name__ == '__main__':
    lista = carga_archivo_texto('./plantillas/plantilla-0.txt')
    for elemento in lista:
        print(elemento)