from random import randint
import copy
from memory import *
from chacha import *

ciphertext=[2553823474, 2619279258, 1975432395, 3687353374, 1577607347, 3409359930, 2181721219, 2390469270, 2971280582, 3759755202, 421331067, 2939897727, 4225932362, 2608343454, 550785889, 3208382193] 
a=0
b=a+4
for a in range(4):
	b=a+4
	c=a+8
	d=a+12
	ciphertext[a] = (ciphertext[a] + ciphertext[b]) & 0xffffffff
	ciphertext[d] = rotate(ciphertext[d] ^ ciphertext[a], 16)
	ciphertext[c] = (ciphertext[c] + ciphertext[d]) & 0xffffffff
	ciphertext[b] = rotate(ciphertext[b] ^ ciphertext[c], 12)
	ciphertext[a] = (ciphertext[a] + ciphertext[b]) & 0xffffffff
	ciphertext[d] = rotate(ciphertext[d] ^ ciphertext[a], 8)
	ciphertext[c] = (ciphertext[c] + ciphertext[d]) & 0xffffffff
	ciphertext[b] = rotate(ciphertext[b] ^ ciphertext[c], 7)



print(ciphertext)
file2 = open("Output","r+")
Out=file2.read().split()
Out=Out[10:]
enc_text=[]
t=[]
for i in range(4):
    for j in range(128):
        s="*BITS"+str(i)+str(j)
        m=Out.index(s)
        temp=float(Out[m+2])
        if(temp>0.5):
            temp0="1"
        else:
            temp0="0"
        t.append(temp0)
        if(j%32==31):
            enc_text.append(t)
            t=[]
for x in range(len(enc_text)):
    enc_text[x].reverse()
    enc_text[x]="".join(enc_text[x])
for i in range(len(enc_text)):
    enc_text[i]=int(enc_text[i],2)
print(enc_text)
print(ciphertext==enc_text)
for i in range(len(ciphertext)):
	if(ciphertext[i]!= enc_text[i]):
		print("expected : ",ciphertext[i] , "Eldo : ", enc_text[i], " at " , i)
		SW=Binary(ciphertext[i])
		HW=Binary(enc_text[i])
		for i in range(len(SW)):
			if(SW[i]!=HW[i]):
				print(i)

#1. List reversal
#2. Extract value to dec
#3. Test :)


