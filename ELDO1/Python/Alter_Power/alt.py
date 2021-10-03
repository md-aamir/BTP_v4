file1 = open('Alter.cir', 'w') 
alt=10
for i in range(alt):
		for x in range(2):
			s=".alter Class"+str(x)+"_Sample"+str(i)+" \n.include 'Netlist/Power.cir' \n.include 'Python/Side_Channel_Tests/TESTs/KnownKEY_UnkownIP/Group2/Class"+str(x+1)+"/Sample_"+str(i)+"'\n\n"
			file1.write(s)
