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
def recursivo(grafo, atual, chegada, limite):
  print(atual)
  if atual == chegada:
    return True
  elif limite == 0:
    return False
  else:
    for vizinho in grafo[atual]:
      if recursivo(grafo, vizinho, chegada, limite - 1):
        return True
    return False
def limitada(grafo, start, chegada, limite):
  return recursivo(grafo, start, chegada, limite)

caminho = limitada(grafo, 'oradea', 'lasi', 6)

if caminho:
  print('cidade encontrada')

else:
  print('cidade nao encontrada no limite especifico')
