from random import randint
import copy
from memory import *
from chacha import *
## Impact of different keys	
########## 2 - different known Key, Same input
CONSTANT=[0x61707865, 0x3320646e,0x79622d32, 0x6b206574] # 0-3 CONSTANT
key1=[0,0,0,0,0,0,0,0]
key2=[0xFFFFFFFF]*len(key1)

block_counter=0
nonce=[0,0,0]
enc_data=[0,0]*8
list1=[]
list2=[]

for i in range(0,1000):	
	for i in range(3):
		nonce[i]=randint(0,2**32-1)
	block_counter=randint(0,2**32-1)

	## 2 different input states
	state1=CONSTANT+key1+[block_counter]+nonce
	state2=CONSTANT+key2+[block_counter]+nonce
	list1.append(state1)
	list2.append(state2)


Data1=copy.deepcopy(list1)
Data2=copy.deepcopy(list2)


file1 = open("Group2_input1", 'w')
file2 = open("Group2_input2", 'w')

for x in range(len(list1)):
	filename="Group2/Class1/Sample"+"_"+str(x)
	icmaker(Data1[x],filename)

	filename="Group2/Class2/Sample"+"_"+str(x)
	icmaker(Data2[x],filename)

for x in range(len(list1)):
	s="["+str(list1[x][0])
	file1.write(s)
	for y in range(1,16):
		s=", "+str(list1[x][y])
		file1.write(s)
	s="] \n"
	file1.write(s)

for x in range(len(list2)):
	s="["+str(list2[x][0])
	file2.write(s)
	for y in range(1,16):
		s=", "+str(list2[x][y])
		file2.write(s)
	s="] \n"
	file2.write(s)
