def tower(start,end,stay,n):
    if n==1:
        print start,'to',end
    else:
        tower(start,stay,end,n-1)
        tower(start,end,stay,1)
        tower(stay,end,start,n-1)
    
tower('a','b','c',2)
