a1="abcabcabcabc"
b1=4

a2="abccbaabccba"
b2=2

def solution(s):
    numberOfMms=len(s)
    setOfColors=set(s)
    numberOfColors=len(setOfColors)
    for nbOfSlices in range(numberOfMms//numberOfColors,1,-1):
        if not numberOfMms%nbOfSlices:
            lengthOfSlice=numberOfMms//nbOfSlices
            errors=0
            for startingIndex in range(numberOfMms//nbOfSlices):
                if len(set(s[startingIndex::lengthOfSlice]))>1:
                    errors+=1
            if not errors:
                return(nbOfSlices)
    return(1)


print(solution(a1))
print(solution(a2))