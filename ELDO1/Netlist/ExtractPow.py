file1 = open('Power.cir', 'w') 				
begin=0
dist=0.004
end=begin+dist
i=0
while begin<=4:
	s=".EXTRACT FILE=Power label = pow"+str(i)+" (1.2*integ(I(v0),"+str(begin)+"N,"+str(end)+"N)/"+str(dist)+"N)"+"\n"
	file1.write(s)
	begin=end
	end=begin+dist
	print(begin," ",end)
	i=i+1
