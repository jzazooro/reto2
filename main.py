from funciones.funcion1 import *
from funciones.funcion2 import *

def main():
    neuronas = [2, 4, 8, 1]
    funciones_activacion=[relu, relu, sigmoid]

    for paso in range(len(neuronas)-1):
        x = capa(neuronas[paso], neuronas[paso+1], funciones_activacion[paso])
        red_neuronal.append(x)
    print(red_neuronal)

    X= np.round(np.random.randn(20, 2), 3)
    z= X

    Z = z + red_neuronal[0].b