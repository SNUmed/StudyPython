
def Palindrome(string):
        

	if string=='':
		return True
	
	elif string[0]!=string[-1]:
		return False 
	
	else:
		return Palindrome(string[1:-2])

def chkpal():
	string=str(raw_input("input string to check: "))
	if Palindrome(string)==False:
		print "False"

	else:
		print "Ture"

chkpal()
