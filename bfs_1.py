from collections import defaultdict
import re
import sys 

inf = 0x3f3f3f3f


queue = []

def readFile(fileName):
    lines = []
    with open(fileName) as data:
        for line in data: lines.append(line.strip('\n'))
    firstLine = re.split(' ', lines[0])
    return firstLine[2], firstLine[3], firstLine[1], lines[1:]


st, ed, num_links, links = readFile(sys.argv[1])
graph = [[] for i in range(int(num_links)*2+1)]
# print(graph)

def makeGraph(links, st):
  nodes = []
  nodes.append(['0',st,'0','0'])
  num_node = 1

  for link in links:
    u, v, color, method = link.split(' ')
    nodes.append([u,v,color,method])
    nodes.append([v,u,color,method])
    num_node += 2

  node_inds = [i for i in range(len(nodes))]

  for node_i_f in node_inds:
    for node_i_e in node_inds:
      if nodes[node_i_e][0] == nodes[node_i_f][1]:
        if nodes[node_i_e][1] == nodes[node_i_f][0]:
          continue
        elif nodes[node_i_f][0] == '0' or nodes[node_i_e][2] == nodes[node_i_f][2] or nodes[node_i_e][3] == nodes[node_i_f][3]:
          graph[node_i_f].append(node_i_e)
         
  return nodes , node_inds, graph

nodes, node_inds, graph = makeGraph(links, st)
# print(graph)
def bfs(visited, graph, node, ed): #function for BFS
  parent = dict()
  parent = defaultdict(list)
  visited.append(node)
  queue = []
  queue.append(node)
  strPath = "NO PATH"

  parent[0] = [-1]

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    
    neighbours = graph[m]

    if not neighbours:
        continue

    neighbour_vs = [nodes[i][1] for i in neighbours]

    neighbour_vs, neighbours = zip(*sorted(zip(neighbour_vs, neighbours)))
    
    for neighbour in neighbours:
      # print(neighbour)
      if neighbour not in visited:
        parent[neighbour].append(m)
        visited.append(neighbour)
        queue.append(neighbour)

        if nodes[neighbour][1] == ed:
          queue = []
          strPath = ed
          par = parent[neighbour].pop()
          
          while(par != -1):
            strPath = nodes[par][1] +  " " + strPath
            par = parent[par].pop()

          break

  return strPath

for i in range(5000):
  visited = []
  strBestPath = bfs(visited, graph, 0, ed)
  print(strBestPath)
