#region test cases

import numpy as np
a=[[[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]]
b=[1]
c=[[1, 2]]

a.append([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 2, 0, 2, -1], [9, 2, 2, 0, -1], [9, 2, 2, 2, 0]])
b.append(1)
c.append(['jsp'])


a.append([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]])
b.append(3)
c.append([0, 1])

g=list(np.random.randint(-3,15,(7,7)))
h=[]
for i,l in enumerate(g):
    m=[]
    for j,n in enumerate(list(l)):
        if i==j:
            m.append(0)
        elif n==0:
            m.append(1)
        else:
            m.append(n)
    h.append(m)
a.append(h)
b.append(20)
c.append(['jsp'])

a.append([[0, 4, 7, 14, 9, 4, 3], [4, 0, 12, 2, 8, 1, 13], [13, 7, 0, 12, 3, 1, 11], [4, 7, 10, 0, 9, 5, 7], [1, 14, 8, 11, 0, 5, 8], [8, 5, 13, 12, 11, 0, 11], [14, 12, 12, 10, 10, 7, 0]])
b.append(20)
c.append(['jsp'])

#endregion

#region old functions
def BellmanFordOld(graph, src):
    dist = {i:float("inf") for i in graph.keys()}
    dist[src] = 0
    for i in graph.keys():
        for j in graph[i].keys():
            weight = graph[i][j]
            if (dist[i] != float("inf") and dist[i] + weight < dist[j]):
                dist[j] = dist[i] + weight
    for i in graph.keys():
        for j in graph[i].keys():
            weight = graph[i][j]
            if (dist[i] != float("inf") and dist[i] + weight < dist[j]):
                return (True,None)
    return (False,{i:dist[i] for i in dist.keys() if i!=src})


def graphCreatorOld(times,nodes):
    graph={}
    for i,node1 in enumerate(nodes):
        graph[node1]={}
        for j,node2 in enumerate(nodes):
            if j!=i:
                graph[node1][node2]=times[i][j]
    return(graph)

def graphCreator(times,nodes):
    graph={'nodes':nodes,'edges':[]}
    for i,l in enumerate(times):
        for j,w in enumerate(l):
            graph['edges'].append((nodes[i],nodes[j],w))
    return(graph)

#endregion

#region actual code

import itertools




def BellmanFord(graph, src):
    dist = {i:float("Inf") for i in graph['nodes']}
    dist[src] = 0
    for _ in range(len(graph['nodes']) - 1):
        for u, v, w in graph['edges']:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    for u, v, w in graph['edges']:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                return(True,None)
    return(False,dist)

def solution(times, times_limit):
    bunniesNb=len(times)-2
    nodes=["S"]+[str(i) for i in range(bunniesNb)]+["B"]
    graph={'nodes':nodes,'edges':[]}
    for i,l in enumerate(times):
        for j,w in enumerate(l):
            graph['edges'].append((nodes[i],nodes[j],w))
    shortestGraph={}
    for i in graph['nodes']:
        negativeCycle,distances=BellmanFord(graph, i)
        if negativeCycle:
            return([i for i in range(0,bunniesNb)])
        shortestGraph[i]=distances
    for n in list(range(bunniesNb,0,-1)):
        possibleRes=[]
        for nodeList in list(itertools.permutations([str(i) for i in range(bunniesNb)],n)):
            pointList=["S"]+list(nodeList)+["B"]
            src="S"
            time=0
            for dest in pointList[1:]:
                time+=shortestGraph[src][dest]
                src=dest
            if time<=times_limit:
                res=sorted([int(i) for i in pointList[1:-1]])
                possibleRes.append(res)
        if possibleRes:
            return(sorted(possibleRes,key=sum)[0])
    return([])

#endregion

print(solution(a[4],b[4]))

#region test
test=False
if test:
    graph={'nodes':[0,1,2],'edges':[(0,1,8),(0,2,2),(1,2,8),(1,0,1),(2,0,8),(2,1,6)]}
    graph={'S': {'0': 7, '1': 1, '2': 12, '3': 4, '4': 11, 'B': 13}, '0': {'S': 9, '1': 13, '2': 3, '3': 9, '4': 6, 'B': 5}, '1': {'S': 9, '0': 6, '2': 7, '3': 7, '4': 3, 'B': 2}, '2': {'S': 6, '0': 4, '1': 7, '3': 10, '4': 8, 'B': 2}, '3': {'S': 7, '0': 1, '1': 1, '2': 2, '4': 10, 'B': 4}, '4': {'S': 14, '0': 3, '1': 5, '2': 4, '3': 6, 'B': 10}, 'B': {'S': 11, '0': 10, '1': 13, '2': 9, '3': 1, '4': 9}}
    for i in graph['nodes']:
       print(i,BellmanFord(graph,i))
    print(len(list(itertools.permutations([i for i in range(1,5)],4))))
    print(graphCreator(a[1],[1,2,3]))

#endregion


#region debug
debug=False
if debug:
    probableRes=[]
    while len(probableRes)<=1:
        g=list(np.random.randint(-3,15,(7,7)))
        h=[]
        for i,l in enumerate(g):
            m=[]
            for j,n in enumerate(list(l)):
                if i==j:
                    m.append(0)
                elif n==0:
                    m.append(1)
                else:
                    m.append(n)
            h.append(m)
        k=20
        probableRes=solution(h,k)
    print(h,probableRes)

#endregion