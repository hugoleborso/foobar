a=[3, 1, 4, 1]
b=4311
c=[3, 1, 4, 1, 5, 9]
d=94311



import itertools


def solution(l):
    all_numbers=[]
    all_perms=[]
    for n in range(1,len(l)+1):
        all_perms+=list(itertools.permutations(l,n))
    
    for perm in all_perms:
        nbStr=''
        for nb in perm:
            nbStr+=str(nb)
        all_numbers.append(int(nbStr))
    
    
    all_numbers.sort(reverse=True)
    for nb in all_numbers:
        if not nb%3:
            return(nb)
    return(0)
    
    
print(solution(c))
