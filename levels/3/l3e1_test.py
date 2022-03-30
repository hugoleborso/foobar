import numpy as np
a=[1, 2, 3, 4, 5, 6]
b=3
c=[1, 1, 1]
d=1

e=[1,2,1,3,6,8,4]

def solutionOld(l):
    luckyTriples=0
    for i,n in enumerate(l):
        #print(n)
        for j,m in enumerate(l[i+1:]):
            #print('  ',m)
            if not m%n:
                for p in l[i+j+2:]:
                    #print('      ',p)
                    if not p%m:
                        #print('     ','yes !')
                        luckyTriples+=1
    return(luckyTriples)


def solutionMiddle(l):
    luckyTriples=0
    numberChains={}
    for i,n in enumerate(l):
        for k in numberChains.keys():
            if n>=k and not n%k:
                numberChains[k][1].append((i,n))
        if n not in numberChains.keys():
            numberChains[n]=([i],[])
        else:
            numberChains[n][0].append(i)
    for c in numberChains.keys():
        for i in numberChains[c][0]:
            for j,p in numberChains[c][1]:
                if j>i:
                    for k,d in numberChains[p][1]:
                        if k>j:
                            luckyTriples+=1
    return(luckyTriples)

def solution(l):
    luckyTriples=0
    dividingIndexes=[]
    for i,n in enumerate(l):
        dividingIndexes.append([])
        for j,m in enumerate(l[:i]):
            if not n%m:
                dividingIndexes[i].append(j)
                luckyTriples+=len(dividingIndexes[j])
        
    return(luckyTriples)
    
print(solution(e))
                
            