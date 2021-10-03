from random import randint
import copy
from memory import *

file1 = open("Input_test_pattern", 'w')


list1=[]
list0=[]
input_matrix=[]
for i in range(0,100):
		itext=[]
		for j in range(16):
			itext=itext+[randint(0,2**32-1)]
		input_matrix.append(itext)

Test_samples=100
input_matrix_cp=copy.deepcopy(input_matrix)


for x in range(Test_samples):
	filename="Input_pattern/Sample"+"_"+str(x)
	icmaker(input_matrix_cp[x],filename)
	
	s="["+str(input_matrix[x][0])
	file1.write(s)
	for y in range(1,16):
		s=", "+str(input_matrix[x][y])
		file1.write(s)
	s="] \n"
	file1.write(s)