##x=10
##i=1
##while(i<x):
##	if x%i==0:
##		print 'divisor',i
##	i=i+1
x=10
divisors=()
for i in range(1,x):
	if x%i==0:
		divisors=divisors+(i,)
print divisors
