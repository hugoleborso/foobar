a=[]
a.append(([1250,1250], [1000,1000], [500,400], 10000))
i=0
import math

def solution(dimensions, your_position, trainer_position, distance):
    possibleHeight=int(distance//dimensions[1])+1
    possibleWidth=int(distance//dimensions[0])+1
    shoots={}
    selfCoordinates=[[],[]]
    targetCoordinates=[[],[]]

    for j in range(-possibleWidth,possibleWidth+1):
        if not j%2:
            targetCoordinates[0].append(j*dimensions[0]+trainer_position[0])
            selfCoordinates[0].append(j*dimensions[0]+your_position[0])
        else:
            targetCoordinates[0].append((j+1)*dimensions[0]-trainer_position[0])
            selfCoordinates[0].append((j+1)*dimensions[0]-your_position[0])
    
    for i in range(-possibleHeight,possibleHeight+1):
        if not i%2:
            targetCoordinates[1].append(i*dimensions[1]+trainer_position[1])
            selfCoordinates[1].append(i*dimensions[1]+your_position[1])
        else:
            targetCoordinates[1].append((i+1)*dimensions[1]-trainer_position[1])
            selfCoordinates[1].append((i+1)*dimensions[1]-your_position[1])
    countGood=0
    goodShoots={}
    for i,coordinates in enumerate([selfCoordinates,targetCoordinates]):
        for x in coordinates[0]:
            for y in coordinates[1]:
                shoot=[x-your_position[0],y-your_position[1]]
                l=math.sqrt(shoot[0]**2+shoot[1]**2)
                if l<=distance and shoot!=[0,0]:
                    angle=math.atan2((your_position[1]-y), (your_position[0]-x))
                    if (angle in shoots and shoots[angle] > l ) or angle not in shoots:
                        shoots[angle]=l
                        if i:
                            countGood+=i
                            goodShoots[angle]=l
    return(len(goodShoots))

print(solution(a[i][0],a[i][1],a[i][2],a[i][3]))
