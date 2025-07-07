# Passeio Aleatório em Grafos Orientados ("Problema do Bêbado")

Este projeto simula o passeio aleatório (random walk), conhecido como "problema do bêbado", em grafos orientados. O objetivo é ilustrar, de forma visual e interativa, como uma partícula (o "bêbado") se move aleatoriamente entre os vértices de um grafo, seguindo as arestas disponíveis.

Autores: Murilo Farinazzo Vieira, Lucas de Souza Silva, Murilo Amorim Bueno Godoy

---

## Descrição do Problema

O "problema do bêbado" consiste em modelar o caminho de um agente que, a cada passo, escolhe aleatoriamente uma das saídas possíveis do vértice atual em um grafo orientado. O projeto gera um grafo aleatório, simula o passeio do bêbado por até 20 passos e exibe uma animação do trajeto percorrido.

---

## Explicação do Código

O código principal está no arquivo `bebado.py`. Abaixo, segue uma explicação detalhada de cada parte:

### Importação de Bibliotecas

```python
import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
```
- `random`: Usada para escolhas aleatórias.
- `networkx`: Biblioteca para manipulação de grafos.
- `matplotlib.pyplot` e `FuncAnimation`: Para visualização e animação do passeio.

---

### Função: gerar_grafo_aleatorio

```python
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
```
- Cria um dicionário onde cada vértice aponta para um conjunto de vizinhos.
- Garante que cada vértice tenha pelo menos uma saída.
- Adiciona arestas extras aleatórias, evitando laços (origem ≠ destino).

---

### Função: passeio_bebado

```python
def passeio_bebado(grafo, max_passos):
    atual = random.choice(list(grafo.keys()))
    caminho = [atual]
    for _ in range(max_passos):
        if not grafo[atual]:
            break  # Sem saída
        atual = random.choice(list(grafo[atual]))
        caminho.append(atual)
    return caminho
```
- Escolhe um vértice inicial aleatório.
- A cada passo, escolhe aleatoriamente uma aresta de saída.
- Para se não houver saída ou se atingir o número máximo de passos.

---

### Função: animar_passeio

```python
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
```
- Constrói o grafo orientado com NetworkX.
- Define posições dos nós.
- Cria uma animação mostrando o caminho do bêbado, destacando o nó atual em vermelho.

---

### Execução Principal

```python
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
```
- Solicita ao usuário o número de vértices, arestas extras e passos.
- Valida os valores inseridos.
- Gera o grafo, executa o passeio e exibe o resultado e a animação.

---

## Como Executar

1. **Pré-requisitos:**  
   Instale as bibliotecas necessárias:
   ```sh
   pip install networkx matplotlib
   ```

2. **Execução:**  
   No terminal, navegue até a pasta do projeto e execute:
   ```sh
   python bebado.py
   ```
   Siga as instruções no terminal para informar os parâmetros do grafo e do passeio.

---

## Observações

- O grafo é sempre orientado e aleatório.
- O passeio pode terminar antes do número máximo de passos se o bêbado chegar a um vértice sem saída.
- O caminho percorrido é mostrado no terminal e animado em uma janela gráfica.

---

**Projeto desenvolvido para fins acadêmicos.**
