'''
Este archivo es el punto de entrada a la aplicación. Aquí se importan las funciones de tablero.py y se ejecutan en un ciclo while.
'''
import tablero

def main():
    ''' Función principal '''
    X = {"G":0,"P":0,"E":0}
    O = {"G":0,"P":0,"E":0}
    score = {"X":X,"O":O}
    numeros = [str(i) for i in range(1,10)]
    corriendo = True
    while corriendo:
        dsimbolos ={x:x for x in numeros}
        g = tablero.juego(dsimbolos)
        tablero.actualiza_score(score,g)
        tablero.despliega_tablero(score)
        seguir = input('Quieres seguir jugando? (s/n): ')
        if seguir.lower() == 'n':
            corriendo = False

if __name__ == '__main__':
    main()