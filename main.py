from collections import defaultdict
import re
import sys 
import queue

inf = 0x3f3f3f3f
dist = dict()
graph = defaultdict(list)
parent = dict()

def makeGraph(edges):
    
    for edge in edges:  
        u, v, color, method = edge.split(' ')
        graph[u].append((v, color, method))
        graph[v].append((u, color, method))
        dist[(u, v)] = dist[(v, u)]= inf
        parent[(u, v)] = parent[(v, u)] = (-1, -1)
    

def findShortestPath(st, ed):
    dist[(st, st)] = 0 
    qf = qb = 0
    q = queue.Queue()
    
    for v, color, method in graph[st]:
        q.put((st, v, color, method))
        
        qb = qb + 1
        dist[(st, v)] = 1
        if v == ed:
            return (st, ed)
        parent[(st, v)] = (-1, -1)
        
    flag = 0
    while q.empty() == False:
        u, v, color, method = q.get()
        
        if v == ed: flag = 1
        for x, _color, _method in graph[v]:
            if x == u: continue 
            if (color != _color and _method != method) : continue
            if dist[(v, x)] < dist[(u, v)] + 1 : continue
            
            if dist[(v, x)] == dist[(u, v)] + 1:
                a, b = parent[(v, x)]

                #a, v, x
                #u, v, x


                if a < u: continue
                
            dist[(v, x)] = dist[(u, v)] + 1
            q.put((v, x, _color, _method))
            qb = qb + 1
            parent[(v, x)] = (u, v) 
            
    if(flag == 0): return "NO PATH"
    
    mn = inf
    t = ed

    for u, color, method in graph[ed]:
        
        if mn > dist[(u, ed)]: 
            mn = dist[(u, ed)]
            t = u
        if mn == dist[(u, ed)]:
            if(u < t):
                mn = dist[(u, ed)]
                t = u
            
            
    path = []
    
    path.append(ed)
    a = t
    b = ed
    while a != -1:
        path.append(a)
        a, b = parent[(a, b)]
        
    path.reverse()


    return path   


def readFile(fileName):
    lines = []
    with open(fileName) as data:
        for line in data: lines.append(line.strip('\n'))
    firstLine = re.split(' ', lines[0])
    return firstLine[2], firstLine[3], lines[1:]


st, ed, edges = readFile(sys.argv[1])
makeGraph(edges)

for i in range(100000):
    resultPath = findShortestPath(st, ed)

    if resultPath == "NO PATH":
        print(resultPath)
    else:
        strOut = ""
        ok = 0
        for nd in resultPath:
            if ok == 0: 
                strOut = strOut + nd
                ok = 1
            else:
                strOut = strOut + " " + nd
                
        print(strOut)

