#Code to Make RREF out of matrix 
#Programming Using Recurssive Structure

import copy #copy module import to handle matrixs
#Debugging Code

#Check if there is non-zero element
def chk0col(mat):
	match=copy.deepcopy(mat)
	count=0
	for i in match:
		if match[count][0]!=0:
			return count
        	count+=1
	return 'yes'

#Minus two vector
def vecminus(vec1,vec2):
	vecch=copy.deepcopy(vec1)
	count=0
	for i in vec1:
		vecch[count]=vec1[count]-vec2[count]
                count+=1
        return vecch

#Remove 1st row and column from matrix
def reducrowcol(mat):
	match=copy.deepcopy(mat[1:])
	count=0
	for i in match:
		match[count]=match[count][1:]
		count+=1
        return match

#Remove 1st column
def reduccol(mat):
	match=copy.deepcopy(mat)
	count=0
	for i in match:
		match[count]=match[count][1:]
		count+=1
	return match

#Remove 1st row
def reducrow(mat):
	match=copy.deepcopy(mat[1:])
	return match

#Find Row size of Matrix
def matrowsize(mat):
	m=0
	for i in mat:
		m=m+1
        
	return m

#Add Zero Row
def add0row(mat):
	row0=[]
	for i in mat[0]:
		row0=row0+[0.0,]
        match=row0+mat
       
	return match

#Add Zero Column
def add0col(mat):
	match=copy.deepcopy(mat)
	count=0
	for i in match:
		match[count]=[0.0,]+match[count]
    	        count=count+1
   
	return match

#Find Column size of Matrix
def matcolsize(mat):
	n=0
	for i in mat[0]:
		n=n+1

	return n

#real multiply vector
def vecmul(vec,real):
	vecch=copy.deepcopy(vec)
	count=0
	for i in vecch:
		vecch[count]=real*vecch[count]
		count+=1
	return vecch

#Make 1st 1
def first1(vec):
	vecch=copy.deepcopy(vec)
	divisor=vecch[0]
	count=0
	for i in vecch:
		vecch[count]=(1.0/divisor)*vecch[count]
		count+=1
        return vecch

#Find 1st 1's column number in row
[[1.0, 1.0, -1.0, 0.0], [0.0, 1.0, -1.6666666666666665, -3.0], [0.0, 0.0, 1.0, 3.0000000000000004]]
[[1.0, 0.0, 0.0, 1.0000000000000004], [0.0, 1.0, 0.0, 2.0], [0.0, 0.0, 1.0, 3.0000000000000004]]
def find1(vec):
	vecch=copy.deepcopy(vec)
	count=0
	for i in vecch:
		if vecch[count]!=0:
			return count
	        count+=1	
        return 0

#Produce RREF of Matrix
def REF(mat):
#	print mat 
	check0=chk0col(mat)
#	print check0
	
	if matrowsize(mat)==1:
		if mat[0][0]==0:
			return mat
		else:
		        mat[0]=first1(mat[0])
	         	return mat
	
	elif check0=='yes':
		return [mat[0]]+add0col(REF(reducrowcol(mat)))
        
        else:
		non0=check0
		count=0

                mat[non0]=first1(mat[non0])                
   
		for i in mat:
			if count!=non0:
				vecsubstract=vecmul(mat[non0],mat[count][0])
			        mat[count]=vecminus(mat[count],vecsubstract)
                        count+=1
                

		temp=mat[0]
		mat[0]=mat[non0]
		mat[non0]=temp
                
                

#               newmat=mat[0]+add0col(REF(reducrowcol(mat)))
#		print mat
#		print reducrowcol(mat)
#		print REF(reducrowcol(mat))
#               print add0col(REF(reducrowcol(mat)))
#               print [mat[0]]+add0col(REF(reducrowcol(mat)))
#		print newmat 
 
                ref=[mat[0]]+add0col(REF(reducrowcol(mat)))
		return ref      
              

#Produce RREF 
def RREF(mat):
	ref=copy.deepcopy(REF(mat))
	lastindex=matrowsize(ref)-1
#	print lastindex
	chk1=0
	for i in range(lastindex):
		chk2=chk1+1
		for j in range(lastindex-chk1):
#                       print ref[lastindex-chk1]
#			print ref[lastindex-chk2]
			f1=find1(ref[lastindex-chk1])
#			print f1
			vecsubstract=vecmul(ref[lastindex-chk1],ref[lastindex-chk2][f1])
			ref[lastindex-chk2]=vecminus(ref[lastindex-chk2],vecsubstract)
#			print lastindex-chk1
#			print lastindex-chk2
		        chk2+=1
		chk1+=1
	
	

        rref=ref	
	return rref
  
	 

#Input Interface
def givemat():
#	simple=[[1,2,3,4,0],[4,5,6,7,0],[7,8,9,10,1],[11,25,45,11,2]]
#	simple=[[1,2,3],[4,5,6],[7,8,1]]
        simple=[[1.0,1.0,-1.0,0.0],[2.0,-1.0,3.0,9.0],[1.0,2.0,1.0,8.0]]
#	simple=[[2,3],[2,4]]
#	simple=[[0.0,0.0],[0.0,0.0]]
#	simple=[[5]]
#       simple=[[0]]
	print REF(simple)
	print RREF(simple)
#	print chk0col([[0,0],[6,-42]])
#       print chk0col([[0,0],[1,1]])
#	print chk0col([[0,0],[0,1]])
#       print REF(simple)
#	print add0col([[0.0,0.0],[0.0,0.0]])
#        print find1([0,0,1])
givemat()
