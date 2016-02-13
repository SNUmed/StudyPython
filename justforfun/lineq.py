## solving a simple system of linear equation

def solve(numLegs,numHeads):
	for legs in range(numHeads):
		numPigs=legs
		numChicks=numHeads-numPigs
		if 2*numChicks+4*numPigs==numLegs:
			return (numPigs,numChicks)
        return (None,None)


def BarnYard():
	numLegs=int(raw_input("Give me the Legs: "))
	numHeads=int(raw_input("Give me the Heads: "))

	(numPigs,numChicks)=solve(numLegs,numHeads)

	print "number of Pigs:",numPigs," "
	print "number of Chicks:",numChicks


BarnYard()
