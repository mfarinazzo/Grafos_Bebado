import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def gerar_grafo_aleatorio(num_vertices, num_arestas_extra=0):
    grafo = {i: set() for i in range(num_vertices)}
    # Garante pelo menos uma aresta de saída por vértice
    for i in range(num_vertices):
        destino = random.choice([v for v in range(num_vertices) if v != i])
        grafo[i].add(destino)
    # Adiciona arestas extras aleatórias
    for _ in range(num_arestas_extra):
        origem = random.randint(0, num_vertices - 1)
        destino = random.randint(0, num_vertices - 1)
        if origem != destino:
            grafo[origem].add(destino)
    return grafo

def passeio_bebado(grafo, max_passos):
    atual = random.choice(list(grafo.keys()))
    caminho = [atual]
    for _ in range(max_passos):
        if not grafo[atual]:
            break  # Sem saída
        atual = random.choice(list(grafo[atual]))
        caminho.append(atual)
    return caminho

def animar_passeio(grafo, caminho):
    G = nx.DiGraph()
    for v, adjs in grafo.items():
        for u in adjs:
            G.add_edge(v, u)
    pos = nx.spring_layout(G, seed=42)
    fig, ax = plt.subplots()
    
    def update(frame):
        ax.clear()
        nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightblue', arrows=True)
        ax.scatter(*pos[caminho[frame]], s=300, c='red', zorder=3)
        ax.set_title(f'Passo {frame}: Nó {caminho[frame]}')
        ax.axis('off')

    ani = FuncAnimation(fig, update, frames=len(caminho), interval=800, repeat=False)
    plt.show()

if __name__ == "__main__":
    print("Quantos vértices o grafo deve ter?")
    num_vertices = int(input())
    if num_vertices < 5:
        print("Número de vértices deve ser maior que 5.")
        exit(1)
    if num_vertices > 20:
        print("Número de vértices deve ser menor que 20.")
        exit(1)

    print("Quantos vértices extras o grafo deve ter?")
    num_arestas_extra = int(input())
    if num_arestas_extra < 6:
        print("Número de vértices extras deve ser maior que 5.")
        exit(1)
    if num_arestas_extra > 20:
        print("Número de vértices extras deve ser menor que 20.")
        exit(1)

    print("Quantos passos o bêbado deve dar?")
    max_passos = int(input())
    if max_passos < 1:
        print("Número de passos deve ser maior que 0.")
        exit(1)
    if max_passos > 100:
        print("Número de passos deve ser menor que 100.")
        exit(1)

    grafo = gerar_grafo_aleatorio(num_vertices, num_arestas_extra)
    caminho = passeio_bebado(grafo, max_passos)
    print("Grafo:")
    for v, adj in grafo.items():
        print(f"{v} -> {list(adj)}")
    print("\nCaminho do bêbado:")
    print(caminho)
    animar_passeio(grafo, caminho)