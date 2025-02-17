'''
Programa principal del juego del ahorcado
'''
import os
import string
import unicodedata
from random import choice
import funciones as fn

def main(archivo_texto:str, nombre_plantilla='plantilla'):
    '''
    Programa principal del juego del ahorcado
    '''
    # cargamos las plantillas
    plantillas = fn.carga_plantillas(nombre_plantilla)
    # cargamos las oraciones
    oraciones = fn.carga_archivo_texto(archivo_texto)
    # obtenemos las palabras
    palabras = fn.obten_palabras(oraciones)
    o = 5 # 5 oportunidades de fallar
    p = choice(palabras) # elegimos una palabra al azar
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    while o>0:
        fn.despliega_plantilla(plantillas, o)
        o = fn.adivina_letra(abcdario, p, adivinadas, o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('Felicidades, adivinaste la palabra')
            break
    print(f"La palabra era: {p}")

if __name__ == '__main__':
    #os.chdir('./curso_ds4/ahorcado')
    archivo = './datos/pg15532.txt'
    main(archivo)