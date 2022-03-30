import matplotlib.pyplot as plt
import math
from matplotlib.ticker import MultipleLocator

def visu(your_position,distance,goodShoots,targetShoots,selfShoots,dimensions):
    fig = plt.gcf()
    ax = fig.gca()
    circle1 = plt.Circle((your_position[0],your_position[1]), distance, color='pink',alpha=0.5)

    ax.xaxis.set_major_locator(MultipleLocator(dimensions[0]))
    ax.yaxis.set_major_locator(MultipleLocator(dimensions[1]))
    ax.grid(which='major', color='#CCCCCC', linestyle='--')

    ax.add_patch(circle1)
    plt.scatter([t[0]+your_position[0] for t in targetShoots],[t[1]+your_position[1] for t in targetShoots],label='targets',color='red')
    plt.scatter([s[0]+your_position[0] for s in selfShoots],[s[1]+your_position[1] for s in selfShoots],label='selfs',color='blue')
    for shoot in goodShoots:
        plt.plot([your_position[0],your_position[0]+shoot[0]],[your_position[1],your_position[1]+shoot[1]],color='black',alpha=0.3)
    plt.scatter([your_position[0]],[your_position[1]],color='orange',label='first self',zorder=10)

    plt.legend()
    plt.show()

def visu2(your_position,distance,goodShoots,targetShoots,selfShoots,dimensions):
    fig = plt.gcf()
    ax = fig.gca()
    circle1 = plt.Circle((your_position[0],your_position[1]), distance, color='pink',alpha=0.5)

    ax.xaxis.set_major_locator(MultipleLocator(dimensions[0]))
    ax.yaxis.set_major_locator(MultipleLocator(dimensions[1]))
    ax.grid(which='major', color='#CCCCCC', linestyle='--')

    ax.add_patch(circle1)
    plt.scatter([distance*math.cos(float(a))+your_position[0] for a in targetShoots.keys() for distance in targetShoots[a]],[distance*math.sin(float(a))+your_position[1] for a in targetShoots.keys() for distance in targetShoots[a]],label='targets',color='red',zorder=8)
    plt.scatter([distance*math.cos(float(a))+your_position[0] for a in selfShoots.keys()   for distance in selfShoots[a]],  [distance*math.sin(float(a))+your_position[1] for a in selfShoots.keys()   for distance in selfShoots[a]],  label='selfs',  color='blue',zorder=8)
    for shootAngle in goodShoots.keys():
        plt.plot([your_position[0],your_position[0]+goodShoots[shootAngle]*math.cos(float(shootAngle))],[your_position[1],your_position[1]+goodShoots[shootAngle]*math.sin(float(shootAngle))],color='black',alpha=0.3)
    plt.scatter([your_position[0]],[your_position[1]],color='orange',label='first self',zorder=10)

    plt.legend()
    plt.show()


def visu3(your_position,distance,goodShoots,targetShoots,selfShoots,dimensions):
    fig = plt.gcf()
    ax = fig.gca()
    circle1 = plt.Circle((your_position[0],your_position[1]), distance, color='pink',alpha=0.5)

    ax.xaxis.set_major_locator(MultipleLocator(dimensions[0]))
    ax.yaxis.set_major_locator(MultipleLocator(dimensions[1]))
    ax.grid(which='major', color='#CCCCCC', linestyle='--')

    ax.add_patch(circle1)
    plt.scatter([t[0]+your_position[0] for t in targetShoots],[t[1]+your_position[1] for t in targetShoots],label='targets',color='red',zorder=8)
    plt.scatter([s[0]+your_position[0] for s in selfShoots],[s[1]+your_position[1] for s in selfShoots],label='selfs',color='blue',zorder=8)
    for shootAngle in goodShoots.keys():
        plt.plot([your_position[0],your_position[0]+goodShoots[shootAngle]*math.cos(float(shootAngle))],[your_position[1],your_position[1]+goodShoots[shootAngle]*math.sin(float(shootAngle))],color='black',alpha=0.3)
    plt.scatter([your_position[0]],[your_position[1]],color='orange',label='first self',zorder=10)

    plt.legend()
    plt.show()