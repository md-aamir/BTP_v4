file1 = open('myfile3.txt', 'w') 
					
b=128

x=1.2
y=0
z=0
m=1
j=0

for i in range(4):
	file1.write("\n+ ")
	for j in range(b):
		s=".EXTRACT TRAN LABEL=BITS FILE=Output yval( v(mem"+str(i)+"_"+str(j)+"),50n)"+"\n"
		file1.write(s)