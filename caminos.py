import numpy as np
from time import time


# decorador para obtener tiempo [ms] que tarda una
# función en terminar de ejecutarse
def decorator(func):
    def get_time(self, *args):
        t0 = time()
        func(self, *args)
        tf = time()
        return (tf - t0) * 1000
    return get_time


# La clase Caminos recibe como argumento las dimensiones de la PCB
# donde N es el número de columnas y M el de filas
class Caminos:
    def __init__(self, n: int, m: int):
        self.pcb = np.zeros((m, n))  # matriz de M x N
        self.n, self.m = n, m  # dimensiones de la PCB
        self.A, self.B = [0, 0], [n - 1, m - 1]  # puntos A y B
        self.roads = 0

    # para encontrar los caminos, podemos aprovechar la recursividad
    # permitiendo hacer recorridos distintos dependiendo del
    # sentido del movimiento
    def recursive(self):
        self.roads = 0  # partimos de cero recorridos encontrados

        # determina el camino desde un punto point considerando que
        # ya ha pasado todos los puntos en visited para no devolverse
        # visited se va copiando para ir buscando por rama
        # y que se permita encontrar más de un recorrido
        def road(point, visited):
            i, j = point
            visited.append([i, j])  # visitamos [i, j]
            if [i, j] == self.B:  # llegamos a B
                self.roads += 1  # aumentamos el contador
            else:
                # vamos a la derecha
                if [i + 1, j] not in visited and i + 1 < self.n:
                    road([i + 1, j], visited.copy())
                # # vamos a la izquierda
                # if [i - 1, j] not in visited and i - 1 >= 0:
                #     road([i - 1, j], visited.copy())
                # vamos hacia abajo
                if [i, j + 1] not in visited and j + 1 < self.m:
                    road([i, j + 1], visited.copy())
                # # vamos hacia arriba
                # if [i, j - 1] not in visited and j - 1 >= 0:
                #     road([i, j - 1], visited.copy())

        road(self.A, [])  # partimos de A y no hemos pasado por ningún punto
        return self.roads

    # algoritmo iterativo con idea similar al anterior, donde se van
    # registrando los estados actuales. Termina cuando se terminan los estados
    def iterative(self):
        self.roads = 0  # partimos de cero recorridos encontrados
        # states indica el estado [point = [i, j], visitados = [[i, j], ... ]]
        states = [[self.A, [self.A]]]  # partimos de A y solo hemos pasado por A
        while len(states) > 0:
            [i, j], visited = states.pop()  # vemos el último estado
            if [i, j] == self.B:  # llegamos a B
                self.roads += 1  # aumentamos el contador
            # vamos a la derecha
            if [i + 1, j] not in visited and i + 1 < self.n:
                states.append([[i + 1, j], visited + [[i + 1, j]]])
            # # vamos a la izquierda
            # if [i - 1, j] not in visited and i - 1 >= 0:
            #     states.append([[i - 1, j], visited + [[i - 1, j]]])
            # vamos hacia abajo
            if [i, j + 1] not in visited and j + 1 < self.m:
                states.append([[i, j + 1], visited + [[i, j + 1]]])
            # # vamos hacia arriba
            # if [i, j - 1] not in visited and j - 1 >= 0:
            #     states.append([[i, j - 1], visited + [[i, j - 1]]])
        return self.roads

    # retorna el número de caminos que tiene la clase a través
    # del algoritmo iterativo en caso de True. En cambio,
    # si fuera False, utiliza el algoritmo recursivo
    @ decorator
    def num_roads(self, iterative: bool):
        return self.iterative() if iterative is True else self.recursive()


if __name__ == '__main__':
    # verificamos casos simples
    assert Caminos(3, 3).recursive() == Caminos(3, 3).iterative() == 6
    assert Caminos(2, 2).recursive() == Caminos(2, 2).iterative() == 2
    # verificamos que es conmutativo
    assert Caminos(3, 2).iterative() == Caminos(2, 3).recursive() == 3
    assert Caminos(2, 3).iterative() == Caminos(3, 2).recursive() == 3
    # verificamos un caso complejo
    assert Caminos(5, 5).iterative() == Caminos(5, 5).recursive()
