from string import *

def subStringMatchExact(target,key):
    start=0
    length=len(target)
    matches=()
    while start!=length:
        found=find(target,key,start)
        if found!=-1:
            matches=matches+(found,)
            start=found+1
        else: 
            break
    return matches

a=input("input target:")
b=input("input key:")
print subStringMatchExact(a,b)


