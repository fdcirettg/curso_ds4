# cálculo de coordenadas de líneas 
import funciones
import argparse


def main(m:float, b:float):
    '''
    Función principal que calcula las coordenadas de una línea recta
    Recibimos m y b
    Regresa: nada'''
    #m = 2.0
    #b = 3.0
    #X = [x for x in range(1,11)]
    #Y = [funciones.calcular_y(x, m, b) for x in X]
    #print("Enteros:")
    #coordenadas_enteros = list(zip(X,Y))
    #print(coordenadas_enteros)
    XF = [x/10.0 for x in range(10,110,5)]
    YF = [funciones.calcular_y(x, m, b) for x in XF]
    coordenadas_flotantes = list(zip(XF,YF))
    print("Flotantes:")
    print(coordenadas_flotantes)

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', type=float, help='Pendiente de la línea', default=2.0)
    parser.add_argument('-b', type=float, help='Ordenada al origen', default=3.0)
    args = parser.parse_args()
    main(args.m, args.b)
    #main(m=2.0, b=3.0)
