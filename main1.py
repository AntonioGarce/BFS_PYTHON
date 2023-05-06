import heapq
from collections import defaultdict
import re   
import sys  

inf = 0x3f3f3f3f
dist = dict()
graph = defaultdict(list)

def makeGraph(edges):
    for edge in edges:
        u, v, color, method = edge.split(' ')
        graph[u].append((v, color, method))
        graph[v].append((u, color, method))
        dist[u] = dist[v] = inf
        
def findShortestPath(st, ed):
    dist[st] = 0 
    qf = qb = 0
    q = []
    pre = dict()
    
    for v, color, method in graph[st]:
        q.append((st, v, color, method))
        qb = qb + 1
        dist[v] = 1
        pre[v] = st
        
    while qf < qb:
        u, v, color, method = q[qf]
        qf = qf + 1
        for x, _color, _method in graph[v]:
            if color != _color and _method != method:continue
            if(dist[x] < dist[v] + 1) or (dist[x] == dist[v] and pre[x] < v) : continue
            dist[x] = dist[v] + 1
            q.append((v, x, _color, _method))
            qb = qb + 1
            pre[x] = v 
    
    if(dist[ed] > inf - 10): return "NO PATH"
    
    path = []
    t = ed
    while t != st:
        path.append(t)
        t = pre[t]
    
    path.append(st)
    path.reverse()
    return path   


def readFile(fileName):
    lines = []
    with open(fileName) as data:
        for line in data: lines.append(line.strip('\n'))
    firstLine = re.split(' ', lines[0])
    return firstLine[2], firstLine[3], lines[1:]
if len(sys.argv) != 2:
    print("You should type the command correctly.\n python3 main.py inputfile")
st, ed, edges = readFile(sys.argv[1])
makeGraph(edges)
print(findShortestPath(st, ed))

