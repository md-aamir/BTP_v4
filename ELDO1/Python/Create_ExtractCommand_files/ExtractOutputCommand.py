file1 = open('Output.cir', 'w') 
					
b=32

x=1.2
y=0
z=0
m=1
j=0

for i in range(4):
	for j in range(b):
		s=".EXTRACT TRAN LABEL=BIT-"+str(i)+str(j)+" FILE=Output yval( v(mem"+str(i)+"_"+str(31-j)+"),890n)"+"\n"
		file1.write(s)

# for i in range(4):
# 	for j in range(b):
# 		s=".EXTRACT TRAN LABEL=BITS FILE=Output4 yval( v(mem"+str(i)+"_"+str(127-j)+"),810n)"+"\n"
# 		file1.write(s)


# for i in range(4):
# 	for j in range(b):
# 		s=".EXTRACT TRAN LABEL=BITS FILE=Output8 yval( v(mem"+str(i)+"_"+str(31-j)+"),8n)"+"\n"
# 		file1.write(s)


# for i in range(4):
# 	for j in range(b):
# 		s=".EXTRACT TRAN LABEL=BITS FILE=Output12 yval( v(mem"+str(i)+"_"+str(31-j)+"),12n)"+"\n"
# 		file1.write(s)

# for i in range(4):
# 	for j in range(b):
# 		s=".EXTRACT TRAN LABEL=BITS FILE=Output16 yval( v(mem"+str(i)+"_"+str(31-j)+"),16n)"+"\n"
# 		file1.write(s)


# for i in range(4):
# 	for j in range(b):
# 		s=".EXTRACT TRAN LABEL=BITS FILE=Output20 yval( v(mem"+str(i)+"_"+str(31-j)+"),20n)"+"\n"
# 		file1.write(s)


# for i in range(4):
# 	for j in range(b):
# 		s=".EXTRACT TRAN LABEL=BITS FILE=Output24 yval( v(mem"+str(i)+"_"+str(31-j)+"),24n)"+"\n"
# 		file1.write(s)


# for i in range(4):
# 	for j in range(b):
# 		s=".EXTRACT TRAN LABEL=BITS FILE=Output28 yval( v(mem"+str(i)+"_"+str(31-j)+"),28n)"+"\n"
# 		file1.write(s)

# for i in range(4):
# 	for j in range(b):
# 		s=".EXTRACT TRAN LABEL=BITS FILE=Output32 yval( v(mem"+str(i)+"_"+str(31-j)+"),32n)"+"\n"
# 		file1.write(s)	
