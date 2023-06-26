grafo = {'oradea': ['zerind', 'sibiu'],
             'zerind': ['oradea', 'arad'],
             'arad': ['zerind', 'timisoara', 'sibiu'],
             'timisoara': ['arad', 'lugoj'],
             'lugoj': ['timisoara', 'mehadia'],
             'mehadia': ['lugoj', 'dobreta'],
             'dobreta': ['mehadia', 'craiova'],
             'craiova': ['dobreta', 'rimnicu vilcea', 'pitesti'],
             'sibiu': ['oradea', 'arad', 'fagaras', 'rimnicu vilcea'],
             'fagaras': ['sibiu', 'bucharest'],
             'rimnicu vilcea': ['sibiu', 'pitesti', 'craiova'],
             'pitesti': ['rimnicu vilcea', 'craiova', 'bucharest'],
             'bucharest': ['pitesti', 'fagaras', 'giurgiu', 'urziceni'],
             'giurgiu': ['bucharest'],
             'urziceni': ['bucharest', 'vaslui', 'hirsova'],
             'hirsova': ['urziceni', 'eforie'],
             'eforie': ['hirsova'],
             'vaslui': ['urziceni', 'lasi'],
             'lasi': ['vaslui', 'neamt'],
             'neamt': ['lasi']
             }

def busca_em_profundidade(grafo, vertice_inicial, vertice_final):
    visitados = set()  # Conjunto para rastrear os vértices visitados
    pilha = [vertice_inicial]  # Pilha para armazenar os vértices a serem visitados

    if vertice_inicial == vertice_final:
        print('ja esta na cidade')

    else:
       while pilha:
          vertice = pilha.pop()  # Remove o último vértice adicionado na pilha

          if vertice == vertice_final:
            print(vertice)
            break

          if vertice not in visitados:
              visitados.add(vertice)
              print(vertice)  # Exibe o vértice visitado

              # Adiciona os vizinhos do vértice não visitados à pilha
              for vizinho in grafo[vertice]:
                  if vizinho not in visitados:
                      pilha.append(vizinho)

busca_em_profundidade(grafo, 'sibiu', 'lasi')
