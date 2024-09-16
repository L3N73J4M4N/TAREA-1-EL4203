from caminos import Caminos
import matplotlib.pyplot as plt

# obtención de datos para la gráfica
N0, Nf = 7, 11
dims = range(N0, Nf)
x, it, rec = [], [], []
for d1 in dims:
    for d2 in dims:
        x.append(f'({d1}, {d2})')
        it.append(Caminos(d1, d2).num_roads(True))
        rec.append(Caminos(d1, d2).num_roads(False))

max_time = max(max(rec), max(it)) + 10
# gráfico de ambos algoritmos
plt.figure(figsize=(12, 6))
plt.bar(x, it, color='coral', label='Iteración')
plt.bar(x, rec, color='royalblue', label='Recursión')
plt.ylim([0, max_time])
plt.ylabel('tiempo [ms]')
plt.xlabel('dimensiones de matriz [N x M]')
plt.title('Tiempo que tardan los algoritmos en función de las dimensiones.')
plt.legend()
plt.savefig('grafico_ambos_algoritmos.svg')
plt.show()

# gráfico de algoritmo iterativo
plt.figure(figsize=(12, 6))
plt.bar(x, it, color='coral')
plt.ylabel('tiempo [ms]')
plt.ylim([0, max_time])
plt.xlabel('dimensiones de matriz [N x M]')
plt.title('Tiempo que tarda algoritmo iterativo en función de las dimensiones.')
plt.savefig('grafico_iteracion.svg')
plt.show()

# gráfico de algoritmo recursivo
plt.figure(figsize=(12, 6))
plt.bar(x, rec, color='royalblue')
plt.ylabel('tiempo [ms]')
plt.ylim([0, max_time])
plt.xlabel('dimensiones de matriz [N x M]')
plt.title('Tiempo que tarda algoritmo recursivo en función de las dimensiones.')
plt.savefig('grafico_recursion.svg')
plt.show()

