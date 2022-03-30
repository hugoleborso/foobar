from datetime import datetime
from l4e2_test_visualisation import visu

a=[([3,2], [1,1], [2,1], 4)]
b=[7]

a.append(([300,275], [150,150], [185,100], 500))
b.append(9)

a.append(([300,275], [150,150], [185,100], 35))
b.append(0)

a.append(([10,10], [4,4], [3,3], 5000))
b.append(739323)

a.append(([2,5], [1,2], [1,4], 11))
b.append(27)

a.append(([23,10], [6,4], [3,2], 23))
b.append(8)


a.append(([1250,1250], [1000,1000], [500,400], 10000))
b.append(196)

i=4
import math
import numpy as np

def checkCodir(a,b):
    u1=np.array(a)/np.linalg.norm(np.array(a))
    u2=np.array(b)/np.linalg.norm(np.array(b))
    return(np.dot(u1,u2)==1.0)

def length(shoot):
    return(math.sqrt(shoot[0]**2+shoot[1]**2))

def solution(dimensions, your_position, trainer_position, distance):
    possibleHeight=int(distance//dimensions[1])+1
    possibleWidth=int(distance//dimensions[0])+1
    targetShoots=[]
    selfShoots=[]
    
    for i in range(-possibleHeight,possibleHeight+1):
        if not i%2:
            targety=i*dimensions[1]+trainer_position[1]
            selfy=i*dimensions[1]+your_position[1]
        else:
            targety=(i+1)*dimensions[1]-trainer_position[1]
            selfy=(i+1)*dimensions[1]-your_position[1]
        
        for j in range(-possibleWidth,possibleWidth+1):
            if not j%2:
                targetx=j*dimensions[0]+trainer_position[0]
                selfx=j*dimensions[0]+your_position[0]
            else:
                targetx=(j+1)*dimensions[0]-trainer_position[0]
                selfx=(j+1)*dimensions[0]-your_position[0]

            targetshoot=[targetx-your_position[0],targety-your_position[1]]
            selfshoot=[selfx-your_position[0],selfy-your_position[1]]
            
            if length(selfshoot)<=distance and selfshoot!=[0,0]:
                selfShoots.append(selfshoot)
            
            if length(targetshoot)<=distance:
                codirFound=0
                for otherShoot in targetShoots:
                    if checkCodir(targetshoot,otherShoot):
                        codirFound=1
                        break
                if not codirFound:
                    obstructed=0
                    for selfshoot in selfShoots:
                        if checkCodir(targetshoot,selfshoot):
                            if length(targetshoot)>length(selfshoot):
                                obstructed=1
                                break
                    if not obstructed:
                        targetShoots.append(targetshoot)
    visu(your_position,distance,targetShoots,targetShoots,selfShoots,dimensions)
    return(len(targetShoots))

print(solution(a[i][0],a[i][1],a[i][2],a[i][3]))

def testSpeed(length=1000):
    res=[0,0]
    now=datetime.now()
    for j in range(length):
        i=j%2
        solution(a[i][0],a[i][1],a[i][2],a[i][3])
    then=datetime.now()
    res[0]+=(then-now).total_seconds()

    now=datetime.now()
    for j in range(length):
        i=j%2
        solutionOld(a[i][0],a[i][1],a[i][2],a[i][3])
    then=datetime.now()
    res[1]+=(then-now).total_seconds()
    print('new : ',res[0]/length,'s')
    print('old : ',res[1]/length,'s')

#testSpeed()

#region old funcs
def solutionOld(dimensions, your_position, trainer_position, distance):
    possibleHeight=int(math.ceil(dimensions[1]/distance)+3)
    possibleWidth=int(math.ceil(dimensions[0]/distance)+3)
    targetShoots=[]
    selfShoots=[]
    
    for i in range(-possibleHeight,possibleHeight+1):
        if not i%2:
            targety=i*dimensions[1]+trainer_position[1]
            selfy=i*dimensions[1]+your_position[1]
        else:
            targety=(i+1)*dimensions[1]-trainer_position[1]
            selfy=(i+1)*dimensions[1]-your_position[1]
        
        for j in range(-possibleWidth,possibleWidth+1):
            if not j%2:
                targetx=j*dimensions[0]+trainer_position[0]
                selfx=j*dimensions[0]+your_position[0]
            else:
                targetx=(j+1)*dimensions[0]-trainer_position[0]
                selfx=(j+1)*dimensions[0]-your_position[0]

            targetshoot=[targetx-your_position[0],targety-your_position[1]]
            selfshoot=[selfx-your_position[0],selfy-your_position[1]]
            if length(targetshoot)<=distance:
                targetShoots.append(targetshoot)
            if length(selfshoot)<=distance and selfshoot!=[0,0]:
                selfShoots.append(selfshoot)
    
    goodShoots=[]
    n=len(targetShoots)

    for i,shoot in enumerate(targetShoots):
        codirFound=0
        for j in range(i+1,n):
            if checkCodir(shoot,targetShoots[j]):
                codirFound+=1
        if not codirFound:
            obstructed=0
            for selfshoot in selfShoots:
                if checkCodir(shoot,selfshoot):
                    if length(shoot)>length(selfshoot):
                        obstructed+=1
            if not obstructed:
                goodShoots.append(targetShoots[i])
    return(len(goodShoots))

def distanceCalc(pos_a,pos_b):
    return(math.sqrt((pos_a[0]-pos_b[0])**2+(pos_a[1]-pos_b[1])**2))

class Node():
    def __init__(self,mirror_trainer_position,lastRebound,children=None):
        self.mirror_trainer_position=mirror_trainer_position
        self.lastRebound=lastRebound
        self.children=children
    
    def appendChild(self,child):
        if self.children is None:
            self.children=[child]
        else:
            self.children.append(child)
    
    def __str__(self):
        if self.children is not None:
            return('The trainer is '+str(self.mirror_trainer_position)+' away, this was a '+str(self.lastRebound)+' rebound and there are '+str(len(self.children))+' children.')
        else:
            return('The trainer is '+str(self.mirror_trainer_position)+' away, this was a '+str(self.lastRebound)+' rebound and there are no children.')

def solutionOld(dimensions, your_position, trainer_position, distance):
    noRebounddistance=distanceCalc(your_position,trainer_position)
    if noRebounddistance>distance:
        return(0)
    else:
        return(graphBuilder(Node(trainer_position,'0'), dimensions, your_position, distance)+1)
        
def graphBuilder(node,dimensions, your_position, distance):
    reverse={'N':'S','S':'N','E':'W','W':'E'}
    print(node)
    childrenCount=0
    for direction in ['N','S','E','W']:
        
        if node.lastRebound!=reverse[direction]:
            new_mirror_trainer_position=addRebound(dimensions,node.mirror_trainer_position,direction)
            
            if distanceCalc(your_position,new_mirror_trainer_position)<=distance:
                new_child=Node(new_mirror_trainer_position,direction)
                node.appendChild(new_child)
                childrenCount+=graphBuilder(new_child,dimensions, your_position, distance)
    
    return(childrenCount)
            
def addRebound(dimensions, mirror_trainer_position,direction):
    newPosition=mirror_trainer_position
    
    if direction=='N':
        newPosition[1]+=2*(dimensions[1]-mirror_trainer_position[1]%dimensions[1])
    if direction=='S':
        newPosition[1]-=2*(mirror_trainer_position[1]%dimensions[1])
    if direction=='E':
        newPosition[0]+=2*(dimensions[0]-mirror_trainer_position[0]%dimensions[0])
    if direction=='W':
        newPosition[0]-=2*(mirror_trainer_position[0]%dimensions[0])
    
    return(newPosition)

def test(dimensions, your_position, trainer_position, distance):
    start=Node(trainer_position,'0')
    print('start : ',start)
    for direction in ['N','S','E','W']:
        if start.lastRebound!=direction:
            new_mirror_trainer_position=addRebound(dimensions,start.mirror_trainer_position,direction)
            
            if distanceCalc(your_position,new_mirror_trainer_position)<=distance:
                new_child=Node(new_mirror_trainer_position,direction)
                start.appendChild(new_child)
                print(new_child)
                print(new_child.children)
    print(start)

def checkColinear(a,b):
    if (a==b) or (a==[0,0] or b==[0,0]) or (a[0]==0 and b[0]==0) or (a[1]==0 and b[1]==0):
        return(True)
    
    for i in [0,1]:
        if a[i]==0:
            if b[1-i]==0:
                return(False)
            if not i:
                a=a[::-1]
                b=b[::-1]
        if b[i]==0:
            if a[1-i]==0:
                return(False)
            if not i:
                a=a[::-1]
                b=b[::-1]

    return(abs(a[1]/a[0]-b[1]/b[0])<1e-12)
#endregion
