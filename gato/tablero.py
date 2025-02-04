'''
tablero.py: Dibuja el tablero del juego del gato
'''
import random

def dibuja_tablero(simbolos:dict):
    '''  Dibuja el tablero del juego de el gato '''
    print(f'''
    {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    ---------
    {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    ---------
    {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
    ''')

def ia(simbolos:dict):
    ''' Estrategia de la computadora'''
    ocupado = True
    while ocupado is True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X','O']:
            simbolos[x] = 'O'
            ocupado = False

def usuario(simbolos:dict):
    ''' Estrategia del usuario '''
    ocupado = True
    lista_numeros = [str(i) for i in range(1,10)] #del 1 al 9
    while ocupado is True:
        x = input('Elija un número del 1 al 9: ')
        if x in lista_numeros:
            if simbolos[x] not in ['X','O']:
                simbolos[x] = 'X'
                ocupado = False
            else:
                print('Esa casilla ya está ocupada')
        else:
            print('Elija un número del 1 al 9')

def juego(simbolos:dict):
    ''' Juego del gato '''
    lista_combinaciones = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['1','4','7'],
        ['2','5','8'],
        ['3','6','9'],
        ['1','5','9'],
        ['3','5','7']
    ]
    en_juego = True
    dibuja_tablero(simbolos)
    movimientos = 0
    while en_juego:
        usuario(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_winner(simbolos,lista_combinaciones)
        if gana is not None:
            en_juego = False
        if movimientos >= 9:
            en_juego = False
            continue
        ia(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_winner(simbolos,lista_combinaciones)
        if gana is not None:
            en_juego = False
        if movimientos >= 9:
            en_juego = False
            continue



def checa_winner(simbolos:dict, combinaciones:list):
    ''' Checa si hay un ganador '''
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]]:
            return simbolos[c[0]]
    return None

if __name__ == '__main__':
    numeros = [str(i) for i in range(1,10)]
    dsimbolos = {x:x for x in numeros}
    juego(dsimbolos)
    '''
    dibuja_tablero(dsimbolos)
    ia(dsimbolos)
    dibuja_tablero(dsimbolos)
    usuario(dsimbolos)
    dibuja_tablero(dsimbolos)
    
    x = random.choice(numeros)
    numeros.remove(x)
    dsimbolos[x] = 'X'
    dibuja_tablero(dsimbolos)
    o = random.choice(numeros)
    numeros.remove(o)
    dsimbolos[o] = 'O'
    dibuja_tablero(dsimbolos)
    print(numeros)
    '''