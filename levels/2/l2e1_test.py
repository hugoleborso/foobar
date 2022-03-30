a2=(0, 1)
b2=3

a1=(19, 36)
b1=1

def solution(src, dest):
    if dest==src:
        return(0)
        
    #building the graph
    edges={}
    for i in range(8):
        for j in range(8):
            n=8*i+j
            edges[n]=[]
            edges[n]+=[8*(i+k)+(j+l) for k in [-2,2] for l in [-1,1] if i+k in list(range(8)) and (j+l) in list(range(8))]
            edges[n]+=[8*(i+l)+(j+k) for k in [-2,2] for l in [-1,1] if i+l in list(range(8)) and (j+k) in list(range(8))]

    #shortest path algo
    explored = []
    
    queue=[[src]]
    
    while queue:
        path=queue.pop(0)
        currentNode=path[-1]
        
        if currentNode not in explored:
            neighbours=edges[currentNode]
             
            for neighbour in neighbours:
                queue.append(path+[neighbour])
                
                if neighbour==dest:
                    return(len(path))
                    
            explored.append(currentNode)
    
    
    
print(solution(a1[0],a1[1]))

