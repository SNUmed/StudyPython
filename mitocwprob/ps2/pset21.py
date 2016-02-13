n=input("give the number:")
for c in range(n/20+1):
    for b in range(((n-20*c)/9+1)):
        for a in range(((n-20*c-9*b)/6+1)):
            if 6*a+9*b+20*c==n:
                print (a,b,c)
