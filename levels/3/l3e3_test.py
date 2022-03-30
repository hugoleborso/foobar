a=[[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
b=7
c=[[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
d=11
import math

def printMap(map):
    changeCar={0:'.',1:'X'}
    firstline=' '
    firstline+='-'*len(map[0])+' '
    print(firstline)
    for line in map:
        printline='|'+''.join([changeCar[x] for x in line])+'|'
        print(printline)
    print(firstline)

def createGraph(map,h,w):
    graph={}
    for i in range(h):
        for j in range(w):
            if not map[i][j]:
                graph[(i,j)]=[n for n in neighbors(i,j,map,h,w) if not map[n[0]][n[1]]]
    return(graph)
    
def neighbors(i,j,map,h,w):
    return([(i+k,j) for k in [-1,1] if i+k>=0 and i+k<h]+[(i,j+l) for l in [-1,1] if j+l>=0 and j+l<w])
    
def possibleRemovesList(map,graph,h,w):
    possibleRemoves=[]
    for i in range(h):
        for j in range(w):
            if map[i][j]:
                if len([n for n in neighbors(i,j,map,h,w) if not map[n[0]][n[1]]])>1:
                   possibleRemoves.append((i,j)) 
    return(possibleRemoves)


def shortestPath(graph,h,w):
    explored = []
    queue=[[(0,0)]]
    while queue:
        path=queue.pop(0)
        currentNode=path[-1]
        
        if currentNode not in explored:
            neighbours=graph[currentNode]
            for neighbour in neighbours:
                queue.append(path+[neighbour])
                
                if neighbour==(h-1,w-1):
                    return(len(path)+1)
            explored.append(currentNode)
    return(math.inf)
        
def solution(map):
    h=len(map)
    w=len(map[0])
    #printMap(map)
    graph=(createGraph(map,h,w))
    #print(graph)
    possibleGraphs=[graph]
    for p in possibleRemovesList(map,graph,h,w):
        map[p[0]][p[1]]=0
        possibleGraphs.append(createGraph(map,h,w))
        map[p[0]][p[1]]=1
    return(min([shortestPath(graph,h,w) for graph in possibleGraphs]))


print(solution(a))
