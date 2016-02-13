import math
count=0
n=1
while count<=1000:
    prime=1
    for i in range(int(math.sqrt(n))-1):
        if n%(i+2)==0:
            prime=0
            break
    if prime==1:
        print n
        count+=1
    n+=1
