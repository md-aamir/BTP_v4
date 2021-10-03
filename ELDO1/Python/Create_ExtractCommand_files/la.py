file1 = open('myfile.txt', 'w') 
a=96		
b=a+32
m=0
j=0
for i in range(4):
	m=0
	for j in range(a,b):
		m=m+1
		s="mem"+str(i)+"_"+str(j)+" "
		file1.write(s)
		if(m==8):
			file1.write("\n+ ")
			m=0
for i in range(4):
	m=0
	for j in range(a,b):
		m=m+1
		s="memB"+str(i)+"_"+str(j)+" "
		file1.write(s)
		if(m==8):
			file1.write("\n+ ")
			m=0