# cálculo de coordenadas de líneas 
import funciones

def main():
    m = 2
    b = 3
    x = 5
    y = funciones.calcular_y(x, m, b)
    print(f'Para x = {x}, y = {y}')

if __name__ == '__main__':
    main()
