from random import randint
import copy
from utility.memory import *
from utility.chacha import *
	
list1=[]
list0=[]
plaintext=[]
for i in range(0,300):
		plaintext=[0x61707865, 0x3320646e,0x79622d32, 0x6b206574] # 0-3 CONSTANT
		for j in range(4,16):
			plaintext=plaintext+[randint(0,2**32-1)]
		enc_data=copy.deepcopy(plaintext)
		oneround(enc_data)
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


#Saving Variables states	
import shelve
filename='Attack_set_storage/listhere'
my_shelf = shelve.open(filename,'n') # 'n' for new

for key in dir():
    try:
        my_shelf[key] = globals()[key]
    except TypeError:
        #
        # __builtins__, my_shelf, and imported modules can not be shelved.
        #
        print('ERROR shelving: {0}'.format(key))
my_shelf.close()