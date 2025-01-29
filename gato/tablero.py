'''
tablero.py: Dibuja el tablero del juego de el gato
'''

def dibuja_tablero(simbolos:dict):
    '''
    Dibuja el tablero del juego de el gato
    '''
    print(f'''
    {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    ---------
    {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    ---------
    {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
    ''')

if __name__ == '__main__':
    numeros = [str(x) for x in range(1, 10)]
    simbolos = {x:x for x in numeros}
    dibuja_tablero(simbolos)
    simbolos['1']='X'
    dibuja_tablero(simbolos)
    simbolos['5']='O'
    dibuja_tablero(simbolos)