a=('4', '7')
b=4
c=('2', '1')
d=1
e=("2","4")
f=("10000000000000003","7")

def solution(x,y):
    
    M=int(x)
    F=int(y)
    gen=0
    
    while M>1 or F>1:
        print(M,F)
        if M==1 or F==1:
            return(str(gen+M+F-2))
        
        elif M>F:
            if M%F:
                gen+=M//F
                M=M%F
            else:
                return('impossible')
            
        elif M<F:
            if F%M:
                gen+=F//M
                F=F%M
            else:
                return('impossible')
        else:
            return('impossible')
    
    else:
        return('impossible')

print(solution(f[0],f[1]))