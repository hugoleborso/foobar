from collections import deque
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.figure import Figure
import numpy as np
import math

a=[]
a.append([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]])
#11567

a.append([[True, False, True], [False, True, False], [True, False, True]])
# 4

a.append([[True, True], [True, False]])
# 4

a.append([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]])
# 254

a.append([[False, False, False, False, False, True, True, True], [False, False, False, False, False, False, True, False], [False, False, False, False, False, False, True, False], [False, False, False, False, False, False, True, False], [False, False, False, False, False, True, True, True]])
# not 254

def graphVisualiser(truthList,ax):

    ax.patch.set_facecolor('black')
    ax.set_aspect('equal', 'box')
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.grid(which='major', color='#CCCCCC', linestyle='--')

    rect = plt.Rectangle([-0.1, -0.1], len(truthList[0])+0.2, len(truthList)+0.2,
                                facecolor='white', edgecolor='black')
    ax.add_patch(rect)
    for y,row in enumerate(truthList):
        for x,cell in enumerate(row):
            color = 'pink' if cell else 'white'
            size =  0.9
            rect = plt.Rectangle([x+0.05, y+0.05], size, size,
                                facecolor=color, edgecolor=color)
            ax.add_patch(rect)

    ax.autoscale_view()
    ax.invert_yaxis()

def graphVisualiser2(truthList,res):
    ax=plt.gca()
    ax.set_title('Evolution - green new, orange old')
    ax.patch.set_facecolor('black')
    ax.set_aspect('equal', 'box')
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.grid(which='major', color='#CCCCCC', linestyle='--')

    rect = plt.Rectangle([-0.1, -0.1], len(truthList[0])+0.2, len(truthList)+0.2,
                                facecolor='white', edgecolor='black')
    ax.add_patch(rect)
    for y,row in enumerate(truthList):
        for x,cell in enumerate(row):
            if cell:
                size =  0.9
                rect = plt.Rectangle([x+0.05, y+0.05], size, size,
                                    facecolor='orange', edgecolor='orange',alpha=0.5)
                ax.add_patch(rect)
    for y,row in enumerate(res):
        for x,cell in enumerate(row):
            if cell:
                size =  0.9
                rect = plt.Rectangle([x+0.05, y+0.05], size, size,
                                    facecolor='green', edgecolor='green',alpha=0.3)
                ax.add_patch(rect)
    rect = plt.Rectangle([0, 0], len(res[0]), len(res),
                                facecolor='none', edgecolor='black',zorder=10)
    ax.add_patch(rect)
    ax.autoscale_view()
    ax.invert_yaxis()
    plt.show()


def nextGraph(truthList):
    r=len(truthList)
    c=len(truthList[0])
    A=np.array(truthList,dtype=float)
    B=np.eye(c,c-1)+np.vstack([np.zeros((1,c-1)), np.eye(c-1,c-1)])
    C=np.transpose(np.eye(r,r-1)+np.vstack([np.zeros((1,r-1)), np.eye(r-1,r-1)]))
    
    sum=np.dot(C,np.dot(A,B))
    #sum=np.transpose(np.dot(np.transpose(np.dot(A,B)),C))
    res=sum==1
    return(res)

def graphAnalysis(truthList):
    onlyOne=[]
    notOne=[]
    for y,row in enumerate(truthList):
        for x,cell in enumerate(row):
            if cell:
                onlyOne.append([(x,y),(x+1,y),(x,y+1),(x+1,y+1)])
            else:
                notOne.append([(x,y),(x+1,y),(x,y+1),(x+1,y+1)])
    print('only one cell : ',onlyOne)
    print('\nnot one cell :',notOne)

def notOnePossibilities(nbOfTrue,nbOfFalse):
    s=0
    if nbOfTrue==1 and nbOfFalse==3:
        print("WEUUU WEUUU")
    elif nbOfTrue==0:
        n=4-nbOfFalse
        for k in range(n):
            if nbOfTrue+k!=1:
                s+=math.comb(n, k)
    return(s)

def onlyOnePossibilities(nbOfTrue,nbOfFalse):
    if not nbOfTrue:
        return(4-nbOfFalse)
    elif nbOfTrue!=1:
        print("WEUUU WEUUU")
    return(1)



def recursivePossibilities(x,y,inputGrid,currentGrid):
    sumPoss=0
    if y==0:
        if x==0:
            for cellValue in [1,0]:
                currentGrid[y][x]=cellValue
                
                if squareIsPossibile(x,y,inputGrid,currentGrid):
                    print("\nOKKKK")
                    print(np.array(currentGrid))
                    print('\n')
                    sumPoss+=1
            return(sumPoss)
        else:
            new_x=x-1
            new_y=len(inputGrid)
    else:
        new_x=x
        new_y=y-1
    #print(x,y,'new',new_x,new_y)

    for cellValue in [1,0]:  
        currentGrid[y][x]=cellValue
        #print(np.array(currentGrid))
        if squareIsPossibile(x,y,inputGrid,currentGrid):
            sumPoss+=recursivePossibilities(new_x,new_y,inputGrid,currentGrid)
    return(sumPoss)


def squareIsPossibile(x,y,inputGrid,currentGrid):
    if x==len(currentGrid[0])-1 or y==len(currentGrid)-1:
        #print(str(x)+','+str(y),'--> go - bord')
        return(True)
    else:
        squareSum=currentGrid[y][x]+currentGrid[y+1][x]+currentGrid[y][x+1]+currentGrid[y+1][x+1]
        if (inputGrid[y][x] and squareSum==1) or ((not inputGrid[y][x]) and squareSum!=1):
            #print(str(x)+','+str(y),'--> go')
            return(True)
        else:
            #print(str(x)+','+str(y),'--> stop')
            return(False)




def solutionOld(inputGrid):
    currentGrid=[[0 for i in range(len(inputGrid[0])+1)] for j in range(len(inputGrid)+1)]
    inputGridInt=[[1 if value else 0 for value in inputGridRow] for inputGridRow in inputGrid ]
    print(20*'\n')
    print("___ START ___")
    print(np.array(inputGridInt))
    print('\n\n')
    return(recursivePossibilities(len(inputGrid[0]),len(inputGrid),inputGridInt,currentGrid))





def solution(inputGrid):
    currentGrid=[[0 for i in range(len(inputGrid[0])+1)] for j in range(len(inputGrid)+1)]
    inputGrid=[[1 if value else 0 for value in inputGridRow] for inputGridRow in inputGrid ]
    visitedGraphs=[]
    possibleGraphs=deque(currentGrid)
    while possibleGraphs:
        for x in range(len(inputGrid[0]+1),-1,-1):
            for y in range(len(inputGrid+1),-1,-1):
                for cellValue in [0,1]:
                    pass#trouver ce qu'il faut faire pour garder la solution en mem


def test(index):
    res=nextGraph(a[index])
    fig, axs = plt.subplots(2)
    graphVisualiser(a[index],axs[0])
    graphVisualiser(res,axs[1])
    plt.show()

def test1(index):
    fig, axs = plt.subplots(1)
    graphVisualiser(a[index],axs)
    plt.show()

def test2(index):
    res=nextGraph(a[index])
    graphVisualiser2(a[index],res)

# test(1)
# test1(1)
print(solutionOld(a[1]))