def newroot(x,n):
	if n==0:
		return 1
        else:
		return (newroot(x,n-1)+(x/newroot(x,n-1)))/2

x=float(input("input number:"))
print newroot (x,10)
