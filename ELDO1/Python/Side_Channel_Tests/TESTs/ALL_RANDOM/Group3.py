from random import randint
import copy
from memory import *
from chacha import *

################Totally Random input states##############
list1=[]
list0=[]
plaintext=[]
for i in range(0,300):
		plaintext=[0x61707865, 0x3320646e,0x79622d32, 0x6b206574] # 0-3 CONSTANT
		for j in range(4,16):
			plaintext=plaintext+[randint(0,2**32-1)]
		enc_data=copy.deepcopy(plaintext)
		chacha20(enc_data)
		binary_rep=bin(enc_data[0])[2:] # first element of output of single round of chacha
		if(binary_rep[-1]=="1"):
			list1.append(plaintext)
		else:
			list0.append(plaintext)


Data1=copy.deepcopy(list1)
Data0=copy.deepcopy(list0)
Test_samples=min(len(list1),len(list0))
for x in range(Test_samples):
	filename="Class1/Sample"+"_"+str(x)
	icmaker(Data1[x],filename)
for x in range(Test_samples):
	filename="Class0/Sample"+"_"+str(x)
	icmaker(Data0[x],filename)


file1 = open("Group3_input1", 'w')
file0 = open("Group3_input0", 'w')

for x in range(len(list1)):
	s="["+str(list1[x][0])
	file1.write(s)
	for y in range(1,16):
		s=", "+str(list1[x][y])
		file1.write(s)
	s="] \n"
	file1.write(s)

for x in range(len(list0)):
	s="["+str(list0[x][0])
	file0.write(s)
	for y in range(1,16):
		s=", "+str(list0[x][y])
		file0.write(s)
	s="] \n"
	file0.write(s)