from l4e2_test_visualisation import visu2

a=[([3,2], [1,1], [2,1], 4)]
b=[7]

a.append(([300,275], [150,150], [185,100], 500))
b.append(9)


a.append(([10,10], [4,4], [3,3], 5000))
b.append(739323)

a.append(([2,5], [1,2], [1,4], 11))
b.append(27)

a.append(([23,10], [6,4], [3,2], 23))
b.append(8)


a.append(([1250,1250], [1000,1000], [500,400], 10000))
b.append(196)

a.append(([3,2], [1,1], [2,1], 8))
b.append('jsp')

a.append(([8,4], [1,1], [1,2], 50))
b.append('jsp')

a.append(([8,4], [7,3], [1,1], 8))
b.append('jsp')

a.append(([20,20], [2,2], [2,4], 5))
b.append('jsp')

#==wrong answers==
a.append([[11, 14], [6, 8], [5, 1], 93])
a.append([[5, 4], [3, 1], [1, 2], 22])
a.append([[9, 42], [7, 9], [2, 4], 25])



i=12


import math
import numpy as np

def getAngle(a):
    u1=np.array(a)/np.linalg.norm(np.array(a))
    if a[1]>0:
        angle=np.arccos(np.clip(np.dot(u1, np.array([1,0])), -1.0, 1.0))
    else:
        angle=-np.arccos(np.clip(np.dot(u1, np.array([1,0])), -1.0, 1.0))
    return("{:.12f}".format(angle))

def length(shoot):
    return(math.sqrt(shoot[0]**2+shoot[1]**2))

def solution(dimensions, your_position, trainer_position, distance):
    possibleHeight=int(distance//dimensions[1])+1
    possibleWidth=int(distance//dimensions[0])+1
    targetShoots={}
    selfShoots={}
    
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
                angle=getAngle(selfshoot)
                if angle in selfShoots.keys():
                    selfShoots[angle].append(length(selfshoot))
                else:
                    selfShoots[angle]=[length(selfshoot)]

            if length(targetshoot)<=distance:
                angle=getAngle(targetshoot)
                if angle in targetShoots.keys():
                    targetShoots[angle].append(length(targetshoot))
                else:
                    targetShoots[angle]=[length(targetshoot)]
    goodShoots={}
    for angle in targetShoots.keys():
        if angle in selfShoots.keys():
            if min(selfShoots[angle])>=min(targetShoots[angle]):
                goodShoots[angle]=min(targetShoots[angle])
        else:
            goodShoots[angle]=min(targetShoots[angle])

    visu2(your_position,distance,goodShoots,targetShoots,selfShoots,dimensions)
    return(len(goodShoots))

print(solution(a[i][0],a[i][1],a[i][2],a[i][3]))
