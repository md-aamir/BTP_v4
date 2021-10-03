file1 = open('Alter.cir', 'w') 
alt=100
temp=0
x=0
for i in range(alt):
		for x in range(2):
			s=".alter Class"+str(x+1)+"_Sample"+str(i+temp)+" \n.include 'Python/Side_Channel_Tests/TESTs/KnownKEY_UnkownIP/Group2/Class"+str(x+1)+"/Sample_"+str(i+temp)+"'\n\n"
			file1.write(s)
