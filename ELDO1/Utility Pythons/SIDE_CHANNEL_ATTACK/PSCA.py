from random import randint
import copy
from memory import *
randint(0,2**32-1)
list1=[]
list0=[]
plaintext=[]
for i in range(0,100):
		plaintext=[]
		for j in range(16):
			plaintext=plaintext+[randint(0,2**32-1)]
		enc_data=copy.deepcopy(plaintext)
		oneround(enc_data)
		if(bin(enc_data[0])[-1]=="1"):
			list1=list1+[plaintext]
		else:
			list0=list0+[plaintext]


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