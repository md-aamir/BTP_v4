from chacha import *
def Binary(n): 
    binary = "" 
    i = 0
    while i<32: 
        s1 = str(int(n%2)) 
        binary = binary + s1 
        n /= 2
        i = i+1
        d = binary[::-1] 
    return d

DATA=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def icmaker(DATA,filename):
	for x in range(16):
		DATA[x]=Binary(x)
	# ARRAY ELEMENTS OF DATA : HAVE STRING OF BINARY {msb----lsb}
	# BUT 0 INDEX IS OF MSB AND 32 INDEX IS LSB

	file1 = open(filename, 'w') 

	b=128
	x=1.2
	y=0
	z=0
	m=1
	j=0

	###########3
	id0=0
	id1=0
	c=0

	for i in range(4):
		file1.write("\n")
		id0=c
		id1=0
		for j in range(b):
			# print(id0," ",id1," ",i,"\n")
			if(DATA[id0][id1]=="1"):
				z=x
			else:
				z=y
			s=".ic v(mem"+str(i)+"_"+str(j)+")= "+str(z)+"v \n"
			file1.write(s)
			m=m*-1
			id1=id1+1
			if(id1==32):
				file1.write("\n")
				id1=0
				id0=id0+1

			#on 32 complete increase a and b=0

		id0=c
		id1=0
		for j in range(b):
			if(DATA[id0][id1]=="0"):
				z=x
			else:
				z=y
			s=".ic v(memB"+str(i)+"_"+str(j)+")= "+str(z)+"v \n"
			file1.write(s)
			m=m*-1
			id1=id1+1
			if(id1==32):
				file1.write("\n")
				id1=0
				id0=id0+1
		c=c+4