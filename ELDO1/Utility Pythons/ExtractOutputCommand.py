file1 = open('Output.cir', 'w') 
					
b=128

x=1.2
y=0
z=0
m=1
j=0

for i in range(4):
	for j in range(b):
		s=".EXTRACT TRAN LABEL=BITS"+str(i)+str(j)+" FILE=Output yval( v(mem"+str(i)+"_"+str(j)+"),32n)"+"\n"
		file1.write(s)
