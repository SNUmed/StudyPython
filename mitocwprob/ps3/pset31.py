from string import *
def countSubStringMatchRecursive(target,key):
    indexfound=find(target,key)
    length=len(target)

    if indexfound==-1:
        return 0
    else: 
        return 1+countSubStringMatchRecursive(target[indexfound+1:],key)

def countSubStringMatch(target,key):
    length=len(target)
    count=0
    start=0
    while start!=length:
        indexfound=find(target,key,start)
        if indexfound!=-1:
            count+=1
            start=indexfound+1
        else:
            break
    return count

a=input("target:")
b=input("key:")
print countSubStringMatchRecursive(a,b)
print countSubStringMatch(a,b)
