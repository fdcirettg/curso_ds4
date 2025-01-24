# archivo con todas las funciones necesarias para la aplicación "linea"
def calcular_y(x, m, b):
    '''
    Calcula el valor de y en una línea recta
    x: valor de x
    m: pendiente
    b: intersección en y
    regresa el valor de y
    '''
    return (m*x)+b
def test_linea():
    '''
    Comprobamos calcular_y()
    '''
    y  = calcular_y(0, 2, 3)
    return y

if __name__ == '__main__':
    if test_linea() == 3:
        print('Test exitoso')
    else:
        print('Test fallido')