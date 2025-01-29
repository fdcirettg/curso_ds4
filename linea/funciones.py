'''archivo con todas las funciones necesarias para la aplicación "linea" '''
import matplotlib.pyplot as plt

def calcular_y(x:float, m:float, b:float)->float:
    '''
    Calcula el valor de y en una línea recta
    x: valor de x
    m: pendiente
    b: intersección en y
    regresa el valor de y
    '''
    return (m*x)+b

def grafica_linea(X: list, Y: list, m:float, b:float):
    '''
    Grafica una línea recta
    X: lista de valores de x
    Y: lista de valores de y
    m: pendiente
    b: intersección en y
    '''
    plt.plot(X,Y)
    plt.title(f'Línea recta con pendiente={m} e intersección en y={b}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()

def test_linea():
    '''
    Comprobamos calcular_y()
    '''
    y  = calcular_y(0.0, 2.0, 3.0)
    return y

if __name__ == '__main__':
    if test_linea() == 3.0:
        print('Test exitoso')
    else:
        print('Test fallido')