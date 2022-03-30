a=[]
a.append([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]])
#11567

a.append([[True, False, True], [False, True, False], [True, False, True]])
# 4

a.append([[True, True], [True, False]])
# 10 ?

a.append([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]])
# 254

a.append([[False, False, False, False, False, True, True, True], [False, False, False, False, False, False, True, False], [False, False, False, False, False, False, True, False], [False, False, False, False, False, False, True, False], [False, False, False, False, False, True, True, True]])
# not 254



def recursivePossibilities(x,y,inputGrid,currentGrid):
    sumPoss=0
    if y==0:
        if x==0:
            for cellValue in [1,0]:
                currentGrid[y][x]=cellValue 
                if squareIsPossibile(x,y,inputGrid,currentGrid):
                    sumPoss+=1
            return(sumPoss)
        else:
            new_x=x-1
            new_y=len(inputGrid)
    else:
        new_x=x
        new_y=y-1

    for cellValue in [1,0]:  
        currentGrid[y][x]=cellValue
        if squareIsPossibile(x,y,inputGrid,currentGrid):
            sumPoss+=recursivePossibilities(new_x,new_y,inputGrid,currentGrid)
    return(sumPoss)


def squareIsPossibile(x,y,inputGrid,currentGrid):
    if x==len(currentGrid[0])-1 or y==len(currentGrid)-1:
        return(True)
    else:
        squareSum=currentGrid[y][x]+currentGrid[y+1][x]+currentGrid[y][x+1]+currentGrid[y+1][x+1]
        if (inputGrid[y][x] and squareSum==1) or ((not inputGrid[y][x]) and squareSum!=1):
            return(True)
        else:
            return(False)


def solution(inputGrid):
    currentGrid=[[0 for i in range(len(inputGrid[0])+1)] for j in range(len(inputGrid)+1)]
    inputGridInt=[[1 if value else 0 for value in inputGridRow] for inputGridRow in inputGrid ]
    return(recursivePossibilities(len(inputGrid[0]),len(inputGrid),inputGridInt,currentGrid))



print(solution(a[0]))