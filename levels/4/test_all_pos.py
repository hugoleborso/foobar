import numpy as np
from alive_progress import alive_bar
import math

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

    return(len(goodShoots))

def mirror_atlas(node, dimensions, distance):
    node_mirrored=[]
    for i in range(len(node)):
        points=[]
        for j in range(-(distance//dimensions[i])-1, (distance//dimensions[i]+2)):
            points.append(get_mirror(j, node[i], dimensions[i]))
        node_mirrored.append(points)
    return node_mirrored

def get_mirror(mirror, coordinates, dimensions):
    res=coordinates
    mirror_rotation=[2*coordinates, 2*(dimensions-coordinates)]
    if(mirror<0):
        for i in range(mirror, 0):
            res-=mirror_rotation[(i+1)%2]
    else:
        for i in range(mirror, 0, -1):
            res+=mirror_rotation[i%2]
    return res 

def answer(dimensions, your_position, guard_position, distance):
    mirrored = [mirror_atlas(your_position, dimensions,distance),mirror_atlas(guard_position, dimensions, distance)]
    res=set()
    angles_dist={}
    for i in range(0, len(mirrored)):
        for j in mirrored[i][0]:
            for k in mirrored[i][1]:
                beam=math.atan2((your_position[1]-k), (your_position[0]-j))
                l=math.sqrt((your_position[0]-j)**2 + (your_position[1]-k)**2)
                if [j,k] != your_position and distance >= l:
                    if((beam in angles_dist and angles_dist[beam] > l) or beam not in angles_dist):
                        if i == 0:
                            angles_dist[beam] = l
                        else:
                            angles_dist[beam] = l
                            res.add(beam)
    return len(res) 

def compute():
    wrong_answers=[]
    for i in range(1000000):
        dimensions=[np.random.randint(2,1250),np.random.randint(2,1250)]
        your_position = [np.random.randint(1,dimensions[0]),np.random.randint(1,dimensions[1])]
        trainer_position = [np.random.randint(1,dimensions[0]),np.random.randint(1,dimensions[1])]
        distance=np.random.randint(2,200)

        a=[dimensions,your_position,trainer_position,distance]
        if your_position!=trainer_position:
            if solution(a[0],a[1],a[2],a[3])!=answer(a[0],a[1],a[2],a[3]):
                print('WRONG ANSWER !',a)
                wrong_answers.append(a)
        yield
    print(wrong_answers)

# with alive_bar(1000000) as bar:
#     for i in compute():
#         bar()

for x in range(2,26):
    for y in range(2,26):
        print(x,y)
        for t1 in range(1,x):
            for t2 in range(1,y):
                for s1 in range(1,x):
                    for s2 in range(1,y):
                        for distance in range(2,20):
                            a=[[x,y],[s1,s2],[t1,t2],distance]
                            if [s1,s2]!=[t1,t2]:
                                if solution(a[0],a[1],a[2],a[3])!=answer(a[0],a[1],a[2],a[3]):
                                    print('WRONG ANSWER !',a)
