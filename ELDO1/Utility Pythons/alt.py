file1 = open('Alter.cir', 'w') 
alt=120
for i in range(alt):
		for x in range(2):
			s=".alter Class"+str(x)+"_Sample"+str(i)+" \n.include 'Netlist/Power.cir' \n.include 'Class"+str(x)+"/Sample_"+str(i)+"'\n\n"
			file1.write(s)
