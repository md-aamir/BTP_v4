from random import randint
import copy
from memory import *
from chacha import *
	
########################################################################
########################################################################
##################SAME KEY DIFFERENT DATA###############################
########################################################################
########################################################################

CONSTANT=[0x61707865, 0x3320646e,0x79622d32, 0x6b206574] # 0-3 CONSTANT
key=[0,0,0,0,0,0,0,0]
block_counter=0
nonce=[0,0,0]
key1=[]
enc_data=[0,0]*8
list1=[]
for i in range(len(key)):
	key1 = key1 + [randint(0,2**32-1)]

##### FIXED input vs pseudo-random input(OP of chacha)###################

# Dataset-1 pseudo-random data 
for i in range(0,300):
	nonce=enc_data[0:3]
	block_counter=block_counter+1
	state=CONSTANT+key1+[block_counter]+nonce
	enc_data=copy.deepcopy(state)
	chacha20(enc_data)
	list1.append(state)


Data1=copy.deepcopy(list1)


file1 = open("Group1_random", 'w')

for x in range(len(list1)):
	filename="Group1/RANDOM/Sample"+"_"+str(x)
	icmaker(Data1[x],filename)

for x in range(len(list1)):
	s="["+str(list1[x][0])
	file1.write(s)
	for y in range(1,16):
		s=", "+str(list1[x][y])
		file1.write(s)
	s="] \n"
	file1.write(s)


########Dataset-2 : FIXED input (block count and nonce)
# So only one IC is sufficient
#############################################################################################################

block_counter=0
nonce=[0,0,0]
enc_data=[0,0]*8



for i in range(3):
	nonce[i]=randint(0,2**32-1)
block_counter=randint(0,2**32-1)
state=CONSTANT+key1+[block_counter]+nonce
enc_data=copy.deepcopy(state)



state1=copy.deepcopy(state)


file2 = open("Group1_fix", 'w')

filename="Group1/FIX/Sample"+"_"+str(0)
icmaker(state1,filename)


s="["+str(state[0])
file2.write(s)
for y in range(1,16):
	s=", "+str(state[y])
	file2.write(s)
s="] \n"
file2.write(s)
